class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        self.products.append(
            Product(name, price, quantity)
        )

        print("Product added")

    def remove_product(self):
        name = input("Enter product name: ")

        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print("Product removed")
                return

        print("Product not found")

    def view_cart(self):
        if not self.products:
            print("Cart is empty")
            return

        for product in self.products:
            print(
                product.name,
                product.price,
                product.quantity,
                product.total()
            )

    def checkout(self):
        total = 0

        for product in self.products:
            total += product.total()

        print("Total Bill:", total)


cart = ShoppingCart()

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cart.add_product()
    elif choice == "2":
        cart.remove_product()
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        cart.checkout()
    elif choice == "5":
        break
    else:
        print("Invalid choice")