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

    elif main_menu_selection == "4":
        print("Resolve Tickets")

    elif main_menu_selection == "5":
        print("Viewing ticket statistics")

    elif main_menu_selection == "6":
        print("Exiting the Program")
        break
    
    else:
        print("ERROR, Please Select an option by number")

