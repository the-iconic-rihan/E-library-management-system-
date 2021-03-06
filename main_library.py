# Creating a library
import time
import random
import datetime


class Library:

    def __init__(self, interest_topic, library_name):
        self.interest_list = interest_topic
        self.library_name = library_name
        self.lend_Dict = {}
        self.donated_dict = {}

        # for adding book
        # none means no one has lend this book
        for topic in interested_topic.keys():
            for book in interested_topic.get(topic):
                self.lend_Dict[book] = None

    # the Return book function which will accept the interest_topic book

    def return_book(self, interest_topic, book, author):
        # verifying the interested topic
        # seaching for the given book in the topic enterd.
        try:
            if interest_topic in interested_topic.keys() and self.lend_Dict[book] is not None:
                self.lend_Dict.pop(book)
                interested_topic[interest_topic].append(book)

            else:
                print(f"The'{book}' book name is incorrect or the book is not lend by '{author} ")

        except NameError:
            print(f"{interest_topic} is not correct. Try again.")

        finally:
            print("Your books has successfully returned")
            main()

    # Accepting the donation of book from the outsiders function

    def add_book(self, interest_topic, book_name):

        if interest_topic in interested_topic.keys():
            self.donated_dict.update({interest_topic: book_name})
            self.lend_Dict[book_name] = None
            print(f"{book_name} added successfully")
        else:
            print("Sorry, we can't accept the book.")

    def display_book(self, interest_topic):

        # the below will allow you to choose the interested topic
        try:
            if interest_topic in interested_topic.keys() and self.donated_dict.keys():
                print(f"Here are the books related to {interest_topic}:")
                print(f"{interested_topic.__getitem__(interest_topic)}")
                print(f"{self.donated_dict[interest_topic]} is EXTRA BOOK")
            else:
                print(f"Here are the books related to {interest_topic}")
                print(f"{interested_topic.__getitem__(interest_topic)}")

        except KeyboardInterrupt:
            print("Topic you entered is incorrect.")
            main()

    def lend_book(self, user_interest, reader, book, book_reference):

        # who owns the book if not available
        # searching the book in interested topics
        if user_interest in interested_topic.keys() or self.donated_dict.keys():
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
        try:
            for topic in interested_topic.keys():
                if topic in interested_topic.keys() and book in interested_topic[topic]:
                    self.lend_Dict.pop(book)
                    interested_topic[topic].remove(book)
                    print(f"{book} deleted successfull!")

                else:
                    print(f"{topic} is incorrect or {book} is not tagged in topic {topic}! ")
                    remove_book_info()
        except NameError:
            print("Topic entered is incorrect")
            remove_book_info()
        finally:
            main()


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
            remove_book_info()
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
def remove_book_info():
    print("Your are about to enter in administrator cell")
    time.sleep(1)
    author_name = str(input("Enter your username:- "))
    code = int(input("Enter the admin's password :- "))
    print('Verifying your credentials,please wait....')
    time.sleep(2)
    if author_name == "rb".lower() and code == secret_key:
        print("\n\t1] Delete Book \n\t2] View return book record and clear"
              "\n\t3] View Display book record and clear \n\t4]View Donated book records and clear"
              "\n\t5] View borrowing record and clear \n\t6] Clear deleted book record")
        admin_choice = int(input("Hit your choice: "))
        if admin_choice == 1:

            interest_topic = str(input("Enter your interested topic : "))
            lib_obj.display_book(interest_topic)
            print("Which book you want to delete? : ")
            book_name = str(input())

            # saving the details of deleted files
            with open("deleted_files.txt", "a") as f:
                string = str("")
                string += str('\n\t') + str("~~~~~~~~~~~~~~~~~~~~~~~~Recycle bin~~~~~~~~~~~~~~~~~~~~~~~~~")
                string += str("\n\t") + str(f"Deleted book :- {book_name}")
                string += str("\n\t") + str(f"Book Deleted @ :- {datetime.datetime.now()}")
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


#     clearing the enquiry record
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
    secret_key = 4562

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
    lib_obj = Library(interested_topic, libraryname)


    password_key = 4562

    main()
