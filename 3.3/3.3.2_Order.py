class Order:

    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __add__(self, product: str) -> 'Order':
        return Order(self.cart + [product], self.customer)

    def __radd__(self, product: str) -> 'Order':
        return Order([product] + self.cart, self.customer)

    def __sub__(self, product: str) -> 'Order':
        new_cart = self.cart.copy()
        if product in new_cart:
            new_cart.remove(product)
        return Order(new_cart, self.customer)

    def __rsub__(self, product: str) -> 'Order':
        return self - product


if __name__ == '__main__':
    order = Order(['banana', 'apple'], 'Гена Букин')

    order_2 = order + 'orange'
    assert order.cart == ['banana', 'apple']
    assert order.customer == 'Гена Букин'
    assert order_2.cart == ['banana', 'apple', 'orange']

    order = 'mango' + order
    assert order.cart == ['mango', 'banana', 'apple']
    order = 'ice cream' + order
    assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

    order = order - 'banana'
    assert order.cart == ['ice cream', 'mango', 'apple']

    order3 = order - 'banana'
    assert order3.cart == ['ice cream', 'mango', 'apple']

    order = order - 'mango'
    assert order.cart == ['ice cream', 'apple']
    order = 'lime' - order
    assert order.cart == ['ice cream', 'apple']
    print('Good')
