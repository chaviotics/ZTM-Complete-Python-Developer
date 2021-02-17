#import utility
from utility import * # multiply, divide; the star imports everything
# import shopping.more_shopping.shopping_cart2
#from shopping.more_shopping.shopping_cart2  import buy2

# from package import function

# OR

# from package import entire_module
from shopping.more_shopping import shopping_cart2 # better to use this to prevent name collisions

print(shopping_cart2.buy2('mango')) # this is better

# print(shopping.more_shopping.shopping_cart2.buy2('apple'))
# print(buy2('orange'))

print(divide(1,2))