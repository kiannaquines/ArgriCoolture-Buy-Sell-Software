from django.shortcuts import render
from . import forms
from main.views import get_path
from main import models
import random
import string
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def generate_transaction_code():
    code_length = 12
    constant_code = "#LTABS"
    transform_digit = string.digits
    code = ''.join(random.choice(transform_digit) for _ in range(code_length))
    return constant_code + code

@login_required(login_url="/ams/")
def products_view(request):
    context = {}

    if request.method == "POST":
        product = models.Item.objects.get(item_id=request.POST.get("product_id"))
        user = models.CustomUser.objects.get(id=request.user.id)

        cart_data = models.Cart(
            user=user,
            order_quantity=1,
            item=product,
        )

        cart_data.save()
        messages.success(request,"You have successfully added your item in your cart.")

        return HttpResponseRedirect("/products/")

    context['products'] = models.Item.objects.all()
    context['products_path'] = get_path(request=request)
    
    return render(request,"products.html",context)

@login_required(login_url="/ams/")
def orders_view(request):
    context = {}
    
    context["order_history"] = models.Cart.objects.filter(is_checkedOut=True).filter(user=request.user.id)
    context['orders_path'] = get_path(request=request)
    return render(request,"my_orders.html",context)

@login_required(login_url="/ams/")
def place_order_view(request):
    context = {}
    
    context['place_order_path'] = get_path(request=request)
    return render(request,"place_order.html",context)

@login_required(login_url="/ams/")
def cart_view(request):
    from django.db.models import F, ExpressionWrapper, fields,Sum

    context = {}        

    if request.method == "POST":

        if "delete_my_item" in request.POST:
            cart_id = request.POST.get("cart_id")
            delete_exec = models.Cart.objects.filter(cart_id=cart_id)
            delete_exec.delete()
            messages.success(request,"Cart Item has been removed")

        if "checkout_product" in request.POST:
            products_ids = request.POST.getlist("product_id")
            item_ids = request.POST.getlist("item_id")

            for products_id in products_ids:

                # add cart
                cart_item = models.Cart.objects.get(cart_id=products_id)
                cart_item.is_checkedOut = True
                cart_item.save()

                # add transaction
                create_transaction = models.Transaction.objects.create(
                    transaction_id=generate_transaction_code(),
                    order_product=models.Item.objects.get(item_id=cart_item.item.item_id),
                    amount_per_product=cart_item.item.item_price,
                    user_transaction=models.CustomUser.objects.get(id=request.user.id),
                    quantity_per_product=cart_item.order_quantity,
                )

                # update the current stock here
                for item_id in item_ids:
                    update_stock = models.Item.objects.get(item_id=item_id)
                    update_stock.item_quantity = update_stock.item_quantity - cart_item.order_quantity

                    update_stock.save()

                create_transaction.save()

            messages.success(request,"You have successfully checkout your order.")

    cart_data = models.Cart.objects.filter(user=request.user.id).filter(is_checkedOut=False).annotate(
        total_amount=ExpressionWrapper(
            F('item__item_price') * F('order_quantity'),
            output_field=fields.DecimalField()
        ),
    )

    grand_total = cart_data.aggregate(total_sum=Sum('total_amount'))['total_sum']

    total_quantity = cart_data.aggregate(total_quantity=Sum('order_quantity'))['total_quantity']

    context['cart_data'] = cart_data
    context['grand_total'] = grand_total
    context['order_quantity'] = total_quantity
    context['cart_path'] = get_path(request=request)
    return render(request,"my_cart.html",context)

@login_required(login_url="/ams/")
def create_products_view(request):
    context = {}

    if request.method == "POST":
        product_create_form = forms.SellForm(request.POST,request.FILES)

        if product_create_form.is_valid():
            product_create_form.save()
            messages.success(request,"You have successfully created your product.")

            return HttpResponseRedirect("/create_product/")
        else:
            print(product_create_form.errors)
    context['form'] = forms.SellForm()
    context['products_path'] = get_path(request=request)
    return render(request,"create_product.html",context)


# TODO: This will be done tomorrow
@login_required(login_url="/ams/")
def edit_number_of_order(request,pk):
    context = {}

    instance = models.Cart.objects.get(cart_id=pk)

    if request.method == "POST":
        update_form = forms.UpdateOrderQuantityForm(request.POST,instance=instance)

        if update_form.is_valid():
            update_form.save()
            messages.success(request,"You have successfully updated the quantity of your order.",extra_tags="update_quantity")
            return HttpResponseRedirect(reverse_lazy('my_cart'))

    context['form'] = forms.UpdateOrderQuantityForm(instance=instance)
    context['id'] = instance.cart_id
    return render(request,"update_order.html",context)
