a = {} # cart
option = 0
print("WELCOME TO THE AMANDO SHOPPING SITE ")
print("1. insert a product")
print("2. search for a product")
print("3. delete a product")
print("4. Select 4 to quit")

while option != 4:
    option = int(input("Enter your option: "))
    #adding 
    if option == 1:
        user_input = int(input("Enter number of products would you like to insert "))

        v = 0
        while v < user_input:
            lll = len(a)
            if lll < 5:
                c = input("Enter product name: ")
                d = input("Enter company: ")
                a.update({c: d})
                print("Product inserted successfully")
            else:
                print("Inventory is full")
            v += 1
 #searching
    elif option == 2:
        m = input("Enter product name: ")
        if m in a:
            print(m + ":" + a[m])
        else:
            print("Not found")
  #deleting
    elif option == 3:
        k = input("Enter product name: ")
        if k in a:
            a.pop(k)
            print("Product deleted")
        else:
            print("Not found")
 #quiting
    elif option == 4:
        print("Thank you")

    else:
        print("invalid option" )

    print(a)