# create an empty dictionary to store products
shoppingCart = {}

# define a function to add a product to the cart
def add_product():
    if len(shoppingCart) >= 5:
        print("Cart is full")
    else:
        product_name = input("Enter product name: ")
        brand = input("Enter brand name: ")
        shoppingCart[product_name] = brand
        print("Product added to cart.")

# define a function to search for a product in the cart
def search_product():
    product_name = input("Enter product name to search: ")
    if product_name in shoppingCart:
        print(f"Brand of {product_name} is {shoppingCart[product_name]}")
    else:
        print("No product exists with this name")

# define a function to delete a product from the cart
def delete_product():
    if not shoppingCart:
        print("Cart is empty, no item is found")
    else:
        product_name = input("Enter product name to delete: ")
        if product_name in shoppingCart:
            del shoppingCart[product_name]
            print("Product deleted from cart.")
        else:
            print("No product exists with this name")

# define the main function to display the menu and call corresponding functions
def main():
    while True:
        print("\nWELCOME TO THE AMANDO SHOPPING SITE\n")
        print("A. Add product to the cart")
        print("B. Search the product")
        print("C. Delete the product from the cart")
        print("D. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "A":
            add_product()
        elif choice == "B":
            search_product()
        elif choice == "C":
            delete_product()
        elif choice == "D":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

# call the main function to start the program
main()
