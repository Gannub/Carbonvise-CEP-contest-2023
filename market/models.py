from django.db import models
from django.contrib.auth import get_user_model
from market.utils import check_slug_unique
from django.db.models.signals import pre_save, post_save
User = get_user_model()


## category
CATEGORY = (
    ('solar','Solar Energy'),
    ('Biof','Biofuel'),
    ('water','Water Sources'),
    ('forest','Forest'),
)
##
def upload_path(instance, filename):
    return f'market/{instance}/{filename}'

class Market(models.Model):
    name = models.CharField(max_length=100,unique=True)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    price_per_unit = models.PositiveIntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    image = models.ImageField(null=True,blank=True, upload_to = upload_path) 
    
    #Number of buyers is necessary, it will be used to calculate the RCC later.
    #but I'm leaving it null=True just in case.
    number_of_buyer = models.PositiveIntegerField(null=True, blank=True)
    deal_rating = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    
    slug = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self, **kwargs):
        pass

    def get_category_name(self):

        for cat in CATEGORY:
            if self.category == cat[0]:
                return cat[1]
        

def pre_save_slug_field(sender, instance, *arg ,**kwargs):  # sent at the beginning of a model’s save() 
        if not instance.slug:
            instance.slug = check_slug_unique(instance)

pre_save.connect(pre_save_slug_field, sender=Market)