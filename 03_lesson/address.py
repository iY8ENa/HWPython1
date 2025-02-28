# address.py

class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def full_address(self):
        return f"{self.index}, {self.city}, ул. {self.street}, дом {self.house}, кв. {self.apartment}"
