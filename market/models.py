from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


## category
CATEGORY = (
    ('solar','Solar Energy'),
    ('Biof','Biofuel'),
    ('water','Water Sources'),
    ('forest','Forest'),
)
##

class Market(models.Model):
    name = models.CharField(max_length=100)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=150, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    price_per_unit = models.PositiveIntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    
    #Number of buyers is necessary, it will be used to calculate the RCC later.
    #but I'm leaving it null=True just in case.
    number_of_buyer = models.PositiveIntegerField(null=True, blank=True)
    deal_rating = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)
    
    


    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self, **kwargs):
        pass

    def get_category_name(self):
        pass