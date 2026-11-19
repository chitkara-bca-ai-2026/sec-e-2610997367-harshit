def box(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def lines(title):
    print("\n" + "-" * 50)
    print(f"{title:^50}")
    print("-" * 50)

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

box("INVENTORY MANAGEMENT")


while True:
    print("Choose one:\n1. Add\n2. Remove\n3. View\n4. Sort\n5. Exit")
    choice = input("Input choice (1-5): ")
    if choice == "1":
        product = input("Enter Product Name: ")
        inventory.append(product.title())
    if choice == "2":
        product = input("Enter Product Name: ")
        inventory.remove(product.title())
    if choice == "3":
        for i in inventory:
                    print(i)
    if choice == "4":
        inventory.sort()
    if choice == "5":
        break        



