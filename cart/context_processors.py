from .cart import Cart

# create context processor so our cart can work on all the pages
def cart(request):
    #Return the default data from our cart
    return {'cart': Cart(request)}

