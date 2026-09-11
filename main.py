import json
file_path = "habits.json"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("The data file is corrupted. Starting with an empty habit list...")
    data = {}
    data["habits"] = []
except FileNotFoundError:
    print("The data file does not exist. Starting with an empty habit list...")
    data = {}
    data["habits"] = []

def main_menu():
    """
    Asks the user whether they want to return to the main menu.

    Returns:
        bool: True if the user chooses yes, False if they choose no.
    """
    while True:

        user_input = input('Do you wish to return to the main menu? (Y/N) ').lower().strip()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Didn\'t get that... Please try agian...')

def save_data(habit=None):
    """
    Saves data to the JSON file.

    If a habit name is provided, it appends the habit to the list.
    Writes the updated data dictionary to the file.
    """
    if habit:
        data['habits'].append(habit)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
def are_you_sure():
    """
    Prompts the user to confirm their action.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    while True:
        user_input = input(
            'Are you sure? (Y/N) ')
        user_input = user_input.lower()
        choice = None
        if user_input == 'y':
            choice = True
            return choice
        
        elif user_input == 'n':
            choice = False
            return choice
        else:
            print('Didn\'t get that... Please try again...')


def get_continue_choice():
    """
    Prompts the user to decide whether to continue or not.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    while True:
        user_input = input(
            'Would you like to continue? (Y/N) ')
        user_input = user_input.lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Didn\'t get that... Please try again...')


def add_habit():
    """
    Prompts the user to enter and validate a new habit name.

    Prevents duplicate habits, asks for confirmation before adding,
    optionally collects and confirms a note, and saves the completed
    habit dictionary to the JSON file.

    Returns:
        None
    """
    while True:
        habit_name = input('Enter Habit Name: ').title().strip()

        if habit_name == '':
            print('Your habit name cannot be empty...')
            continue

        if len(habit_name) < 3:
            print('Your habit name cannot be less then 3 chracters...')
            continue

        if len(habit_name) > 30:
            print('Your habit name cannot be more then 30 charaters...')
            continue

        if habit_name.isdigit():
            print('Your habit name cannot be a number...')
            continue

        habit_exists = False

        for habit in data["habits"]:
            if habit_name == habit["name"]:
                habit_exists = True
                break
        if habit_exists:
            print("This habit already exists. Please enter a different name.")
            continue

        if not are_you_sure():
            print("Adding habit cancelled.")
            return

        note = ""
        add_note = input("Would you like to add a note for this habit? (Y/N): ").lower().strip()
        if add_note == 'y':
            while True:
                note = input("Enter the note for this habit: ").strip()
                print(f'This note: " {note} " is going to be added to {habit_name} habit, ')
                if are_you_sure():
                    print('Note has been added successfully...')
                    break
                else:
                    note_choice = input('''1. Change Note
2. Delete Note
What would you like to do? ''')
                    if note_choice == '1':
                        continue
                    elif note_choice == '2':
                        print('Deleting note...')
                        note = ""
                        main_menu_choice = main_menu()
                        if main_menu_choice:
                            return
                        
                    else:
                        print('Didn\'t get that... Please try again...')
        new_habit = {
            "name": habit_name,
            "completed": False,
            "streak": 0,
            "note": note
        } # Information format
        save_data(new_habit)
        break


def view_habits():
    """
    Displays all saved habits with their names, completion status,
    streak values, and notes.

    If no habits exist, informs the user that the habit list is empty.

    Returns:
        None
    """
    if not data["habits"]:
        print("No habits found...")
        return
    else:
        for number, habit in enumerate(data["habits"], start=1):
            print(f"{number}: {habit['name']}")
            print(f"Completed: {habit['completed']}")
            print(f"Streak: {habit['streak']}")
            print(f"Note: {habit['note']}")


def search_habit():
    """
    Searches for a specific habit in the list.

    Prompts the user to enter a habit name to search for.
    Checks if the habit exists in the list.
    If found, notifies the user; otherwise, informs the user it was not found.
    Allows the user to continue searching or exit the search process.
    """
    if not data['habits']:
        print('You don\'t have any habits yet...')
    else:
        while True:
            search_input = input('Enter your habit: ')
            search_input = search_input.title().strip()

            if search_input in data['habits']:
                print(f'Habit {search_input} found! ')
                choice = get_continue_choice()
                if choice == False:
                    break
            else:
                print('Habit not found! ')
                choice = get_continue_choice()
                if choice == False:
                    break


def statistics():
    """
    Displays statistics about the habits.

    Calculates and displays the total number of habits in the list.
    """
    total_habits = len(data['habits'])
    print(f'Total Habits: {total_habits}')

def delete_habit():
    """
    Deletes a habit from the list.

    Prompts the user to enter a habit name to delete.
    Checks if the habit exists in the list.
    If found, removes the habit and saves the updated list to the JSON file.
    If not found, informs the user.
    """
    if not data['habits']:
        print('You don\'t have any habits yet...')
    else:
        while True:
            delete_input = input('Enter the habit you want to delete: ')
            delete_input = delete_input.title().strip()

            if delete_input in data['habits']:
                result_are_you_sure = are_you_sure()
                if result_are_you_sure:
                    data['habits'].remove(delete_input)
                    save_data()  # Save changes after deletion
                    print(f'Habit {delete_input} has been deleted! ')
                elif result_are_you_sure == False:
                    print('Deletion cancelled.')
                choice = get_continue_choice()
                if choice == False:
                    break

            else:
                print('Habit not found! ')
                choice = get_continue_choice()
                if choice == False:
                    break
while True:
    choice = input('''
===== Habit Tracker =====

1. Add Habit
2. View Habits
3. Search Habit
4. Statistics
5. Delete Habit
6. Exit

Choose an option: ''')
    if choice == '1':
        print('<< Add Habit >>')
        add_habit()

    elif choice == '2':
        print('<< View Habits >>')
        view_habits()

    elif choice == '3':
        print('<< Search Habit >>')
        search_habit()
    elif choice == '4':
        print('<< Statistics >>')
        statistics()
    elif choice == '5':
        print('<< Delete Habit >>')
        delete_habit()
    elif choice == '6':
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break
    else:
        print('Invalid choice! Please try again...')
print('-----------------------------------')