from django.db import models
from django.urls import reverse
from profiles.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model

# Create your models here.
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


def verify_upload_path(instance, filename):
    return f'dealer/dealer_verify/{instance}/{filename}'
def upload_path(instance, filename):
    return f'dealer/dealer_icon/{instance}/{filename}'
class Dealer(models.Model):
    #is_dealer data
    user = models.OneToOneField(User,related_name='dealer_data',on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100, unique=True)
    deal_province = models.CharField(max_length=100, choices=PROVINCES)
    website = models.URLField(max_length=200, null=True, blank=True)
    shop_icon = models.ImageField(null=True,blank=True, upload_to = upload_path) 

    verify = models.FileField(upload_to=verify_upload_path, max_length=254)
    is_verify = models.BooleanField(default=False)

    def get_absolute_url(self, **kwargs):
        
        return reverse('profiles:profile_page', kwargs={'slug':self.user.profile.slug}) 
    def __str__(self):
        return f'{self.user.username}' 

    