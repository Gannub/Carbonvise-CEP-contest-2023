from django.db import models
from django.urls import reverse
from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.utils import timezone
from market.models import Market
    
User = get_user_model()

PROVINCES=(('1', 'กรุงเทพมหานคร'),
 ('2', 'สมุทรปราการ'),
 ('3', 'นนทบุรี'),
 ('4', 'ปทุมธานี'),
 ('5', 'พระนครศรีอยุธยา'),
 ('6', 'อ่างทอง' ),
 ('7', 'ลพบุรี'),
 ('8', 'สิงห์บุรี'),
 ('9', 'ชัยนาท'),
 ('10', 'สระบุรี'),
 ('11', 'ชลบุรี'),
 ('12', 'ระยอง'),
 ('13', 'จันทบุรี'),
 ('14', 'ตราด'),
 ('15', 'ฉะเชิงเทรา'),
 ('16', 'ปราจีนบุรี'),
 ('17', 'นครนายก'),
 ('18', 'สระแก้ว'),
 ('19', 'นครราชสีมา'),
 ('20', 'บุรีรัมย์'),
 ('21', 'สุรินทร์'),
 ('22', 'ศรีสะเกษ'),
 ('23', 'อุบลราชธานี'),
 ('24', 'ยโสธร'),
 ('25', 'ชัยภูมิ'),
 ('26', 'อำนาจเจริญ'),
 ('27', 'บึงกาฬ'),
 ('28', 'หนองบัวลำภู'),
 ('29', 'ขอนแก่น'),
 ('30', 'อุดรธานี'),
 ('31', 'เลย'),
 ('32', 'หนองคาย'),
 ('33', 'มหาสารคาม'),
 ('34', 'ร้อยเอ็ด'),
 ('35', 'กาฬสินธุ์'),
 ('36', 'สกลนคร'),
 ('37', 'นครพนม'),
 ('38', 'มุกดาหาร'),
 ('39', 'เชียงใหม่'),
 ('40', 'ลำพูน'),
 ('41', 'ลำปาง'),
 ('42', 'อุตรดิตถ์'),
 ('43', 'แพร่'),
 ('44', 'น่าน'),
 ('45', 'พะเยา'),
 ('46', 'เชียงราย'),
 ('47', 'แม่ฮ่องสอน'),
 ('48', 'นครสวรรค์'),
 ('49', 'อุทัยธานี'),
 ('50', 'กำแพงเพชร'),
 ('51', 'ตาก'),
 ('52', 'สุโขทัย'),
 ('53', 'พิษณุโลก'),
 ('54', 'พิจิตร'),
 ('55', 'เพชรบูรณ์'),
 ('56', 'ราชบุรี'),
 ('57', 'กาญจนบุรี'),
 ('58', 'สุพรรณบุรี'),
 ('59', 'นครปฐม'),
 ('60', 'สมุทรสาคร'),
 ('61', 'สมุทรสงคราม'),
 ('62', 'เพชรบุรี'),
 ('63', 'ประจวบคีรีขันธ์'),
 ('64', 'นครศรีธรรมราช'),
 ('65', 'กระบี่'),
 ('66', 'พังงา'),
 ('67', 'ภูเก็ต'),
 ('68', 'สุราษฎร์ธานี'),
 ('69', 'ระนอง'),
 ('70', 'ชุมพร'),
 ('71', 'สงขลา'),
 ('72', 'สตูล'),
 ('73', 'ตรัง'),
 ('74', 'พัทลุง'),
 ('75', 'ปัตตานี'),
 ('76', 'ยะลา'),
 ('77', 'นราธิวาส'))
#seperate calls to avoid circular import.
# class User(AbstractUser):
#     pass


ACHIEVEMENTS = [
    {"name": "สิบเครดิตแรก", "threshold": 10},
    {"name": "คนขี้ร้อน", "threshold": 50},
    {"name": "Gold", "threshold": 100},
    {"name": "diamond", "threshold": 200},
    {"name": "ruby", "threshold": 500},
    
]


def upload_path(instance, filename):
    return f'profiles/{instance}/{filename}'

class Profile(models.Model):
    #remind about dealer 
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    about_me = models.TextField(null=True,blank=True)
    province = models.CharField(max_length=100, choices=PROVINCES)
    image = models.ImageField(null=True,blank=True, upload_to = upload_path) 

    #hopefully i fixed the circular import
    deals = models.ManyToManyField(Market, blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    @property
    def get_slug(self):
        return(self.slug)
    
    def get_absolute_url(self, **kwargs):
        return reverse('profiles:profile_page', kwargs={'slug':self.slug}) 
    
    @property
    def get_province_name(self):
        for province in PROVINCES:
            if self.province == province[0]:
                return province[1]

def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
    if not instance.slug:
        instance.slug = check_slug_unique(instance)
pre_save.connect(pre_save_slug_field, sender=Profile)

def post_save_profile_create(sender ,instance, created, *arg, **kwargs): # sent at the end of the save()
    if created:
        Profile.objects.create(user=instance)
post_save.connect(post_save_profile_create, sender=User)




def upload_path(instance, filename):
    return f'static_achievements/{filename}'

class Achievement(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to=upload_path, null=True,blank=True)
    credit_goal = models.PositiveIntegerField(null=True,blank=True)
    des1 = models.TextField(null=True,blank=True)
    des2 = models.TextField(null=True,blank=True) 
    image_compare = models.ImageField(upload_to=upload_path, null=True,blank=True)

    def __str__(self):
        return f'{self.name} - {self.credit_goal}'




class CreditSession(models.Model):
    user = models.OneToOneField(User,related_name='profile_credit',on_delete=models.CASCADE)
    session_name = models.CharField(max_length=20, null=True, blank=True)
    session_des = models.TextField(null=True,blank=True)
    credits = models.IntegerField(default=0)
    is_neutral = models.BooleanField(default=False)
    session_active = models.BooleanField(default=False)
    achievements = models.ManyToManyField(Achievement, blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    reset_date = models.DateTimeField(null=True,blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user} | {self.credits}"
    @property
    def checkNeutral(self):
        credits_goal = 300

        if self.credits >= credits_goal and not self.is_neutral:
            self.is_neutral = True
            self.save()
        elif self.credits < credits_goal and self.is_neutral:
            self.is_neutral = False
            self.save()


    #apply achievements here
    @property
    def assignAch(self):    
        for achievement in ACHIEVEMENTS:
            achievement_name = achievement['name']
            achievement_threshold = achievement['threshold']

            if self.credits >= achievement_threshold and self.achievements.filter(name=achievement_name).count() == 0:
                achievement_to_add , created = Achievement.objects.get_or_create(name=achievement_name)

                self.achievements.add(achievement_to_add)
        

def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
    if not instance.slug:
        instance.slug = check_slug_unique(instance)
pre_save.connect(pre_save_slug_field, sender=CreditSession)

class CreditHistory(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=100, null=True, blank=True)
    session_des = models.TextField(null=True,blank=True)
    credits_of_month = models.IntegerField()
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    is_neutral = models.BooleanField(default=False)  
    slug = models.SlugField(unique=True, null=True, blank=True)


    def __str__(self):
        return f"{self.user} - {self.credits_of_month} credits - {self.start_date}"