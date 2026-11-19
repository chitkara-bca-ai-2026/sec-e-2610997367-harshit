books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]

library_categories = {book[3] for book in books}
student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity",
}


def show_menu():
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")
        if not books:
            print("No books are currently cataloged.")
        else:
            for number, (title, author, year, category) in enumerate(books, start=1):
                print(
                    f'{number}. "{title}" by {author} ({year}) '
                    f"| Genre: {category}"
                )
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if not title or not author or not year or not category:
            print("[ERROR] All fields are required. Book was not added.")
            continue

        book = (title, author, year, category)
        books.append(book)

        library_categories.add(category)

        print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
        print(f'[INFO] Category set updated with: "{category}"')

    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")
        if library_categories:
            for category in sorted(library_categories, key=str.casefold):
                print(f"- {category}")
        else:
            print("No categories are currently in the library.")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print("\n--- Add Category to Student Wishlist ---")
        category = input("Enter requested category/genre: ").strip()

        if not category:
            print("[ERROR] Category cannot be empty.")
        elif category in student_wishlist:
            print(f'[INFO] "{category}" is already on the student wishlist.')
        else:
            student_wishlist.add(category)
            print(f'[SUCCESS] "{category}" added to the student wishlist.')

    elif choice == "5":
        print("\n--- Category Gap Analysis ---")

        intersection = student_wishlist & library_categories

        difference = student_wishlist - library_categories

        union = student_wishlist | library_categories

        print(f"Library categories: {sorted(library_categories)}")
        print(f"Student wishlist:  {sorted(student_wishlist)}")

        print(f"\nIntersection (requested and available): {sorted(intersection)}")
        print(f"Difference (requested but unavailable):  {sorted(difference)}")
        print(f"Union (all categories):                 {sorted(union)}")

    elif choice == "6":
        print("Exiting Library Book & Category Manager.")
        break

    else:
        print("[ERROR] Invalid choice. Enter a number from 1 to 6.")