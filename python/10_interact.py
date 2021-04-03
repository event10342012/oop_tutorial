class Product:
    def __init__(self, brand: str, type_no: str, price: int):
        self.brand = brand
        self.type_no = type_no
        self.price = price

    def call(self, people, message):
        print('Hi', people.name)
        print(message, 'from', self.type_no)


class Store:
    def __init__(self, name: str, cash: int, income: int = 0):
        self.name = name
        self.income = income
        self.cash = cash

        self.stock = []

    def purchase(self, number: int, product: Product):
        for i in range(number):
            self.stock.append(product)
            self.cash -= product.price
            print(f'Purchase {product.brand}-{product.type_no}')
        print(f'This is {self.cash} left.')


class People:
    def __init__(self, name: str, age: int, gender: str, cash: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.cash = cash
        self.phone = None

    def buy(self, store: Store):
        if len(store.stock) > 0:
            phone = store.stock.pop()
            if phone.price <= self.cash:
                self.phone = phone
                self.cash -= phone.price
            else:
                store.stock.append(phone)
                print('You cannot afford it!!!')
        else:
            print('sold out!!!')

    def call(self, people, message):
        if self.phone:
            self.phone.call(people, message)
        else:
            print('You do not have a phone')


if __name__ == '__main__':
    # assume store sell only one product in this world

    leo = People(name='Leo', age=27, gender='m', cash=150)
    john = People(name='John', age=25, gender='m', cash=150)

    iphone = Product(brand='Iphone', type_no='IphoneX', price=150)

    iphone_store = Store(name='IphoneStore', cash=1000, income=0)
    iphone_store.purchase(5, iphone)

    leo.buy(iphone_store)

    leo.call(john, 'I bought a wonderful phone.')
