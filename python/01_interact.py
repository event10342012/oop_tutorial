class Phone:
    def __init__(self, brand: str, type_no: str, price: int):
        self.branch = brand
        self.type_no = type_no
        self.price = price

    def call(self, people, message):
        print('Hi', people.name)
        print(message, 'from', self.type_no)


class PhoneStore:
    def __init__(self, name: str, cash: int, income: int = 0):
        self.name = name
        self.income = income
        self.cash = cash

        self.stock = []

    def purchase(self, number: int, phone: Phone):
        for i in range(number):
            self.stock.append(phone)
            self.cash -= phone.price


class People:
    def __init__(self, name: str, age: int, gender: str, balanced: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.balanced = balanced
        self.phone = None

    def buy_phone(self, store: PhoneStore):
        if len(store.stock) > 0:
            phone = store.stock.pop()
            if phone.price < self.balanced:
                self.phone = phone
                self.balanced -= phone.price
            else:
                store.stock.append(phone)
                print('You cannot afford it!!!')
        else:
            print('Sell out!!!')

    def call(self, people, message):
        if self.phone:
            self.phone.call(people, message)
        else:
            print('You do not have a phone')


if __name__ == '__main__':
    leo = People(name='Leo', age=27, gender='m', balanced=100)
    john = People(name='John', age=25, gender='m', balanced=150)

    iphone = Phone(brand='Iphone', type_no='IphoneX', price=150)

    iphone_store = PhoneStore(name='IphoneStore', cash=1000, income=0)
    iphone_store.purchase(5, iphone)

    leo.buy_phone(iphone_store)

    leo.call(john, 'I bought a wonderful phone.')
