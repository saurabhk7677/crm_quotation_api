from django.urls import path
from . import views

urlpatterns = [
    # company urls
    path('', views.CompanyRoot.as_view()),
    # path('', views.QuotationRoot.as_view()),
    # path('', views.ProductRoot.as_view()),
    
    path('compny/', views.CompanyListAPIView.as_view(), name='compines'),
    path('create-company/', views.CompanyCreateAPIView.as_view(), name='create-company'),
    path('retrive-company/<int:pk>/', views.CompanyRetrieveAPIView.as_view(), name='retrive-company'),
    path('update-company/<int:pk>/', views.CompanyUpdateAPIView.as_view(), name='update-company'),
    path('delete-company/<int:pk>/', views.CompanyDestroyAPIView.as_view(), name='delete-company'),

    #Product API urls
    path('product/', views.ProductListAPIView.as_view(), name='product'),
    path('create-product/', views.ProductCreateAPIView.as_view(), name='create-product'),
    path('retrive-product/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='retrive-product'),
    path('update-product/<int:pk>/', views.ProductUpdateAPIView.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', views.ProductDestroyAPIView.as_view(), name='delete-product'),

    #Quotation API urls 
    path('quotation/', views.QuotationListAPIView.as_view(), name='quotation'),
    path('create-quotation/', views.QuotationCreateAPIView.as_view(), name='create-quotation'),
    path('retrive-quotation/<int:pk>/', views.QuotationRetrieveAPIView.as_view(), name='retrive-quotation'),
    path('update-quotation/<int:pk>/', views.QuotationUpdateAPIView.as_view(), name='update-quotation'),
    path('delete-quotation/<int:pk>/', views.QuotationDestroyAPIView.as_view(), name='delete-quotation'),
]