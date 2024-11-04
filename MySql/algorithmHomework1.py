class Bookstore():
    def __init__(self, name, author, year_publish, price):
        self.name = name
        self.author = author
        self.year_publish = year_publish
        self.price = price

    def info(self):
        return f'{self.name} {self.author} {self.year_publish}'    

class Library(Bookstore):
    def __init__(self, name, author, year_publish, price, sale):
        super().__init__(name, author, year_publish, price)
        self.sale = sale

    def info(self):
        self.newPrice = self.price - (self.price * self.sale) // 100
        return f'{super().info()} {self.newPrice}'


l1 = Library('Xamsa', 'Alisher_Navoiy', 2000, 500, 15)
l2 = Library("O'tkan_kunlar", 'Abdulla_Qodiriy', 2001, 100, 10)                
l3 = Library('Sariq_devni_minib', "Xudoyberdi_To'xtaboyev", 2000, 200, 5)                
l4 = Library('Boburnoma', 'Zahiriddin_Bobur', 2005, 300, 25)                
l5 = Library('Koinot', "Mirzo_Ulug'bek", 2006, 400, 17)

lst = [l1, l2, l3, l4, l5]
for i in lst:
    print(i.info())
    