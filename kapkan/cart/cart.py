import math
from decimal import Decimal
from django.conf import settings

from shop.models import Product
from user_reg_log.models import Profile


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.user_id = self.session.get('user_id')
        self.discount_order = 0

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.get_price())}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    @property
    def coupon(self):
        if self.user_id:
            customer = Profile.objects.get(id=self.user_id)
            return customer.bonus_points, customer
        return None

    def get_discount(self):
        if self.coupon:
            bonus_points, customer = self.coupon
            max_discount = self.get_total_price() * (Decimal(10) / Decimal(100))
            print(bonus_points, customer)
            print(max_discount, 'max_discount')
            print(bonus_points, 'bonus_points')
            discount = max_discount - bonus_points
            print(discount, 'discount')
            if bonus_points == 0:
                print(customer.bonus_points, '==')
                return Decimal('0')
            elif discount < 0:
                bonus_points = bonus_points - max_discount
                customer.bonus_points = math.floor(bonus_points)
                customer.save()
                print(customer.bonus_points, '<')
                self.discount_order = max_discount
            elif discount > 0:
                customer.bonus_points = 0
                customer.save()
                print(customer.bonus_points, '>')
                self.discount_order = discount
            else:
                customer.bonus_points = 0
                customer.save()
                print(customer.bonus_points, '!=')
                self.discount_order = max_discount
            print(self.discount_order, 'discount_order')
            # self.session['discount_order'] = list(float(self.discount_order))
            # self.session.modified = True
            return self.discount_order
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        del self.session['user_id']
        # del self.session['discount_order']
        self.session.modified = True
