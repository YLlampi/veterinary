from django import forms
from .models import UserProfile


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'id_veterinarian',)

        """
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'num_whatsapp': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200',
                'placeholder': 'Ej. 987654321'
            }),
            'departamento': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }
        """
