
# IT Help Desk Ticket Manager

A Python command-line application that simulates basic IT help desk operations, allowing users to create, view, search, resolve, and track technical support tickets.

This project was developed as a hands-on introduction to Python programming and software development, with an emphasis on building practical tools relevant to IT support and technical operations.

## Project Status

**Current Version:** V0.4  
**Status:** Active Development  
**Next Milestone:** V0.5 — Persistent Storage Using JSON

The core ticket-management functionality is complete. Persistent storage and final testing are planned for the first stable release, V1.0.

## Features

### Create Support Tickets
- Create tickets with user-provided issue descriptions.
- Validate input to prevent empty or whitespace-only tickets.
- Automatically assign new tickets an "Open" status.

### View and Search Tickets
- Display all tickets in a numbered list.
- View issue descriptions and ticket statuses.
- Search for individual tickets by their displayed numbers.
- Handle invalid input and nonexistent ticket numbers.
- Display appropriate messages when no tickets exist.

### Resolve Support Tickets
- Select a ticket by number.
- Review its information before resolving it.
- Confirm or cancel the resolution.
- Change a ticket's status from "Open" to "Resolved".
- Detect tickets that have already been resolved.

### Ticket Statistics
- Display the total number of tickets.
- Count open tickets.
- Count resolved tickets.

### Input Validation
- Reject empty ticket descriptions.
- Handle nonnumeric ticket searches.
- Check ticket numbers against valid list positions.
- Validate yes/no responses during ticket resolution.
- Handle invalid main-menu selections.

## Technologies Used

- **Python 3** — Core application development
- **Visual Studio Code** — Development environment
- **Git** — Version control
- **GitHub** — Source code hosting

The application currently uses Python's built-in functionality and does not require external packages.

## Programming Concepts Demonstrated

This project provides practical experience with:

- Python functions
- Variables and data types
- Lists and dictionaries
- Conditional statements
- `for` and `while` loops
- String methods and input validation
- Exception handling with `try` and `except`
- List indexing
- Dictionary access and updates
- Counters and basic statistics
- Debugging and manual testing
- Git version control

## Installation and Setup

### Requirements

- Python 3
- A command-line terminal

### Installation

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/dalizotte/helpdesk-ticket-manager
   ```

2. Navigate to the project directory:

   ```bash
   cd helpdesk-ticket-manager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

   Depending on your operating system and Python installation, you may need to use `python3 main.py` instead.

No additional dependencies are required.

## How to Use

When the application launches, it displays the following menu:

```text
===================
IT Help Desk Ticket Manager
===================
    1. Create New Ticket
    2. View All Tickets
    3. Search Tickets
    4. Resolve a Ticket
    5. View Ticket Statistics
    6. Exit
===================
```

Enter the corresponding number to select an operation.

### Example: Creating a Ticket

```text
Please Select an option: 1

Please describe your issue: Printer is not responding

Your ticket has been created and added to our tickets list.
```

### Example: Viewing Tickets

```text
====List Of Tickets====
1. Issue: Printer is not responding | Status: Open
2. Issue: Unable to connect to WiFi | Status: Resolved
```

### Example: Searching for a Ticket

```text
Please Select an option: 3

Please search for the number of ticket youre trying to find: 1

=====Ticket Found!=====
Ticket Number: 1
Issue: Printer is not responding
Status: Open
```

### Example: Resolving a Ticket

```text
Please Select an option: 4

What ticket number would you like to resolve? 1

Ticket Number: 1
Issue: Printer is not responding
Status: Open

Would you like to resolve this ticket? y/n: y

Ticket Number 1 has been resolved
```

### Example: Viewing Ticket Statistics

```text
Total Tickets: 2
Open Tickets: 1
Resolved Tickets 1
```

These examples illustrate application behavior using sample tickets.

## Ticket Data Structure

Tickets are stored as dictionaries inside a Python list.

Example:

```python
tickets = [
    {
        "issue": "Printer is not responding",
        "status": "Open"
    },
    {
        "issue": "Unable to connect to WiFi",
        "status": "Resolved"
    }
]
```

Each dictionary contains two fields:

- `issue` — A description of the technical problem.
- `status` — The ticket's current state, either `Open` or `Resolved`.

Tickets are numbered according to their positions in the list. List indices are converted into user-facing ticket numbers starting at 1.

## Current Limitations

The application is still under development.

- Tickets are stored in memory and are lost when the program exits.
- Ticket numbers are based on list positions rather than permanent unique identifiers.
- The interface is command-line only.
- Ticket priority, technician assignment, and user authentication are not implemented.

These limitations provide opportunities for future development.

## Development Roadmap

### Completed

- [x] V0.1 — Main menu and ticket creation
- [x] V0.2 — Ticket searching and input validation
- [x] V0.3 — Ticket resolution and status management
- [x] V0.4 — Ticket statistics

### Planned for V1.0

- [ ] V0.5 — Save ticket data to a JSON file
- [ ] V0.5 — Load saved tickets when the application starts
- [ ] V1.0 — Test persistence and ticket-management workflows
- [ ] V1.0 — Finalize documentation and release the first stable version

### Future Development

- [ ] Integrate SQLite for database storage
- [ ] Implement SQL-based ticket operations
- [ ] Develop a REST API using FastAPI
- [ ] Add permanent ticket IDs
- [ ] Explore ticket priorities and technician assignment

These features are planned enhancements and are not part of the current release.

## Testing

The application has been manually tested throughout development.

Testing includes:

- Creating valid tickets
- Rejecting empty ticket descriptions
- Viewing empty and populated ticket lists
- Searching for existing tickets
- Handling nonexistent ticket numbers
- Handling nonnumeric search input
- Resolving open tickets
- Preventing duplicate resolution
- Canceling resolution requests
- Verifying ticket status changes
- Checking ticket statistics

Automated testing is a possible future improvement.

## Project Goals

The IT Help Desk Ticket Manager was created to apply Python concepts to a practical IT support scenario.

The project emphasizes:

1. Building functional applications independently.
2. Learning structured programming and reusable functions.
3. Practicing debugging and problem-solving.
4. Understanding how applications manage data.
5. Developing experience with Git and GitHub.
6. Establishing a foundation for future work involving databases, APIs, and software engineering.

The project will continue to evolve as new programming concepts and technologies are introduced.

## License

No license has been assigned to this project.
