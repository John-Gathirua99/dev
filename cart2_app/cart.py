from store.models import Product
class Cart():
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart =self.session['session_key']={}


        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty= str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]={'price':str(product.price)}
            self.cart[product_id]=int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)
    

    def get_products(self):
        product_ids = self.cart.keys()# getting id"s frm cart

        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantities(self):
        quantities= self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id=str(product)
        product_quantity=int(quantity)

        my_cart=self.cart
        #update the cart

        my_cart[product_id] = product_quantity
        self.session.modified =True
        tt = self.cart
        return tt
    
    def delete(self,product):
        product_id=str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

