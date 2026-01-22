import sys

class Library:
    def __init__(self):
        self.books = {}  # book_id -> {title, author, available}
        self.next_id = 1

    def add_book(self, title, author):
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


# --- Non-interactive Demo for Jenkins ---
if __name__ == "__main__":
    library = Library()

    # Example usage with command-line arguments
    # python batch.py add "The Hobbit" "J.R.R. Tolkien"
    # python batch.py display
    # python batch.py borrow 1
    # python batch.py return 1
    # python batch.py search Hobbit
    # python batch.py remove 1

    if len(sys.argv) < 2:
        print("Usage: python batch.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 4:
        library.add_book(sys.argv[2], sys.argv[3])
    elif command == "display":
        library.display_books()
    elif command == "borrow" and len(sys.argv) == 3:
        library.borrow_book(int(sys.argv[2]))
    elif command == "return" and len(sys.argv) == 3:
        library.return_book(int(sys.argv[2]))
    elif command == "search" and len(sys.argv) == 3:
        library.search_books(sys.argv[2])
    elif command == "remove" and len(sys.argv) == 3:
        library.remove_book(int(sys.argv[2]))
    else:
        print("Invalid command or arguments.")
