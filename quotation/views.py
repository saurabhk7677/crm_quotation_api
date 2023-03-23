from django.shortcuts import render
from rest_framework.reverse import reverse
from django.db import transaction
from rest_framework import generics
from rest_framework.response import Response
from .models import Company, Quotation, Product
from .serializers import CompanySerializer, QuotationSerializer, ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# Create your views here.

class Root(generics.GenericAPIView):
    name = 'root'
    def get(self, request, *args, **kwargs):
        return Response(
            {
                'company': reverse(CompanyRoot.name, request=request),
                'product': reverse(ProductRoot.name, request=request),
                'quotation': reverse(QuotationRoot.name, request=request),
            }
        )
class CompanyRoot(generics.GenericAPIView):
    name = 'company-api-root'
    def get(self, request, *args, **kwargs):
       return Response(
           {
               'compny-list': reverse(CompanyListAPIView.name, request=request),
               'create-company': reverse(CompanyCreateAPIView.name, request=request),
            #    'retrive-company': reverse(CompanyRetrieveAPIView.name, request=request),
            #    'update-company': reverse(CompanyUpdateAPIView.name, request=request),
            #    'delete-company': reverse(CompanyDestroyAPIView.name, request=request),

            }
       )
class ProductRoot(generics.GenericAPIView):
    name = 'product-api-root'
    def get(self, request, *args, **kwargs):
       return Response(
           {
                'product': reverse(ProductListAPIView.name, request=request),
                'create-product' : reverse(ProductCreateAPIView.name, request=request),
                # 'retrive-product' : reverse(ProductRetrieveAPIView.name, request=request),
                # 'update-product' : reverse(ProductUpdateAPIView.name, request=request),
                # 'delete-product' : reverse(ProductDestroyAPIView.name, request=request),
            }
       )
       
class QuotationRoot(generics.GenericAPIView):
    name = 'quotation-api-root'
    def get(self, request, *args, **kwargs):
       return Response(
           {
                'quotation': reverse(QuotationListAPIView.name, request=request),
                'create-quotation' : reverse(QuotationCreateAPIView.name, request=request),
            }
       )


#Company.............
class CompanyListAPIView(ListAPIView):
    name = 'compines'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyCreateAPIView(CreateAPIView):
    name = 'create-company'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def post(self, request):
        company_name = request.data.get('company_name')
        created_by = request.user
        updated_by = request.user
        company = Company.objects.create(company_name=company_name, created_by=created_by, updated_by=updated_by)
        company.save()
        return Response({"Success": "The Company Created Successfully!"}) 
    
class CompanyRetrieveAPIView(RetrieveAPIView):
    name = 'retrive-company'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyUpdateAPIView(UpdateAPIView):
    name = 'companyupdate'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyDestroyAPIView(DestroyAPIView):
    name = 'companydestroy'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#Product.....
class ProductListAPIView(ListAPIView):
    name = 'product'
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductCreateAPIView(CreateAPIView):
    name = 'create-product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def post(self, request):
        product_name = request.data.get('product_name')
        created_by = request.user
        updated_by = request.user
        product = Product.objects.create(product_name=product_name, created_by=created_by, updated_by=updated_by)
        product.save()
        return Response({"Success": "The Product Created Successfully!"}) 
    
class ProductRetrieveAPIView(RetrieveAPIView):
    name = 'retrive-Product'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(UpdateAPIView):
    name = 'product-update'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDestroyAPIView(DestroyAPIView):
    name = 'product-destroy'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Quotation............
class QuotationListAPIView(ListAPIView):
    name = 'quotation'
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class QuotationCreateAPIView(CreateAPIView):
    name = 'create-quotation'
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

    def post(self, request):
        company_id=request.data.get('company')
        print('comapny:',company_id)
        company = Company.objects.filter(id=company_id).first()
        product_json=request.data.get('quotation_json')
        total_quantity=request.data.get('total_quantity')
        total_price=request.data.get('total_price')
         
            # save data
        with transaction.atomic():
            obj = Quotation.objects.create(company=company, quotation_json=product_json, total_quantity=total_quantity, total_price=total_price, created_by=request.user, updated_by=request.user)
            obj.save()
                        
            quotation_prefix = "QUT-"
            quotation_ids = quotation_prefix+"{0:09d}".format(obj.id)
            obj.quotation_no = quotation_ids
            obj.save()
            return Response({"ok":"quotation add"})
            
class QuotationRetrieveAPIView(RetrieveAPIView):
    name = 'retrive-quotation'
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class QuotationUpdateAPIView(UpdateAPIView):
    name = 'update-quotation'
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class QuotationDestroyAPIView(DestroyAPIView):
    name = 'delete-quotation'
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer