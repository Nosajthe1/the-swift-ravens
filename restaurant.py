class Table:
    def __init__(self, guests_per_table):
        self.bill = []
        self.subtotal = 0.00
        self.guests_per_table = guests_per_table
        self.total_price = 0.00


    def order(self, item, price, quantity=1):
        order_list = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(order_list)
        return self.bill

    def remove(self, item, price, quantity):
        if self.bill[0]['item'] == '' and self.bill[0]['price'] == 0:
            return False
        old_quantity = self.bill[0]['quantity']
        new_quantity = old_quantity - quantity
        self.bill[0]['quantity'] = new_quantity
        return self.bill

    def get_subtotal(self):
        for num in self.bill:
            self.subtotal += num['price'] * num['quantity']
        print(self.subtotal)
        return self.subtotal

    def get_total(self, discount):
        discount_price = self.subtotal * discount
        self.total_price = self.subtotal + discount_price
        print({'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': self.total_price})
        return {'Sub Total': self.subtotal, 'Service Charge': discount_price, 'Total': self.total_price}

    def split_bill(self):
        bill_split = self.total_price / self.guests_per_table
        print(bill_split)
        return bill_split


tab = Table(2)
tab1 = Table(3)
tab.order('Food', 10.00, 5)
tab.order('Food2', 5.00, 1)
# print(tab.bill)
print(tab.get_subtotal())
print(tab.get_total(0.15))
print(tab.split_bill())
