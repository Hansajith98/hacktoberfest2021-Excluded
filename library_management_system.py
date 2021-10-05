class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("lender-book database has been updated.you can take the book.")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookslist.append(book)
        print("book has been updated to the booklist.")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == "__main__":
    v1 = Library(['Python', 'C++', 'Java', 'DSA', 'HTMl'],'Code')

    while (True):
        print("WELCOME TO THE LIBRARY.ENTER YOUR CHOICE:")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        print("5. Exit ")

        user_choice = int(input("enter your choice:"))
        if user_choice not in [1, 2, 3, 4, 5]:
            print("Enter a valid option")
            continue

        if user_choice == 1:
            v1.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want:")
            user = input("Enter your name:")
            v1.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the book you want to add:")
            v1.addBook(book)

        elif user_choice == 4:
            book = input("Enter the book you want to return:")
            v1.returnBook(book)

        elif user_choice == 5:
            exit()

        else:
            print("Not a valid option")

        print("Press 'q' to quit and 'c' to continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
