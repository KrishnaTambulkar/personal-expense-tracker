
Personal Expense Tracker Using Python
1. Project Overview

Personal Expense Tracker is a simple command-line Python project used to record and manage daily expenses.

The user can add an expense by entering its amount, category, and description. The program can display all recorded expenses, calculate the total expense, and show the total amount spent in each category.

The project is created using basic Python concepts and does not require any external libraries.

2. Objectives

The objectives of this project are:

To create a simple personal expense management system.
To practice basic Python programming.
To use lists, tuples, and dictionaries for storing data.
To use functions, loops, and conditional statements.
To calculate total and category-wise expenses.
To create a project that can be executed through the command line.
3. Features

The project contains the following options:

Add Expense
View All Expenses
Calculate Total Expense
View Category-wise Expense
Exit
4. Technologies Used
Python 3
Command Prompt / Terminal
Python built-in data structures

No external Python packages are required.

5. Requirements

The only requirement for running this project is:

Python 3.x

To check whether Python is installed, open Command Prompt or Terminal and run:

python --version

If that does not work, try:

python3 --version

No additional dependencies need to be installed.

6. Project Structure
Personal-Expense-Tracker/
│
├── expense_tracker.py
└── README.md
7. How to Set Up the Project
Step 1: Install Python

Install Python 3 on your computer if it is not already installed.

For Windows, Python can be installed with the option to add Python to PATH enabled.

Step 2: Clone the Repository

Open Command Prompt or Terminal and run:

git clone https://github.com/your-username/Personal-Expense-Tracker.git

Replace your-username with the GitHub username of the repository owner.

You can also download the repository as a ZIP file from GitHub.

Step 3: Open the Project Folder

Move into the project folder:

cd Personal-Expense-Tracker
Step 4: Check the Files

The project folder should contain:

expense_tracker.py
README.md
8. Dependency Installation

This project uses only Python's built-in features.

Therefore, no external packages or dependencies are required.

There is no need to run:

pip install
9. How to Run the Project

The project is completely executable from the command line.

Windows

Open Command Prompt in the project folder and run:

python expense_tracker.py

If required, use:

python3 expense_tracker.py
Linux / macOS

Open Terminal in the project folder and run:

python3 expense_tracker.py

The program will display the main menu.

10. Main Menu

When the program starts, it displays:

===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

The user can select an option by entering its number.

11. How the Program Works
Add Expense

The user enters:

Amount
Category
Description

Example:

Enter amount: 250
Enter category: Food
Enter description: Lunch
Expense added successfully!

The information is stored as a tuple:

(amount, category, description)

All expense tuples are stored inside a list.

View All Expenses

This option displays all the expenses entered during the current program execution.

Example:

----- ALL EXPENSES -----
Amount: 250.0 | Category: Food | Description: Lunch
Amount: 100.0 | Category: Travel | Description: Bus
Total Expense

This option adds the amount of every stored expense and displays the total.

Example:

Total Expense: 350.0
Category-wise Expense

This option calculates how much money was spent in each category.

Example:

----- CATEGORY WISE EXPENSE -----
Food : 250.0
Travel : 100.0
Exit

Option 5 terminates the program.

12. Python Concepts Used

The project uses:

Variables
input() and print()
Lists
Tuples
Dictionaries
Functions
for loop
while loop
if-elif-else
Arithmetic operations
13. Data Structures Used
List

A list stores all the expenses:

expenses = []
Tuple

Each expense is stored as a tuple:

expense = (amount, category, description)
Dictionary

A dictionary stores category-wise expense totals:

categories = {}
14. Project Executability

The project can be executed directly from a terminal or command prompt.

It does not require:

GUI software
External Python libraries
Database software
Internet connection while running

Only Python 3 is required.

15. Sample Run
===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

Enter your choice: 1
Enter amount: 250
Enter category: Food
Enter description: Lunch
Expense added successfully!

===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

Enter your choice: 1
Enter amount: 100
Enter category: Travel
Enter description: Bus
Expense added successfully!

===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

Enter your choice: 3
Total Expense: 350.0

===== PERSONAL EXPENSE TRACKER =====
1. Add Expense
2. View All Expenses
3. Total Expense
4. Category-wise Expense
5. Exit

Enter your choice: 4

----- CATEGORY WISE EXPENSE -----
Food : 250.0
Travel : 100.0
16. Testing

The project was tested using different menu options.

Test Case	Input	Expected Result
Add Expense	Amount, category, description	Expense is added
View Expenses	2	All expenses are displayed
Total Expense	3	Total amount is displayed
Category-wise Expense	4	Category totals are displayed
Exit	5	Program terminates
Invalid Choice	Any number other than 1-5	Invalid choice message is displayed
17. Limitations
Expenses are stored only during the current program execution.
Data is lost when the program is closed.
The project does not use a database.
The project does not save expenses to a file.
It is designed for basic personal expense tracking.
18. Future Scope

The project can be improved in the future by adding:

Permanent file storage.
Date-wise expense tracking.
Monthly expense reports.
Budget limits.
Search and delete options.
Graphical user interface.
Database support.
19. Conclusion

The Personal Expense Tracker is a simple Python command-line project that demonstrates the use of basic Python programming concepts.

The project combines lists, tuples, dictionaries, functions, loops, conditional statements, input/output, and arithmetic operations to create a useful expense management application.

20. Author

Developed as a Python Essentials course project.
