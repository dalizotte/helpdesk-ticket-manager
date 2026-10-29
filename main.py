#IT Help desk tracker, this will be the main menu for the help desk it will contain: 
#1. Create New Ticket
#2. View All Tickets
#3. Search Tickets
#4. Resolve a Ticket
#5. View Ticket Statistics
#6. Exit

# Title
# Display for the Main Menu for our program

def display_menu():
    print("""===================
IT Help Desk Ticket Manager
===================""")
    print("""    1. Create New Ticket
    2. View All Tickets
    3. Search Tickets
    4. Resolve a Ticket
    5. View Ticket Statistics
    6. Exit""")

    print("===================")


# List of all tickets

tickets = []


# Ticket Management Funcitons

# Function for option 1 (create ticket)
def create_ticket():
    while True:
        issue = input("Please describe your issue: ")
        clean_issue = issue.strip()
        if clean_issue == "":
            print("Whoops we didnt get that")
        else:
            tickets.append(clean_issue)
            print("Your ticket has been created and added to our tickets list.")
            break

# Function for option 2 (open tickets)

def open_tickets():
    counter = 0
    print("====List Of Tickets====")
    for ticket in tickets:
        counter += 1
        print(counter,"...", ticket)
    if len(tickets) == 0:
        print("No tickets have been created yet.")


# Fuction for option 3 (search tickets)

def search_ticket():
    while True:
        if len(tickets) == 0:
            print("There are no tickets avalible right now.")
            print("Sending back to main menu...")
            break
        else:
            try:
                search_query = int(input("Please search for the number of ticket youre trying to find: "))
            except ValueError:
                print("Please enter the number for your ticket search")
                continue
            get_ticket = search_query - 1
            if get_ticket < 0:
                print("That ticket number is too low, please search again")
            elif get_ticket >= len(tickets):
                print("That ticket hasn't been created, please try a lower ticket number")
            else:
                print("here is your ticket", tickets[get_ticket])
                break

# Main Menu Selection Process

while True:
    display_menu()
    main_menu_selection = input("Please Select an option:")

    if main_menu_selection == "1":
        print("Opening a new ticket for creation...")
        create_ticket()
        
    elif main_menu_selection == "2":
        print("Opening all tickets...")
        open_tickets()

    elif main_menu_selection == "3":
        print("Searching Tickets...")
        search_ticket()

    elif main_menu_selection == "4":
        print("Resolve Tickets")

    elif main_menu_selection == "5":
        print("Viewing ticket statistics")

    elif main_menu_selection == "6":
        print("Exiting the Program")
        break
    
    else:
        print("ERROR, Please Select an option by number")

