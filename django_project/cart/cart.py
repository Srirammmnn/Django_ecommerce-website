
from django_app.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] =int(product_qty)

        self.session.modified = True

    def __len__(self):
        return sum(self.cart.values())  # Total quantity, not just # of items

    def get_prods(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.cart

    def update(self, product, quantity):
        product_id = str(product)
        quantity = int(quantity)

        if product_id in self.cart:
            self.cart[product_id] = quantity
            self.session.modified = True

        return self.cart

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def delete(self,product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified =True

    def cart_total(self):
        
    
        # Get product IDS

        product_ids = self.cart.keys()

        # lookup those keys in our products database model

        products = Product.objects.filter(id__in=product_ids)

        # Get quantities, {'4':3}

        quantities = self.cart

        # Start counting at 0

        total = 0

       

        for key, value in quantities.items():

            # Convert key string into into so we can do math

            key = int(key) #convert string to a int

            for product in products:

                if product.id == key:

                    if product.is_sale:

                        total = total + (product.sale_price * value)

                    else:

                        total = total + (product.price * value)
        return total 

        
