import os, django, random
os.environ['DJANGO_SETTINGS_MODULE'] = 'carbonvise.settings'
django.setup()
import random

from django.contrib.auth import get_user_model
User = get_user_model()
from profiles.models import CreditSession
from market.models import Market

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

#fake 10 dealers test

# dealers = [{
#     'username':f'userset{num}',
#     'first_name':f'set{num}',
#     'last_name':f'theory{num}',
#     'email':f'set{num}@dev.com',
#     'province':random.randint(1,78),
    
# } for num in range (0,1000)] 

# for dealer in dealers:
#     User.objects.create_user(password='111111', **dealer)

# users = User.objects.all()
# session = CreditSession.objects.all()

# for user in session:
#     credits = random.randint(500,4000)
#     user.credits = credits
#     user.save()





#fake deals 

users = User.objects.filter(username__icontains='12')


CATEGORY = (
    ('solar','Solar Energy'),
    ('Biof','Biofuel'),
    ('water','Water Sources'),
    ('forest','Forest'),
)

def dummy_text(num):
    lorem_text = 'placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available. It is also used to temporarily replace text in a process called greeking, which allows designers to consider the form of a webpage or publication, without the meaning of the text influencing the design'.split(' ')
    result = [random.choice(lorem_text) for i in range(num)]
    return ' '.join(result)
print(dummy_text(7))         
    


for user in users:
    deal_entries = random.randint(1,3)
    for deal in range(deal_entries):
        # dealer = user
        name = dummy_text(4)
        short_description = dummy_text(10)
        long_description = dummy_text(40)
        price_per_unit = random.randint(20,100) 
        category = random.choice(CATEGORY)[0]
        n_of_buyer = random.randint(1,1000)

        deal_object = Market.objects.get_or_create(
            dealer=user,
            name=name,
            short_description=short_description,
            long_description=long_description,
            price_per_unit=price_per_unit,
            category=category,
            quantity_left = n_of_buyer,
        )
        
        # print(deal_object)









    # name = models.CharField(max_length=100)
    # dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    # short_description = models.CharField(max_length=150, null=True, blank=True)
    # long_description = models.TextField(null=True, blank=True)
    # price_per_unit = models.PositiveIntegerField()
    # category = models.CharField(max_length=100, choices=CATEGORY)
    
    # #Number of buyers is necessary, it will be used to calculate the RCC later.
    # #but I'm leaving it null=True just in case.
    # number_of_buyer = models.PositiveIntegerField(null=True, blank=True)
    # deal_rating = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
