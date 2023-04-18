class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product_name, brand):
        if len(self.cart) >= 5:
            print("Cart is full")
        else:
            self.cart[product_name] = brand
            print(f"{product_name} added to the cart")

    def search_product(self, product_name):
        if product_name in self.cart:
            print(f"{product_name} - {self.cart[product_name]}")
        else:
            print("No product exists with this name")

    def delete_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"{product_name} deleted from the cart")
            if not self.cart:
                print("Cart is empty, no item is found")
        else:
            print("No product exists with this name")

    def display_menu(self):
        print("WELCOME TO THE AMANDO SHOPPING SITE\n")
        print("A. Add product to the cart.")
        print("B. Search the product.")
        print("C. Delete the product from the cart.")
        print("D. Quit.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == 'A':
                product_name = input("Enter the product name: ")
                brand = input("Enter the brand name: ")
                self.add_product(product_name, brand)
            elif choice == 'B':
                product_name = input("Enter the product name: ")
                self.search_product(product_name)
            elif choice == 'C':
                product_name = input("Enter the product name: ")
                self.delete_product(product_name)
            elif choice == 'D':
                break
            else:
                print("Invalid choice")


shopping_cart = ShoppingCart()
shopping_cart.run()
