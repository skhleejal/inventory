from django.shortcuts import render
from .models import Customer, Invoice

def home(request):
    return render(request, 'invoicemgmt/home.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'invoicemgmt/customer_list.html', {'customers': customers})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoicemgmt/invoice_list.html', {'invoices': invoices})
