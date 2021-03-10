from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from django.core.mail import send_mail

from cart.cart import Cart
from confedencial import EMAIL_USER_CONFED
from user_reg_log.models import Profile


def order_create(request):
    dictionary = {}
    cart = Cart(request)
    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         price_x_items=item['total_price'],
                                         quantity=item['quantity'],
                                         total_price=cart.get_total_price(), )
                dictionary[str(item['product'])] = item['quantity']
            if request.user.is_authenticated:
                customer.orders.add(order)
            # очистка корзины
            cart.clear()
            # отправка сообщения
            result = '; \n'.join([f'{key.capitalize()}: x{value}' for key, value in dictionary.items()])
            cd = form.cleaned_data
            subject = 'Спасибо за заказ {}'.format(cd['first_name'])
            message = '{} {}, вами был произведён заказ на сайте kapkan.bel, номер заказа {}\n' \
                      'Состав заказа: {}.\nОбщей стоймостью: {} \nКомментарий к заказу: {}'.format(
                cd['last_name'], cd['first_name'], order.id, result, cart.get_total_price(), cd['comment_for_order']
            )
            send_mail(subject, message, f'{EMAIL_USER_CONFED}', [f'lehado67@gmail.com'], fail_silently=False)
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})
