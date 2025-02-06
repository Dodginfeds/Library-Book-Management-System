# -------------------------------
# Library Book Management System
# -------------------------------
# This program allows users to:
# 1. Add new books to the library.
# 2. Display all books currently in the library.
# 3. Search for a book by its title.
# 4. Remove a book from the library.
# 5. Exit the program.
# --------------------------------
# Data is stored in a dictionary where:
# - Authors are keys.
# - Each author has a list of books (title, year).
# --------------------------------

books = {}

# -------------------------------
# Function to Add Books
# -------------------------------
def add_books():
    """
    Allows the user to add multiple books to the library.
    Each book has a title, author, and year published.
    """
    try:
        amount = int(input("How many books would you like to add?: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    for _ in range(amount):
        author = input("Enter the Author's Name: ")
        title = input("Enter the Book Title: ")
        year = input("Enter the Publishing Year: ")

        if author in books:
            books[author].append((title, year))  # Append new book to existing author
        else:
            books[author] = [(title, year)]  # Create new author entry

    print(f"{amount} book(s) added successfully!")

# -------------------------------
# Function to Display All Books
# -------------------------------
def display_books():
    """
    Displays all books stored in the library in a formatted table.
    """
    if not books:
        print("\nNo books found in the library.")
        return

    print("\n----------------------------------------")
    print("| Author          | Book Title      | Year      |")
    print("----------------------------------------")
    for author, book_list in books.items():
        for title, year in book_list:
            print(f"| {author:<15} | {title:<15} | {year:<8} |")
    print("----------------------------------------")

# -------------------------------
# Function to Search for a Book
# -------------------------------
def search_book():
    """
    Searches for books by author name.
    Displays the books if found, otherwise prints a not found message.
    """
    author = input("Enter the Author's Name to Search: ")

    if author in books:
        print(f"\nBooks by {author}:")
        for title, year in books[author]:
            print(f"- {title} ({year})")
    else:
        print("No books found for this author.")

# -------------------------------
# Function to Remove a Book
# -------------------------------
def remove_book():
    """
    Allows the user to remove a book by providing the author's name and title.
    """
    author = input("Enter the Author's Name: ")

    if author not in books:
        print("This author does not exist in the library.")
        return

    print(f"Books by {author}:")
    for index, (title, year) in enumerate(books[author], start=1):
        print(f"{index}. {title} ({year})")

    try:
        book_index = int(input("Enter the book number to remove: ")) - 1
        if 0 <= book_index < len(books[author]):
            removed_book = books[author].pop(book_index)
            print(f"Removed: {removed_book[0]} ({removed_book[1]})")
            if not books[author]:  # If author has no books left, remove the entry
                del books[author]
        else:
            print("Invalid selection!")
    except ValueError:
        print("Please enter a valid number.")

# -------------------------------
# Main Menu Function
# -------------------------------
def main_menu():
    """
    Provides the main menu for user interaction.
    """
    while True:
        print("\nLibrary Book Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Books")
        print("4. Remove Books")
        print("5. Exit")

        try:
            choice = int(input("Pick your option (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            add_books()
        elif choice == 2:
            display_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            print("Thank you for visiting the library! Have a great day :)")
            break
        else:
            print("Invalid Choice. Please select a valid option.")

# -------------------------------
# Program Entry Point
# -------------------------------
if __name__ == "__main__":
    main_menu()
