from django import forms
from market.models import Market


class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields = ['name','short_description','long_description','price_per_unit','category','quantity_left','image',]
        
# class MarketUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Market
#         template_name = 'market_update_form.html'
#         fields = ['name','short_description','long_description','price_per_unit','category','image',]
        




    # name = models.CharField(max_length=100,unique=True)
    # dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    # short_description = models.CharField(max_length=150, null=True, blank=True)
    # long_description = models.TextField(null=True, blank=True)
    # price_per_unit = models.PositiveIntegerField()
    # category = models.CharField(max_length=100, choices=CATEGORY)
    # image = models.ImageField(null=True,blank=True, upload_to = upload_path) 

    # number_of_buyer = models.PositiveIntegerField(null=True, blank=True)
    # deal_rating = models.DecimalField(decimal_places=1, max_digits=5, null=True, blank=True)