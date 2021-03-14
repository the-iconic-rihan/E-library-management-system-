# Creating a library
import time
import random
import datetime


class Library:
    admin = "rihan"

    # admin_clear_input = str(input())
    # admin_choice = int(input("Enter the admin's choice : "))

    def __init__(self, interest_topic, library_name, author):
        self.interest_list = interest_topic
        self.library_name = library_name
        self.author = author
        self.lend_Dict = {}

        for topic in interested_topic.keys():
            for book in interested_topic.get(topic):
                self.lend_Dict[book] = None
        print(self.lend_Dict)

    # the Return book function which will accept the interest_topic book

    def return_book(self, interest_topic, book, author):
        # verifying the interested topic
        # seaching for the given book in the topic enterd.
        if interest_topic in interested_topic.keys() and self.lend_Dict[book] is not None:
            self.lend_Dict.pop(book)
            interested_topic[interest_topic].append(book)
            print("Your books has successfully returned")
            main()

        else:
            print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")
            print(f"{interest_topic} is not correct. Try again.")
            main()

    # Accepting the donation of book from the outsiders function

    def add_book(self, interest_topic, book_name):
        if interest_topic in interested_topic.keys():
            for topic in interested_topic.keys():
                interested_topic[topic].append(book_name)
                self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")
            print(self.lend_Dict)

        else:
            print("Sorry, we can't accept the book.")

    def display_book(self, interest_topic):

        # the below will allow you to choose the interested topic

        if interest_topic in interested_topic.keys():
            print(f"Here are the books related to {interest_topic}:")
            print(f"{interested_topic.__getitem__(interest_topic)}")
        else:
            print("Topic you entered is incorrect.")
            main()

    def lend_book(self, user_interest, reader, book, book_reference):

        # who owns the book if not available
        # searching the book in interested topics
        if user_interest in interested_topic.keys():
            if book in self.lend_Dict and self.lend_Dict[book] is None:
                # the none means no author has lend this book
                self.lend_Dict[book] = reader
                self.interest_list[user_interest].remove(book)
                print(f"Your book reference id is:- {book_reference}. Please save it for further reference.")
                print("Your details as saved ....Collect your book.")
                print(f"Book lend to {reader}")
            elif book not in self.lend_Dict or self.lend_Dict[book] is not None:
                print(f"No book named {book} is tagged in {user_interest} or {book} is lend by someone else.")

        else:
            print("Please , select the correct intereset topic.")

    # THE delete book funtion
    def _remove_book(self, book):
        for topic in interested_topic.keys():
            if topic in interested_topic.keys() and book in interested_topic[topic]:
                self.lend_Dict.pop(book)
                interested_topic[topic].remove(book)
                print(f"{book} deleted successful!")


def main():
    print(f"Welcome to {libraryname}")

    print("\n\t1] Add Book \n\t2] Display Book \n\t3]Lend Book\n\t4] Return Book \n\t5]Admin Cell \n\t6] Exit")
    Exit = False
    while Exit is not True:

        user_input = int(input("Hit Your choice: "))
        # the adding input
        if user_input == 1:
            add_book_info()
            main()

        # the displaying input
        elif user_input == 2:
            display_book_info()
            main()

        # the borrowing input
        elif user_input == 3:
            lend_book_info()
            main()
        # code for return function
        elif user_input == 4:
            return_book_info()
            main()

        elif user_input == 5:
            admin_cell()
            main()

        else:
            exit()


# files
# the add book function's working

def add_book_info():
    # saving the details of donor.
    name = str(input("Enter your name : "))
    mobile_no = int(input("Enter your mobile number : "))
    print("Which book do you want to donate?")
    interest_topic = str(input("Enter your interest topic :- "))
    donate_book = str(input("Enter your book name:- "))

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


# the display book function working.
def display_book_info():
    # taking input for interested topic
    display_topic()
    interest_topic = str(input("Enter your interested topic : "))
    # Saving th details for students enquire in library
    with open("Enquire_file.txt", "a") as f:
        string = str("")
        string += str("\n\t") + str("~~~~~~~~~~~~Enquiry Details~~~~~~~~~~~~~~")
        string += str("\n") + str(f"Interested topic :- {interest_topic}")
        string += str("\n") + str(f"Enquire @ :- {datetime.datetime.now()}")
        string += str("\n\t") + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        f.write(string)
    print(f"Thank you, for interest in our library.Greeting from {libraryname}")
    lib_obj.display_book(interest_topic)


# the working lend_book function
def lend_book_info():
    display_topic()
    interest_topic = str(input("Enter your interested topic : "))
    lib_obj.display_book(interest_topic)
    book_name = (input("Enter the book name from list :- "))
    reader_name = str(input("Enter your name:- "))
    book_reference = random.randint(1, 20)
    # saving the borrower's data
    with open("borrow.txt", "a") as f:
        string = str("")
        string += str("\n\t") + str("~~~~~~~~~~~~Borrowing Details~~~~~~~~~~~~~~")
        string += str("\n\t") + str(f"Borrower's name :- {reader_name}")
        string += str("\n\t") + str(f"Interested Topic :- {interest_topic}")
        string += str("\n\t") + str(f"Book name :- {book_name}")
        string += str("\n\t") + str(f"Book reference id is :- {book_reference}")
        string += str("\n\t") + str(f"Borrowing time :- {datetime.datetime.now()}")
        string += str('\n') + str("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        f.write(string)
    lib_obj.lend_book(interest_topic, reader_name, book_name, book_reference)


# the working of return book funtion
def return_book_info():
    display_topic()
    interest_topic = str(input("Enter your interested topic : "))
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
    lib_obj.return_book(interest_topic, book_name, author_name)


# the data functions for admin

# working of remove book
def admin_choice_funct():
    admin_choice = int(input("Enter the admins' choice : "))
    return admin_choice


def admin_clear_input_funct():
    admin_clear_input = str(input())
    return admin_clear_input


def admin_cell():
    secret_key = 4562
    print("Your are about to enter in administrator cell")
    time.sleep(1)
    admin_name = str(input("Enter your username:- "))
    code = int(input("Enter the admin's password :- "))
    print('Verifying your credentials,please wait....')
    time.sleep(2)
    if admin_name == lib_obj.admin.lower() and code == secret_key:
        print("\n\t1] Delete Book \n\t2] View return book record and clear"
              "\n\t3] View Display book record and clear \n\t4]View Donated book records and clear"
              "\n\t5] View borrowing record and clear \n\t6] logout admin cell")
        interest_topic = str(input("Enter your interested topic : "))
        lib_obj.display_book(interest_topic)

        clear_view_record_admin(admin_choice_funct())
    else:
        print(f"The credentials your entered are incorrect.Somebody tried to entered in admins' cell!!")
        main()


# displaying topic list
def display_topic():
    for index, topic in enumerate(interested_topic):
        print(f"{index + 1}]{topic}")


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


# function working for clearing the records by admin:
def clear_record_admin(admin_clear_input, admin_choice):
    if admin_clear_input == admin_clear_input_funct().lower() and admin_choice == admin_clear_input_funct():
        __record_clear(admin_choice_funct(), admin_clear_input_funct())
        admin_cell()
    else:
        admin_cell()


# this function work  for saving the record of deleted book
def remove_book_admin():
    print("Which book you want to delete? : ")
    book_name = str(input())

    # saving the details of deleted files
    with open("deleted_files.txt", "a") as f:
        string = str("")
        string += str('\n\t') + str("~~~~~~~~~~~~~~~~~~~~~~~~Recycle bin~~~~~~~~~~~~~~~~~~~~~~~~~")
        string += str("\n\t") + str(f"Deleted book :- {book_name}")
        string += str("\n\t") + str(f"Book Deleted @ :- {datetime.datetime.now()}")
    lib_obj._remove_book(book_name)
    print("Do you want to clear the deleted books record? yes/no or view the record :")
    __record_clear(admin_choice_funct(), admin_clear_input_funct())


# this function work  for clearing the record of returned book

def return_book_admin():
    print("Here is the record of returned books.")
    __return_files_record()
    print("Do you want to clear the return record? hit yes/y or no/n : ")
    __record_clear(admin_choice_funct(), admin_clear_input_funct())


def display_book_admin():
    print("Here is the record of Enquired students.")
    __display_book_record()
    print("Do you want to clear the enquiry record? hit yes/y or no/n : ")
    __record_clear(admin_choice_funct(), admin_clear_input_funct())


def donated_book_admin():
    print("Here is the record of donation books.")
    __add_book_record()
    print("Do you want to clear the donation record? hit yes/y or no/n : ")
    __record_clear(admin_choice_funct(), admin_clear_input_funct())


def lend_book_admin():
    print("Here is the record of borrowed books.")
    __lend_books_record()
    print("Do you want to clear the borrowed record? hit yes/y or no/n : ")
    __record_clear(admin_choice_funct(), admin_clear_input_funct())


# clearing and viewing the records of library

def clear_view_record_admin(admin_choice):
    if admin_choice == 1:
        remove_book_admin()
    elif admin_choice == 2:
        return_book_admin()
    elif admin_choice == 3:
        display_book_admin()
    elif admin_choice == 4:
        donated_book_admin()
    elif admin_choice == 5:
        lend_book_admin()
    else:
        print(f"{admin_choice} is incorrect! Try again.")
        admin_cell()


# working of clearing data
def __record_clear(admin_choice, clear_input):
    if admin_choice == 1 and clear_input == "yes".lower() or "y".lower():
        __deleted_book_record_clear()
    elif admin_choice == 2 and clear_input == "yes".lower() or "y".lower():
        __return_record_clear()
    elif admin_choice == 3 and clear_input == "yes".lower() or "y".lower():
        __display_record_clear()
    elif admin_choice == 4 and clear_input == "yes".lower() or "y".lower():
        __add_book_record_clear()
    elif admin_choice == 5 and clear_input == "yes".lower() or "y".lower():
        __borrowed_book_record_clear()
    else:
        admin_cell()


# clearing the return record
def __deleted_book_record_clear():
    with open("deleted_files.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


def __return_record_clear():
    with open("Return_info.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")

    # clearing the enquiry record


def __display_record_clear():
    with open("Enquire_file.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


# clearing the donate record
def __add_book_record_clear():
    with open("donator.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")

    # clearing the lended books record


def __borrowed_book_record_clear():
    with open("borrow.txt", "r+") as f:
        f.read()
        f.truncate(0)
        f.close()
    print("Details cleared successfully!")


if __name__ == '__main__':
    # by default variables

    libraryname = "Parliament of Library, online, India"
    interested_topic = {"Politics": ["Seven Decades Of Independent India: Ideas And Reflections",
                                     "When Crime Pays: Money And Muscle In Indian Politics", "24 Akbar Road",
                                     "Jobonomics: India’s Employment Crisis And What the Future Holds"],
                        "History": ["White Mughals", "India a History", "India After Gandhi",
                                    " The Great Indian Novel", "Discovery Of India"],
                        "Geography": ["World Geography", "Geography of Population", "Geography of India",
                                      "Models in Geography"],
                        "Science": [" Ideas And Opinions", "The Structure of Scientific Revolutions",
                                    "What Evolution Is",
                                    "The Selfish Gene"],
                        "Engineering": ["Introduction to Algorithm", "The C Programming Language",
                                        "The Art of Computer Programming", "The Computer Networking"]}
    lib_obj = Library(interested_topic, libraryname, str(input("Enter your name")))

    main()
