from Product import Product

myProduct = Product(-1,"Tikcets", 70.0,"Olivia Rodrigo GUTS Last Row Tickets!",False)
#Print Current Product Info:
print("Current Product Info:")
myProduct.display_product_info()

#The Shop Owner made some errors and will now correct it and check to see if it worked!:
print("\n------------------------------------------------------------------------------\nNew Information:")
myProduct.setProductId(1)
print(myProduct.getProductId())
myProduct.setProductName("Concert Tickets")
print(myProduct.getProductName())
myProduct.setProductPrice(90.80)
print(myProduct.getProductPrice())
myProduct.setProductDescription("Olivia Rodrigo GUTS Front Row Tickets!")
print(myProduct.getProductDescription())
myProduct.setProductInStock(True)
print(myProduct.isProductInStock())
myProduct.isProductInStock()

#Final Print Statement
print("\n---------------------------------------------------------------------------")
myProduct.display_product_info()

