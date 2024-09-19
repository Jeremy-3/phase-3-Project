from helpers import(
    exit_program,
    list_authors,
    find_author_by_id,
    find_author_by_name,
    find_author_by_genre,
    create_new_author,
    update_author,
    delete_author,
    list_books,
    find_book_by_id,
    find_book_by_title,
    find_book_by_year_published,
    create_new_book,
    update_book,
    delete_book
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_authors()
        elif choice == "2":
            find_author_by_id()
        elif choice == "3":
            find_author_by_name()
        elif choice == "4":
            find_author_by_genre()
        elif choice == "5":
            create_new_author()
        elif choice == "6":
            update_author()
        elif choice == "7":
            delete_author()
        elif choice == "8":
            list_books()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            find_book_by_title()
        elif choice == "11":
            find_book_by_year_published()
        elif choice == "12":
            create_new_book()
        elif choice == "13":
            update_book()
        elif choice == "14":
            delete_book()  
        else:
            print("Invalid Choice please select again")    
        
        

def menu():
    print("Welcome To The Online BookStore 🎉 ")
    print("Please select the options below 👇") 
    print("0. Exit the program")
    print("1. List all the authors")
    print("2. Find author by id")
    print("3. Find author by name")
    print("4. Find author by the genre written")
    print("5. Add a new author")
    print("6. Update author")
    print("7.❗Delete Author❗")
    print("8. list all the books")
    print("9. Find book by id")
    print("10. Find book by title")
    print("11. Find book by the year it was published")
    print("12. Add a new book")
    print("13. Update book") 
    print("14.❗Delete Book❗")                                                               


if __name__ == "__main__":
    main()   
    