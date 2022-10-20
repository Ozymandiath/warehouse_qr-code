from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

from .models import Product

User = get_user_model()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["part_name", "content", "availability"]
        widgets = {
            "part_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название товара"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Характеристики товара"
            }),
            "availability": forms.NumberInput(attrs={
                "class": "form-control",
            })
        }


class UserCustomForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
            })
            # "password1": forms.PasswordInput(attrs={
            #     "class": "form-control",
            #     "placeholder": "*******"
            # }),
            # "password2": forms.PasswordInput(attrs={
            #     "autocomplete": "new-password",
            #     "class": "form-control",
            #     "placeholder": "*******"
            # })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "placeholder": "*******"
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "placeholder": "*******"
        })


class LoginCustomForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,
                                                           "class": "form-control",
                                                           "placeholder": "Username"
                                                           }))
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "class": "form-control",
                                          "placeholder": "*******"
                                          }),
    )
