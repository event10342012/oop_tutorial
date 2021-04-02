class Phone:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price


if __name__ == '__main__':
    phone = Phone(brand='IPhone', color='r', price=100)
    print(phone.brand)
    print(phone.color)
    print(phone.price)
