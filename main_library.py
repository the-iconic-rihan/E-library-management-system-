# Creating a library 
import time
import random
import datetime


class Library:

    def __init__(self, interest_topic, library_name):
        self.interest_list = interest_topic
        self.library_name = library_name
        self.lend_Dict = {}

        # for adding book
        # none means no one has lend this book
        for book in political_books:
            self.lend_Dict[book] = None

        for book in historical_books:
            self.lend_Dict[book] = None

        for book in geographical_book:
            self.lend_Dict[book] = None

        for book in scientific_books:
            self.lend_Dict[book] = None

        for book in engineerings_books:
            self.lend_Dict[book] = None

    # the Return book function which will accept the interest_topic book

    def return_book(self, interest_topics, book, author):
        # verifying the interested topic

        if interest_topics == self.interest_list[0]:
            # seaching for the given book in the topic enterd.

            if book in self.lend_Dict and self.lend_Dict[book] is None:
                print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")

            else:
                self.lend_Dict.popitem()
                political_books.append(book)
                print("Your books has successfully returned")
            # verifying the interested topic

        elif interest_topics == self.interest_list[1]:
            # seaching for the given book in the topic enterd
            if book in self.lend_Dict and self.lend_Dict[book] is None:
                print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")

            else:
                self.lend_Dict.popitem()
                historical_books.append(book)
                print("Your books has successfully returned")

            # verifying the interested topic

        elif interest_topics == self.interest_list[2]:
            # seaching for the given book in the topic enterd
            if book in self.lend_Dict and self.lend_Dict[book] is None:
                print(f"The book name'{book}' is incorrect or the book is not lend by '{author} ")
            else:
                self.lend_Dict.popitem()
                geographical_book.append(book)
                print("Your books has successfully returned")
        # verifying the interested topic

        elif interest_topics == self.interest_list[3]:
            # seaching for the given book in the topic enterd
            if book in self.lend_Dict and self.lend_Dict[book] is None:
                print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")

            else:
                self.lend_Dict.popitem()
                scientific_books.append(book)
                print("Your books has successfully returned")

        # verifying the interested topic
        elif interest_topics == self.interest_list[4]:
            # seaching for the given book in the topic enterd
            if book in self.lend_Dict and self.lend_Dict[book] is None:
                print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")

            else:
                self.lend_Dict.popitem()
                engineerings_books.append(book)
                print("Your books has successfully returned")
        else:
            print("Please, go with the correct interest topic.")

    # Accepting the donation of book from the outsiders function

    def add_book(self, interest_topic, book_name):

        if interest_topic == self.interest_list[0]:
            political_books.append(book_name)
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")

        elif interest_topic == self.interest_list[1]:
            historical_books.append(book_name)
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")

        elif interest_topic == self.interest_list[2]:
            geographical_book.append(book_name)
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")

        elif interest_topic == self.interest_list[3]:
            scientific_books.append(book_name)
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")

        elif interest_topic == self.interest_list[4]:
            engineerings_books.append(book_name)
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")

        else:
            print("Sorry, we can't accept the book.")

    def display_book(self, interest_topic):

        # the below will allow you to choose the interested topic

        if interest_topic == self.interest_list[0]:

            print("Here are the books related to politics: ")
            for index[1], books in enumerate(political_books):
                print(f"{index}]{books}")

        elif interest_topic == self.interest_list[1]:

            print("Here are the books related to history:")
            for index, books in enumerate(historical_books):
                print(f"{index}]{books}")

        elif interest_topic == self.interest_list[2]:
            print("Here are the books related to Geography:")

            for index, books in enumerate(geographical_book):
                print(f"{index}]{books}")

        elif interest_topic == self.interest_list[3]:
            print("Here are the books related to Science:")

            for index, books in enumerate(scientific_books):
                print(f"{index}]{books}")

        elif interest_topic == self.interest_list[4]:

            print("Here are the books related to Engineering:")

            for index, books in enumerate(engineerings_books):
                print(f"{index}]{books}")

        else:
            print("Here is the list of entire books in library.")
            print("Books related to politics")
            for index, books in enumerate(political_books):
                print(f"{index}]{books}")

            print("Books related to History")
            for index, books in enumerate(historical_books):
                print(f"{index}]{books}")

            print("Here are the books related to Science:")
            for index, books in enumerate(scientific_books):
                print(f"{index}]{books}")

            print("Here are the books related to engineering:")
            for index, books in enumerate(engineerings_books):
                print(f"{index}]{books}")

            print("Here are the books related to Geography:")
            for index, books in enumerate(geographical_book):
                print(f"{index}]{books}")

    def lend_book(self, user_interest, reader, book, book_reference):

        # who owns the book if not available

        # Searching the book in Politics section

        if user_interest == self.interest_list[0]:
            if book in self.lend_Dict is not reader and book in political_books:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.lend_Dict[book]
                political_books.remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")

            else:
                print("You Enter the incorrect book. Please go with the correct one!")

        # Searching the book in history section

        elif user_interest == self.interest_list[1]:
            if book in self.lend_Dict is not reader and book in historical_books:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.lend_Dict[book]
                historical_books.remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")

            else:
                print("You Enter the incorrect book. Please go with the correct one!")

        # Searching the book in geography  section

        elif user_interest == self.interest_list[2]:
            if book in self.lend_Dict is not reader and book in geographical_book:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.lend_Dict[book]
                geographical_book.remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")
            else:
                print("You Enter the incorrect book. Please go with the correct one!")

        # Searching the book in science section

        elif user_interest == self.interest_list[3]:
            if book in self.lend_Dict is not reader and book in scientific_books:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.lend_Dict[book]
                scientific_books.remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")
            elif book not in scientific_books:
                print("You Enter the incorrect book. Please go with the correct one!")

        # Searching the book in engineering section

        elif user_interest == self.interest_list[4]:
            if book in self.lend_Dict is not reader and book in engineerings_books:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.lend_Dict[book]
                engineerings_books.remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")
            elif book not in engineerings_books:
                print("You Enter the incorrect book. Please go with the correct one!")

        else:
            print("Please , select the correct intereset topic.")

    # THE delete book funtion
    def _remove_book(self, book_name):
        if book_name in historical_books:
            historical_books.remove(book_name)
            self.lend_Dict.pop(book_name)

        elif book_name in political_books:
            political_books.remove(book_name)
            self.lend_Dict.pop(book_name)

        elif book_name in geographical_book:
            geographical_book.remove(book_name)
            self.lend_Dict.pop(book_name)

        elif book_name in scientific_books:
            scientific_books.remove(book_name)
            self.lend_Dict.pop(book_name)

        elif book_name in engineerings_books:
            engineerings_books.remove(book_name)
            self.lend_Dict.pop(book_name)

        else:
            print(f"{book_name} not found is the library.")


def main():
    interest_topic = ["Politics", "History", "Geography", "Science", "Engineering"]
    libraryname = "Parliament of Library, online, India"

    lib_obj = Library(interest_topic, libraryname)

    secret_key = 4562

    print(f"Welcome to {libraryname}")

    print("\n\t1] Add Book \n\t2] Display Book \n\t3]Lend Book\n\t4] Return Book \n\t5]Admin Cell \n\t6] Exit")
    Exit = False
    while Exit is not True:

        user_input = int(input("Hit Your choice: "))

        # the add book working of function
        if user_input == 1:
            name = str(input("Enter your name : "))
            mobile_no = int(input("Enter your mobile number : "))

            print("Which book do you want to donate?")
            interest_topic = str(input("Enter your interest topic :- "))
            donate_book = str(input("Enter your book name:- "))

            # saving the details of donor.
            with open("donator.txt", "a") as f:
                string = str(" ")
                string += str("\n") + str(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~Donor Details~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                string += str("\n") + str(f"Donor name :- {name}")
                string += str("\n") + str(f"Donor mobile number :- {mobile_no}")
                string += str("\n") + str(f"Interest topic :- {interest_topic}")
                string += str("\n") + str(f"Book name :- {donate_book}")
                string += str("\n") + str(f"Book donated @ :- {datetime.datetime.now()}")

                string += str('\n') + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write(string)
            print("Your details are saved successfully..")

            lib_obj.add_book(interest_topic, donate_book)
            main()

        # the displaybook function working.

        elif user_input == 2:
            # taking input for interested topic

            for index, topic in enumerate(interest_topic):
                print(f"{index}]{topic}")
            interest_topics = str(input("Enter your interested topic : "))
            # Saving th details for students enquire in library
            with open("Enquire_file.txt", "a") as f:
                string = str("")
                string += str("\n\t") + str("~~~~~~~~~~~~Enquiry Details~~~~~~~~~~~~~~")
                string += str("\n") + str(f"Interested topic :- {interest_topics}")
                string += str("\n") + str(f"Enquire @ :- {datetime.datetime.now()}")
                string += str("\n\t") + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write(string)
            print(f"Thank you, for interest in our library.Greeting from {libraryname}")
            lib_obj.display_book(interest_topics)
            main()

        # the function lend function

        elif user_input == 3:
            for index, topic in enumerate(interest_topic):
                print(f"{index}]{topic}")
            interest_topics = str(input("Enter your interested topic : "))
            lib_obj.display_book(interest_topics)
            book_name = (input("Enter the book name from list :- "))
            reader_name = str(input("Enter your name:- "))
            book_reference = random.randint(1, 20)
            # saving the borrower's data
            with open("borrow.txt", "a") as f:
                string = str("")
                string += str("\n\t") + str("~~~~~~~~~~~~Borrowing Details~~~~~~~~~~~~~~")
                string += str("\n\t") + str(f"Borrower's name :- {reader_name}")
                string += str("\n\t") + str(f"Interested Topic :- {interest_topics}")
                string += str("\n\t") + str(f"Book name :- {book_name}")
                string += str("\n\t") + str(f"Book reference id is :- {book_reference}")
                string += str("\n\t") + str(f"Borrowing time :- {datetime.datetime.now()}")
                string += str('\n') + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                f.write(string)
            lib_obj.lend_book(interest_topics, reader_name, book_name,book_reference)

            main()
        # code for return function
        elif user_input == 4:
            for index, topic in enumerate(interest_topic):
                print(f"{index}]{topic}")
            interest_topics = str(input("Enter your interested topic : "))
            print("Which books do you want to return?")
            book_name = str(input("Enter the book name:- "))
            author_name = str(input("Enter your name:- "))

            # Saving the details of borrower
            with open("Return_info.txt", "a") as f:
                string = str("")
                string += str("\n\t") + str("~~~~~~~~~~~~~~Return info~~~~~~~~~~~~~~~~~")
                string += str("\n\t") + str(f"Name of Borrower:- {author_name}")
                string += str("\n\t") + str(f"Name of Book:- {book_name}")
                string += str("\n\t") + str(f"Book Return on :- {datetime.datetime.now()}")
                string += str('\n') + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                f.write(string)
            print("Details saved successfully...")
            lib_obj.return_book(interest_topics, book_name, author_name)

            main()

        elif user_input == 5:
            print("Your are about to enter in administrator cell")
            time.sleep(1)

            author_name = str(input("Enter your username:- "))
            code = int(input("Enter the admin's password :- "))
            print('Verifying your credentials,please wait....')
            time.sleep(2)
            if author_name == "rihan bagwan".lower() and code == secret_key:
                print("\n\t1] Delete Book \n\t2] View return book record and clear"
                      "\n\t3] View Display book record and clear \n\t4]View Donated book records and clear"
                      "\n\t5] View borrowing record and clear \n\t6] Clear deletd book record")
                admin_choice = int(input("Hit your choice: "))
                if admin_choice == 1:
                    for index, topic in enumerate(interest_topic):
                        print(f"{index}]{topic}")
                    interest_topics = str(input("Enter your interested topic : "))
                    lib_obj.display_book(interest_topics)
                    print("Which book you want to delete? : ")
                    book_name = str(input())

                    # saving the details of deleted files
                    with open("deleted_files.txt", "a") as f:
                        string = str("")
                        string += str('\n\t') + str("~~~~~~~~~~~~~~~~~~~~~~~~Recycle bin~~~~~~~~~~~~~~~~~~~~~~~~~")
                        string += str("\n\t") + str(f"Deleted book :- {book_name}")
                        string += str("\n\t") + str(f"Book Deleted @ :- {datetime.datetime.now()}")
                    print("Book deleted successfully!")
                    lib_obj._remove_book(book_name)
                    main()
                elif admin_choice == 2:
                    print("Here is the record of returned books.")
                    __return_files_record()
                    print("Do you want to clear the return record? hit yes/y or no/n : ")
                    admin_clear = input()
                    if admin_clear == "yes".lower() or admin_clear == "y".lower():
                        __return_record_clear()
                        main()
                    else:
                        main()

                elif admin_choice == 3:
                    print("Here is the record of Enquired students.")
                    __display_book_record()
                    print("Do you want to clear the enquiry record? hit yes/y or no/n : ")
                    admin_clear = input()
                    if admin_clear == "yes".lower() or admin_clear == "y".lower():
                        __display_record_clear()
                        main()
                    else:
                        main()

                elif admin_choice == 4:
                    print("Here is the record of donation books.")
                    __add_book_record()
                    print("Do you want to clear the donation record? hit yes/y or no/n : ")
                    admin_clear = input()
                    if admin_clear == "yes".lower() or admin_clear == "y".lower():
                        __addbook_record_clear()
                        main()
                    else:
                        main()

                elif admin_choice == 5:
                    print("Here is the record of borrowed books.")
                    __lend_books_record()
                    print("Do you want to clear the borrowed record? hit yes/y or no/n : ")
                    admin_clear = input()
                    if admin_clear == "yes".lower() or admin_clear == "y".lower():
                        __borrowed_book_record_clear()
                        main()
                    else:
                        main()

                elif admin_choice == 6:
                    print("Here is the record of deleted books.")
                    __deleted_files_record()
                    print("Do you want to clear the deleted book record? hit yes/y or no/n : ")
                    admin_clear = input()
                    if admin_clear == "yes".lower() or admin_clear == "y".lower():
                        __delete_book_record_clear()
                        main()
                    else:
                        main()
                else:
                    print("You hit the wrong choice.")
                    main()

            else:
                print(f"The credentials your entered are incorrect.Somebody tried to entered in admins' cell!!")
                main()
        else:
            exit()


# the data functions for admin
# reading the deleted records by admin
def __deleted_files_record():
    with open("deleted_files.txt", "r") as f:
        print(f.read())
        f.close()


# reading the return_record
def __return_files_record():
    with open("Return_info.txt", "r") as f:
        content = f.read()
        print(content)
        f.close()


# reading the display_book records
def __display_book_record():
    with open("Enquire_file.txt", "r") as f:
        print(f.read())
        f.close()


# reading the donated book record
def __add_book_record():
    with open("donator.txt", "r") as f:
        content = f.read()
        print(content)
        f.close()


# reading the  borrowing records
def __lend_books_record():
    with open("borrow.txt", "r") as f:
        print(f.read())
        f.close()


# funtion working for clearing the records by admin:
# clearing the deletd books record
def __delete_book_record_clear():
    with open("deleted_files.txt", "r+") as f:
        content = f.read()
        f.seek(0)
        for line in content:
            if line == "Here is the record of deleted books.":
                f.write(line)
        f.truncate(0)
        f.close()


# clearing the return record
def __return_record_clear():
    with open("Return_info.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


#     clearing the enquirey record
def __display_record_clear():
    with open("Enquire_file.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


# clearing the donate record
def __addbook_record_clear():
    with open("donator.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


#     clearing the lended books record
def __borrowed_book_record_clear():
    with open("borrow.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


if __name__ == '__main__':
    # by default variables

    political_books = ["Seven Decades Of Independent India: Ideas And Reflections",
                       "When Crime Pays: Money And Muscle In Indian Politics", "24 Akbar Road",
                       "Jobonomics: India’s Employment Crisis And What the Future Holds"]

    historical_books = ["White Mughals", "India a History", "India After Gandhi",
                        " The Great Indian Novel" "Discovery Of India"]

    geographical_book = ["World Geography", "Geography of Population", "Geography of India", "Models in Geography"]

    scientific_books = [" Ideas And Opinions", "The Structure of Scientific Revolutions", "What Evolution Is",
                        "The Selfish Gene"]

    engineerings_books = ["Introduction to Algorithm", "The C Programming Language",
                          "The Art of Computer Programming", "The Computer Networking"]

    password_key = 4562

    main()
