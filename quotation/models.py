from django.db import models
from django.contrib.auth.models import User
import jsonfield


# Create your models here.

# company model
class Company(models.Model):
    company_name = models.CharField(max_length=150, null=True, unique=True)
    created_by = models.ForeignKey(User,related_name="comapany_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="comapany_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_name	

class Product(models.Model):
    product_name = models.CharField(max_length=150, null=True, unique=True)
    created_by = models.ForeignKey(User,related_name="product_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="product_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name	

class Quotation(models.Model):
    quotation_no = models.CharField(max_length=50, null=True, blank=True)
    company = models.ForeignKey(Company, related_name="company",on_delete=models.PROTECT)
    quotation_json = jsonfield.JSONField()
    total_quantity = models.IntegerField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User,related_name="quotation_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="quotation_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    finelize_quotations = models.BooleanField(default=False)   
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.quotation_json)
        

    
    