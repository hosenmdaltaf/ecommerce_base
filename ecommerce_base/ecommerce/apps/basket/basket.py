from decimal import Decimal

from django.conf import settings
from ecommerce.apps.catalogue.models import Product
from ecommerce.apps.checkout.models import DeliveryOptions


class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket


    # def add(self, product_id, quantity=1, update_quantity=False):
    #     product_id = str(product_id)
        
    #     if product_id not in self.cart:
    #         self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
    #     if update_quantity:
    #         self.cart[product_id]['quantity'] += int(quantity)

    #         if self.cart[product_id]['quantity'] == 0:
    #             self.remove(product_id)
                        
    #     self.save()

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            # self.basket[product_id]["qty"] = qty
            self.basket[product_id]["qty"] += int(qty)
        else:
            self.basket[product_id] = {"price": str(product.regular_price), "qty": qty}
        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())
    
        #   if product_id not in self.cart:
        #     self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
        # if update_quantity:
        #     self.cart[product_id]['quantity'] += int(quantity)
        # if self.cart[product_id]['quantity'] == 0:
        #         self.remove(product_id)   

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            # self.basket[product_id]["qty"] = qty
            self.basket[product_id]["qty"] += int(qty)
        self.save()


    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(newprice)
        return total

    def basket_update_delivery(self, deliveryprice=0):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())
        total = subtotal + Decimal(deliveryprice)
        return total

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        del self.session["address"]
        del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True










# class Cart(object):
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)

#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] = {}
        
#         self.cart = cart

#     def __iter__(self):
#         for p in self.cart.keys():
#             self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
#         for item in self.cart.values():
#             item['total_price'] = item['product'].price * item['quantity']

#             yield item
    
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())
    
#     def add(self, product_id, quantity=1, update_quantity=False):
#         product_id = str(product_id)
        
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 1, 'id': product_id}
        
#         if update_quantity:
#             self.cart[product_id]['quantity'] += int(quantity)

#             if self.cart[product_id]['quantity'] == 0:
#                 self.remove(product_id)
                        
#         self.save()
    
#     def remove(self, product_id):
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()

#     def save(self):
#         self.session[settings.CART_SESSION_ID] = self.cart
#         self.session.modified = True
    
#     def clear(self):
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True
    
#     def get_total_cost(self):
#         for p in self.cart.keys():
#             self.cart[str(p)]['product'] = Product.objects.get(pk=p)

#         return sum(item['quantity'] * item['product'].price for item in self.cart.values())