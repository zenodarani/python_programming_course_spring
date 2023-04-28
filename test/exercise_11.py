
class Item:

    def __init__(self, name, desc, code, price):
        self.name = name
        self.desc = desc
        self.code = code
        self.price = price


class ShoppingBasket:

    def __init__(self):
        self.items = list()

    def add_item(self, item):
        self.items.append(item)

    def rem_item(self, item):
        self.items.remove(item)

    def __len__(self):
        return len(self.items)

    def num_items(self):
        return len(self)

    def total(self):
        tot = 0
        for item in self.items:
            tot += item.price
        return tot
