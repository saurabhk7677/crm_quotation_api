from django.contrib import admin
from .models import Company, Quotation, Product
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'created_by', 'updated_by', 'created_on', 'updated_on', 'is_active']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'created_by', 'updated_by', 'created_on', 'updated_on', 'is_active']

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['id', 'quotation_no', 'company', 'quotation_json', 'total_quantity', 'total_price', 'created_by', 'updated_by', 'created_on', 'updated_on', 'finelize_quotations', 'is_active']
   