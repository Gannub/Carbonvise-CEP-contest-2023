import os, django, random
os.environ['DJANGO_SETTINGS_MODULE'] = 'carbonvise.settings'
django.setup()


from django.contrib.auth import get_user_model
User = get_user_model()

from market.models import Market



#fake 10 dealers test

dealers = [{
    'username':f'dealer{num}',
    'first_name':f'dealer{num}',
    'last_name':f'dealer{num}',
    'email':f'dealer{num}@dev.com',
    
} for num in range (0,10)] 

for dealer in dealers:
    User.objects.create_user(password='111111', **dealer)


#fake deals 

users = User.objects.filter(username__icontains='dealer')

PROVINCES=(('1', 'กรุงเทพมหานคร'),
 ('2', 'จังหวัดสมุทรปราการ'),
 ('3', 'จังหวัดนนทบุรี'),
 ('4', 'จังหวัดปทุมธานี'),
 ('5', 'จังหวัดพระนครศรีอยุธยา'),
 ('6', 'จังหวัดอ่างทอง' ),
 ('7', 'จังหวัดลพบุรี'),
 ('8', 'จังหวัดสิงห์บุรี'),
 ('9', 'จังหวัดชัยนาท'),
 ('10', 'จังหวัดสระบุรี'),
 ('11', 'จังหวัดชลบุรี'),
 ('12', 'จังหวัดระยอง'),
 ('13', 'จังหวัดจันทบุรี'),
 ('14', 'จังหวัดตราด'),
 ('15', 'จังหวัดฉะเชิงเทรา'),
 ('16', 'จังหวัดปราจีนบุรี'),
 ('17', 'จังหวัดนครนายก'),
 ('18', 'จังหวัดสระแก้ว'),
 ('19', 'จังหวัดนครราชสีมา'),
 ('20', 'จังหวัดบุรีรัมย์'),
 ('21', 'จังหวัดสุรินทร์'),
 ('22', 'จังหวัดศรีสะเกษ'),
 ('23', 'จังหวัดอุบลราชธานี'),
 ('24', 'จังหวัดยโสธร'),
 ('25', 'จังหวัดชัยภูมิ'),
 ('26', 'จังหวัดอำนาจเจริญ'),
 ('27', 'จังหวัดบึงกาฬ'),
 ('28', 'จังหวัดหนองบัวลำภู'),
 ('29', 'จังหวัดขอนแก่น'),
 ('30', 'จังหวัดอุดรธานี'),
 ('31', 'จังหวัดเลย'),
 ('32', 'จังหวัดหนองคาย'),
 ('33', 'จังหวัดมหาสารคาม'),
 ('34', 'จังหวัดร้อยเอ็ด'),
 ('35', 'จังหวัดกาฬสินธุ์'),
 ('36', 'จังหวัดสกลนคร'),
 ('37', 'จังหวัดนครพนม'),
 ('38', 'จังหวัดมุกดาหาร'),
 ('39', 'จังหวัดเชียงใหม่'),
 ('40', 'จังหวัดลำพูน'),
 ('41', 'จังหวัดลำปาง'),
 ('42', 'จังหวัดอุตรดิตถ์'),
 ('43', 'จังหวัดแพร่'),
 ('44', 'จังหวัดน่าน'),
 ('45', 'จังหวัดพะเยา'),
 ('46', 'จังหวัดเชียงราย'),
 ('47', 'จังหวัดแม่ฮ่องสอน'),
 ('48', 'จังหวัดนครสวรรค์'),
 ('49', 'จังหวัดอุทัยธานี'),
 ('50', 'จังหวัดกำแพงเพชร'),
 ('51', 'จังหวัดตาก'),
 ('52', 'จังหวัดสุโขทัย'),
 ('53', 'จังหวัดพิษณุโลก'),
 ('54', 'จังหวัดพิจิตร'),
 ('55', 'จังหวัดเพชรบูรณ์'),
 ('56', 'จังหวัดราชบุรี'),
 ('57', 'จังหวัดกาญจนบุรี'),
 ('58', 'จังหวัดสุพรรณบุรี'),
 ('59', 'จังหวัดนครปฐม'),
 ('60', 'จังหวัดสมุทรสาคร'),
 ('61', 'จังหวัดสมุทรสงคราม'),
 ('62', 'จังหวัดเพชรบุรี'),
 ('63', 'จังหวัดประจวบคีรีขันธ์'),
 ('64', 'จังหวัดนครศรีธรรมราช'),
 ('65', 'จังหวัดกระบี่'),
 ('66', 'จังหวัดพังงา'),
 ('67', 'จังหวัดภูเก็ต'),
 ('68', 'จังหวัดสุราษฎร์ธานี'),
 ('69', 'จังหวัดระนอง'),
 ('70', 'จังหวัดชุมพร'),
 ('71', 'จังหวัดสงขลา'),
 ('72', 'จังหวัดสตูล'),
 ('73', 'จังหวัดตรัง'),
 ('74', 'จังหวัดพัทลุง'),
 ('75', 'จังหวัดปัตตานี'),
 ('76', 'จังหวัดยะลา'),
 ('77', 'จังหวัดนราธิวาส'))

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
