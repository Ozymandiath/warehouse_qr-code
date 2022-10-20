import os
import qrcode

from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.db import transaction
from django.views.generic import ListView

from localsite.settings import STATIC_URL
from .models import Product, OrderProduct, CustomUser
from .forms import ProductForm, UserCustomForm, LoginCustomForm


class HomeProduct(ListView):
    model = Product
    template_name = "scanner/parts_list.html"
    context_object_name = "parts"


class AddProduct(View):
    template_name = "scanner/add_product.html"
    form_class = ProductForm
    time = str(datetime.today().date()).replace("-", "\\")

    def get(self, request):
        context = {
            "form": self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instanse = form.save()
            img = qrcode.make(f"http://127.0.0.1:8000/parts/{instanse.id}")
            if not os.path.isdir(f"{STATIC_URL}\\image\\{self.time}"):
                os.makedirs(f"{STATIC_URL}\\image\\{self.time}")
            img.save(f"{STATIC_URL}\\image\\{self.time}\\{instanse.id}.png")
            add_image_base = Product.objects.get(pk=instanse.id)
            add_image_base.photo = f"image\\{self.time}\\{instanse.id}.png"
            add_image_base.save()
            messages.success(request, "Товар добавлен")
            return redirect("add")
        else:
            messages.error(request, "Ошибка заполнения")
            return render(request, self.template_name, {"form": form})


class AddUser(View):
    form_class = UserCustomForm
    template_name = "scanner/register_user.html"

    def get(self, request):
        context = {
            "form": self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password2")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            # messages.error(request, "Ошибка регистрации")
            return render(request, self.template_name, {"form": form})


class UserLogin(LoginView):
    form_class = LoginCustomForm
    template_name = "scanner/login.html"
    next_page = "home"


class DescriptionPart(View):
    model = Product
    template_name = "scanner/description.html"
    context_object_name = "part"

    def get(self, request, pk):
        post = Product.objects.get(pk=pk)
        return render(request, self.template_name, {"part": post})


class OrderListParts(ListView):
    model = OrderProduct
    template_name = "scanner/order_profile.html"
    context_object_name = "parts"


class SetOrderParts(View):

    @transaction.atomic
    def get(self, request, product_pk, user_pk):
        product_id = Product.objects.get(pk=product_pk)
        user_id = CustomUser.objects.get(pk=user_pk)
        product_id.availability -= 1
        product_id.save()
        OrderProduct.objects.create(order_id=product_id, user=user_id, availability=1)
        return redirect("home")


class OrderDelete(View):

    @transaction.atomic
    def get(self, request, order_pk):
        order = OrderProduct.objects.get(pk=order_pk)
        product_id = Product.objects.get(pk=order.order_id.pk)
        product_id.availability += 1
        product_id.save()
        order.delete()
        return redirect("profile")
