#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a menu driven program that shows the working of a library. The menu option should be:
# ADD BOOK INFORMATION
# DISPLAY BOOK INFORMATION
# LIST ALL BOOKS OF GIVEN AUTHOR 
# LIST THE COUNT OF BOOKS IN THE LIBRARY
# EXIT

#function to display the menu of the Library
def displayMenu() :
    print ("\n1. ADD BOOK INFORMATION")
    print("2. DISPLAY BOOK INFORMATION")
    print("3. LIST ALL BOOKS OF GIVEN AUTHOR")
    print("4. LIST THE COUNT OF BOOKS IN LIBRARY")
    print("5. EXIT\n")

#function to check whether the input within the chosen menu 1:5
def inputCheck (string) :
    temp = str(string)
    if (temp.isnumeric()) :
        if ( int(temp) >= 1 and int(temp) <=5 ) :
            return True
    else :
        return False

#Adding some initial data in the Library
books_title = ["Python from the Very Beginning","Python One-Liners"]
books_author = ["J. Whitington","Christian Mayer"]
books_publisher = ["Coherent Press","No Starch Press"]

choice = "y"
books_count = len(books_title)
while (choice == "y") :
    displayMenu();
    menu_choice = (input("Enter your choice from the above (1:5)"))
    if (inputCheck(menu_choice)):
        menu_choice = int(menu_choice)
        if (menu_choice == 1) :
            new_book_title = input("\nEnter the book title")
            books_title.append(new_book_title)
            new_book_author = input("\nEnter the book author")
            books_author.append(new_book_author)
            new_book_publisher = input("\nEnter the book publisher")
            books_publisher.append(new_book_publisher)
            print("Book added succesfully!\n")
            choice = input("Do you still want to continue (y/n)")
        elif (menu_choice == 2) :
            print("******** LIST OF BOOKS *******\n")
            for i in range(len(books_title)) :
                print(f'Book Name : {books_title[i]}\n')
                print(f'Book Author : {books_author[i]}\n')
                print(f'Book Publisher : {books_publisher[i]}\n')
                print('*******************************\n')
            choice = input("Do you still want to continue (y/n)")
        elif (menu_choice == 3) :
            print("******** LIST OF AUTHORS *******\n")
            for j in range(len(books_author)) :
                print(f"{books_author[j]}\n")
            choice_author = input ("Enter the author name from the above list\n")
            author_index =[]
            for k in range(len(books_author)) :
                if ( books_author[k] == choice_author ) :
                    print(f'Book Name : {books_title[k]}\n')
                    print(f'Book Author : {books_author[k]}\n')
                    print(f'Book Publisher : {books_publisher[k]}\n')
                    author_index.append(books_author[k])
            if (len(author_index) == 0) :
                    print(f" No books found for the author : {choice_author}")
            choice = input("Do you still want to continue (y/n)")
        elif (menu_choice == 4) :
            books_count = len (books_title)
            print(f"Number of the books in the library: {books_count}")
            choice = input("Do you still want to continue (y/n)")
        elif (menu_choice == 5) :
            print("Bye Bye!")
            break;
    else :
        print('Please enter valid input')
        choice = "y"


# In[ ]:




