"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    new_todo_item = raw_input("Add new item: > ")
    my_list.append(new_todo_item)
    return my_list


def view_list(my_list):
    """Print each item in the list."""
    for items in my_list:
        print items




def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """Would you like to
    A. Add a new item
    B. View list
    C. Quit the program
    >>> """
   

    while True:
        answer = raw_input(user_options)
        # Collect input and include your if/elif/else statements here.
        if answer == "A":
            add_to_list(my_list)  
        elif answer == "B":
            view_list(my_list)
        elif answer == "C":
            break

#-------------------------------------------------

my_list = []
display_main_menu(my_list)
