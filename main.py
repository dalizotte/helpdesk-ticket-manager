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
            new_ticket = {
                "issue": clean_issue,
                "status": "Open"
            }
            tickets.append(new_ticket)
            print("Your ticket has been created and added to our tickets list.")
            break


# Function for option 2 (open tickets)

def open_tickets():
    counter = 0
    print("====List Of Tickets====")
    for ticket in tickets:
        counter += 1
        print(f'{counter}. Issue: {ticket["issue"]} | Status: {ticket["status"]}')
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
                ticket = tickets[get_ticket]
                print("=====Ticket Found!=====")
                print(f'Ticket Number: {search_query}')
                print(f' Issue: {ticket["issue"]}')
                print(f' Status: {ticket["status"]}')
                break

# Functon for Option 4 Resolve Ticket.

def resolve_ticket():
    while True:
        if len(tickets) == 0:
            print("There are no tickets avalible right now.")
            print("Sending back to main menu...")
            break
        else:
            try:
                ticket_resolve_num = int(input("What ticket number would you like to resolve?"))
            except ValueError:
                print("Please enter the number for your ticket search")
                continue
            ticket_resolve_num_index = ticket_resolve_num - 1            
            if ticket_resolve_num_index < 0:
                print("That ticket number is too low, please search again")
            elif ticket_resolve_num_index >= len(tickets):
                print("That ticket hasn't been created, please try a lower ticket number")
            else:
                ticket = tickets[ticket_resolve_num_index]
                print(f'Ticket Number: {ticket_resolve_num}')
                print(f' Issue: {ticket["issue"]}')
                print(f' Status: {ticket["status"]}')
                if ticket["status"] == "Resolved":
                    print("This ticket has already been resolved")
                    return
                else:
                    while True:
                        resolve_ticket_question = input("Would you like to resolve this ticket? y/n: ")
                        clean_resolve_ticket_question = resolve_ticket_question.strip().lower()
                        if clean_resolve_ticket_question == "yes" or clean_resolve_ticket_question == "y":
                            ticket["status"] = "Resolved"
                            print(f' Ticket Number {ticket_resolve_num} has been resolved')
                            return
                        elif clean_resolve_ticket_question == "no" or clean_resolve_ticket_question == "n":
                            print(f' Ticket Number {ticket_resolve_num} has not changed.')
                            return
                        else:
                            print(f'I am sorry I did not get that please enter a valid answer for ticket number {ticket_resolve_num} and try again')

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
        resolve_ticket()

    elif main_menu_selection == "5":
        print("Viewing ticket statistics")

    elif main_menu_selection == "6":
        print("Exiting the Program")
        break
    
    else:
        print("ERROR, Please Select an option by number")

