from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # e.g., Home page for your app
    path('customers/', views.customer_list, name='customer_list'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('add_invoice/',views.create_invoice, name='create_invoice'),
]