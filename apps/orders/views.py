from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order, OrderTotalPrice
from .forms import OrderCreateForm
from django.core.mail import send_mail

from apps.cart import Cart
from confedencial import EMAIL_ADMIN_CONFED
from apps.user_reg_log.models import Profile


def order_create(request):
    dictionary = {}
    cart = Cart(request)
    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            OrderTotalPrice.objects.create(order_id=order)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         price_x_items=item['total_price'],
                                         quantity=item['quantity'],)
                dictionary[str(item['product'])] = item['quantity']
            if request.user.is_authenticated:
                customer.orders.add(order)
            cart.clear()
            # send message
            result = '; \n'.join([f'{key.capitalize()}: x{value}' for key, value in dictionary.items()])
            cd = form.cleaned_data
            subject_for_customer = 'Спасибо за заказ {}'.format(cd['first_name'])
            message_for_customer = '{} {}, вами был произведён заказ на сайте kapkan2.bel, номер заказа {}\n '\
                                   'Состав заказа: {}.\nОбщей стоймостью: {} \nКомментарий к заказу: {}'.format(
                cd['last_name'], cd['first_name'], order.id, result, cart.get_total_price(), cd['comment_for_order']
            )
            subject_for_admin = 'Произведён заказ'
            message_for_admin = 'Произведён заказ, номер заказа {}\n '\
                                'Состав заказа: {}.\nОбщей стоймостью: {} \nКомментарий к заказу: {}'.format(
                order.id, result, cart.get_total_price(), cd['comment_for_order']
            )
            send_mail(subject_for_customer, message_for_customer, f'{EMAIL_ADMIN_CONFED}',
                      [cd['email']], fail_silently=False)
            send_mail(subject_for_admin, message_for_admin, f'{EMAIL_ADMIN_CONFED}',
                      [EMAIL_ADMIN_CONFED], fail_silently=False)

            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})
