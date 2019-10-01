
class Pizza:
    def __init__(self, initial_price, meat, vege, cheese, others, size, prices):
        self.prices = prices
        self.size = size

        self.initial_price = initial_price
        self.end_price = initial_price

        self.meat = meat
        self.vege = vege
        self.cheese = cheese
        self.others = others

    def swap(self, target_meat, target_vege, target_cheese, target_others):

        for meat in  self.meat:
            self.end_price -= self.prices['meat'][meat]['price_' + self.size]
        for vege in  self.vege:
            self.end_price -= self.prices['vegetables'][vege]['price_' + self.size]
        for cheese in  self.cheese:
            self.end_price -= self.prices['cheese'][cheese]['price_' + self.size]
        for others in  self.others:
            self.end_price -= self.prices['others'][others]['price_' + self.size]

        for meat in  target_meat:
            self.end_price += self.prices['meat'][meat]['price_' + self.size]
        for vege in  target_vege:
            self.end_price += self.prices['vegetables'][vege]['price_' + self.size]
        for cheese in  target_cheese:
            self.end_price += self.prices['cheese'][cheese]['price_' + self.size]
        for others in  target_others:
            self.end_price += self.prices['others'][others]['price_' + self.size]

    def get_final_price(self):
        if self.end_price < self.initial_price:
            return self.initial_price
        return self.end_price



