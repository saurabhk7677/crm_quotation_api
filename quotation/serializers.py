from rest_framework import serializers
from .models import Company,Quotation, Product

class CompanySerializer(serializers.ModelSerializer):
    #quotation = serializers.StringRelatedField(many=True, read_only=True)
    class Meta :
        model = Company
        fields = ['id', 'company_name', 'created_by', 'updated_by', 'created_on', 'updated_on']
        read_only_fields = ['created_by', 'updated_by', 'created_on', 'updated_on'] 

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ['id', 'product_name','created_by', 'updated_by', 'created_on', 'updated_on']
        read_only_fields = ['created_by', 'updated_by', 'created_on', 'updated_on'] 
class QuotationSerializer(serializers.ModelSerializer):
    #company = serializers.StringRelatedField(many=True, read_only=True)
    class Meta :
        model = Quotation
        fields=['id', 'company','quotation_json','total_price','total_quantity','quotation_no','finelize_quotations','is_active','created_by','updated_by','created_on', 'updated_on']
        read_only_fields=['quotation_no','finelize_quotations','is_active','created_by','updated_by', 'created_on', 'updated_on']

    
    