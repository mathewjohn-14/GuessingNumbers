class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f"'{title}' already exists in the library.")
        else:
            self.books[title] = {"author": author, "available": True}
            print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("\nAvailable Books:")
            for title, info in self.books.items():
                status = "Available" if info["available"] else "Borrowed"
                print(f"- {title} by {info['author']} ({status})")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]["available"]:
                self.books[title]["available"] = False
                print(f"You borrowed '{title}'. Enjoy reading!")
            else:
                print(f"Sorry, '{title}' is already borrowed.")
        else:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]["available"]:
                self.books[title]["available"] = True
                print(f"Thank you for returning '{title}'.")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' not found in the library.")


# --- Demo ---
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
