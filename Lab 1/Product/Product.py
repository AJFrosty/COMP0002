class Product:
    def __init__(self, id=0, name='', price=0.0, description='', inStock=False):
        self.__product_id = id
        self.__product_name = name
        self.__product_price = price
        self.__product_description = description
        self.__product_in_stock = inStock
    
    def getProductId(self):
        return self.__product_id
    def getProductName(self):
        return self.__product_name
    def getProductPrice(self):
        return self.__product_price
    def getProductDescription(self):
        return self.__product_description
    def isProductInStock(self):
        return self.__product_in_stock
    
    def setProductId(self, id):
        self.__product_id = id
    def setProductName(self, name):
        self.__product_name = name
    def setProductPrice(self, price):
        self.__product_price = price
    def setProductDescription(self, description):
        self.__product_description = description
    def setProductInStock(self, inStock):
        self.__product_in_stock = inStock
    
    def display_product_info(self):
        print(f"ID: {self.__product_id} \nName: {self.__product_name} \nDescription: {self.__product_description} \nPrice: ${self.__product_price} \nIn Stock: {self.__product_in_stock}")
    
