class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def purchase(self, amount):
        if amount <= self.__stock:
            self.__stock -= amount
            print(f"{amount} dona {self.name} sotildi. Qolgan zaxira: {self.__stock}")
        else:
            print(f"{self.name} mahsuloti sotuvda yo‘q yoki zaxira yetarli emas!")

    def get_stock(self):
        return self.__stock


class InventoryManager:
    def update_stock(self, product, new_stock):
        product._Product__stock = new_stock  
        print(f"{product.name} uchun yangi zaxira miqdori: {new_stock}")

prod = Product("Telefon", 3000, 10)
manager = InventoryManager()

prod.purchase(3)
manager.update_stock(prod, 15)
prod.purchase(5)
prod.purchase(20) 
