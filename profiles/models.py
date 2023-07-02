from django.db import models
from django.urls import reverse
from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model

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
def upload_path(instance, filename):
    return f'profiles/{instance}/{filename}'

class Profile(models.Model):
    #remind about dealer 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_me = models.TextField(null=True,blank=True)
    province = models.CharField(max_length=100, choices=PROVINCES)
    image = models.ImageField(null=True,blank=True, upload_to = upload_path) 

    #hopefully i fixed the circular import
    deals = models.ManyToManyField(Market, blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    
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
