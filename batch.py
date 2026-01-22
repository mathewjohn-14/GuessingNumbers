class Library:
    def __init__(self):
        self.books = {}  # book_id -> {title, author, available}
        self.next_id = 1

    def add_book(self, title, author):
        # Check if book already exists by title and author
        for book in self.books.values():
            if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
                print(f"'{title}' by {author} already exists in the library.")
                return
        self.books[self.next_id] = {"title": title, "author": author, "available": True}
        print(f"Book '{title}' added successfully with ID {self.next_id}!")
        self.next_id += 1

    def display_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("\n--- Library Collection ---")
            for book_id, info in self.books.items():
                status = "Available" if info["available"] else "Borrowed"
                print(f"ID: {book_id} | {info['title']} by {info['author']} ({status})")

    def borrow_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["available"]:
                self.books[book_id]["available"] = False
                print(f"You borrowed '{self.books[book_id]['title']}'. Enjoy reading!")
            else:
                print(f"Sorry, '{self.books[book_id]['title']}' is already borrowed.")
        else:
            print(f"Book ID {book_id} not found in the library.")

    def return_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]["available"]:
                self.books[book_id]["available"] = True
                print(f"Thank you for returning '{self.books[book_id]['title']}'.")
            else:
                print(f"'{self.books[book_id]['title']}' was not borrowed.")
        else:
            print(f"Book ID {book_id} not found in the library.")

    def search_books(self, keyword):
        results = [info for info in self.books.values() if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower()]
        if results:
            print("\n--- Search Results ---")
            for info in results:
                status = "Available" if info["available"] else "Borrowed"
                print(f"- {info['title']} by {info['author']} ({status})")
        else:
            print(f"No books found matching '{keyword}'.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed['title']}' removed from the library.")
        else:
            print(f"Book ID {book_id} not found in the library.")


# --- Demo ---
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Remove Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        try:
            book_id = int(input("Enter book ID to borrow: "))
            library.borrow_book(book_id)
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
    elif choice == "4":
        try:
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
    elif choice == "5":
        keyword = input("Enter keyword (title/author): ")
        library.search_books(keyword)
    elif choice == "6":
        try:
            book_id = int(input("Enter book ID to remove: "))
            library.remove_book(book_id)
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")
    elif choice == "7":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
