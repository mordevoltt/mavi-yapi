from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'phone', 'email', 'district', 'service_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 placeholder-gray-400',
                'placeholder': 'Adınız ve Soyadınız',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 placeholder-gray-400',
                'placeholder': '05XX XXX XX XX',
                'type': 'tel',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 placeholder-gray-400',
                'placeholder': 'E-posta adresiniz (İsteğe bağlı)'
            }),
            'district': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 placeholder-gray-400',
                'placeholder': 'İlçe / Mahalle (Örn: Kadıköy, Bostancı)',
                'required': True
            }),
            'service_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 bg-white cursor-pointer',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-amber-500 focus:border-amber-500 transition outline-none text-gray-800 placeholder-gray-400',
                'rows': 4,
                'placeholder': 'Yapılmasını istediğiniz iş hakkında kısa bilgi verin (Örn: 120m2 dairenin banyo ve salon tadilatı veya 50m bahçe taş duvarı)',
                'required': True
            }),
        }

