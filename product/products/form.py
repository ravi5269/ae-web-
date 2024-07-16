# your_app_name/forms.py
from django import forms
from products.models import Contact


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "company_name",
            "email",
            "contact_number",
            "product",
            "message",
        ]
