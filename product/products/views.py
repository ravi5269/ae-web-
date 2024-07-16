from django.shortcuts import render

# Create your views here.

# your_app_name/views.py
from django.shortcuts import render, redirect
from products.form import InquiryForm
from .models import Product
from .models import About


def home(request):
    products = Product.objects.all()
    form = InquiryForm()
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    return render(request, "Home.html", {"products": products, "form": form})


def about_view(request):
    about = About.objects.first()  # Assuming there's only one entry
    return render(request, "about.html", {"about": about})


def inquiry_view(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success_url")  # Redirect to a success page
    else:
        form = InquiryForm()
    return render(request, "contact.html", {"form": form})
