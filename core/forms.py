from django import forms
from core.models import Contact, Product

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'message', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'الاسم', 'class': 'input-text', 'dir': 'rtl'})
        self.fields['message'].widget.attrs.update({'placeholder': 'الرسالة', 'class': 'input-textarea', 'dir': 'rtl'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'رقم الهاتف', 'class': 'input-text', 'dir': 'rtl'})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug']