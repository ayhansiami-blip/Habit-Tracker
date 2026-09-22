from datetime import date, timedelta

today = date.today()


import json

file_path = "habits.json"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)


    for habit in data["habits"]:
        if habit["last completed"]:
            last_completed = date.fromisoformat(habit["last completed"])

            if not last_completed == today:
                habit["completed"] = False

            else:
                habit["completed"] = True


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



def update_streak(habit):
    if habit["last completed"] is None:
        habit["streak"] = 1
        return

    last_completed = date.fromisoformat(habit["last completed"])
    yesterday = today - timedelta(days=1)

    if last_completed == today:
        return

    elif last_completed == yesterday:
        habit["streak"] += 1
        return

    else:
        habit["streak"] = 1

def save_data():
    """
    Saves the current habit data to the JSON file.

    Opens the JSON file in write mode and writes the current
    data dictionary to it with UTF-8 encoding and indentation
    for better readability.

    Returns:
        None
    """
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
            print('Your habit name cannot be empty.')
            continue

        if len(habit_name) < 3:
            print('Your habit name cannot be less then 3 chracters.')
            continue

        if len(habit_name) > 30:
            print('Your habit name cannot be more then 30 charaters.')
            continue

        if habit_name.isalnum() and habit_name.isdigit():
            print("Habit name cannot be only numbers.")
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
                print(f"""This note:
" {note} " ,
 is going to be added to " {habit_name} " habit,""")
                if are_you_sure():
                    print('Note has been added successfully...')
                    break
                else:
                    while True:
                        note_choice = input('''1. Change Note
2. Delete Note
What would you like to do? ''')
                        if note_choice == '1':
                            break

                        elif note_choice == '2':
                            print('Deleting note...')
                            note = ""

                            if main_menu():
                                return

                            break

                        else:
                            print('Didn\'t get that... Please enter 1 or 2.')

                            
        elif add_note == 'n':
            pass

        else:
            print('Invalid choice! Please try again...')
            continue
        new_habit = {
            "name": habit_name,
            "completed": False,
            "last completed": None,
            "streak": 0,
            "note": note
        } # Information format
        data["habits"].append(new_habit)
        save_data()
        print('Habit saved successfully.')
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
            print('-------------------------------------')
            print(f"{number}: {habit['name']}")
            print(f"Completed: {habit['completed']}")
            print(f"Streak: {habit['streak']}")
            print(f"Notes: {habit['note']}")
            print('-------------------------------------')

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

            found = False

            for habit in data["habits"]:
                if search_input == habit["name"]:
                    found = True
                    break


            if found:
                print(f'Habit {search_input} found!: ')
                print('-------------------------------------')
                print(f'Habit Name: {habit["name"]} ')
                print(f'Completed: {habit["completed"]}')
                print(f'Streak: {habit["streak"]}')
                print(f'Notes: {habit["note"]}')
                print('-------------------------------------')
                choice = get_continue_choice()
                if not choice:
                    return
            else:
                print('Habit not found')
                choice = get_continue_choice()
                if not choice:
                    return

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
            delete_input = input('Enter your habit: ')
            delete_input = delete_input.title().strip()

            found = False

            for habit in data["habits"]:
                if delete_input == habit["name"]:
                    found = True
                    break


            if found:
                choice = are_you_sure()
                if choice:
                    data["habits"].remove(habit)
                    save_data()
                    choice3 = get_continue_choice()
                    if choice3:
                        continue
                    else:
                        return
                    
                else:
                    print('Deletion cancelled; What do you want to do?')
                    choice2 = get_continue_choice()
                    if choice2:
                        continue
                    else:
                        return

            else:
                print('Habit not found! ')
                choice4 = get_continue_choice()
                if choice4:
                    pass
                else:
                    print('Going back to main menu...')
                    return


def tick_habit():
    if not data["habits"]:
            print("No habits found...")
            return



    while True:

        print("\n======== Tick Habit ========\n")
        for number, habit in enumerate(data["habits"], start=1):
                    
                    if habit['completed'] == True:
                        completed = '[✓]'
                    else:
                        completed = '[ ]'

                    print(
                        f"\n{number}: {habit['name']}    "
                        f"{completed}    "
                        f"Streak: {habit['streak']}"
                    )
        print("\n0: Back")

        while True:
            choice = input("\nChoose a habit: ").strip()

            if choice == "0":
                if are_you_sure():
                    return
                else:
                    continue

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(data["habits"]):
                print("Invalid habit number.")
                continue

            break


        selected_habit = data["habits"][choice -1]


        print(f"\nYou selected: {selected_habit['name']}")
        print(f"Completed: {selected_habit['completed']}")
        print(f"Streak: {selected_habit['streak']}")
        if selected_habit["note"]:
            print(f"Notes: {selected_habit['note']}")

        else:
            print("Notes: Empty...")

        if not are_you_sure():
            print("Tick cancelled.")
            continue

        update_streak(selected_habit)
        
        selected_habit["completed"] = True
        selected_habit["last completed"] = str(today)

        save_data()

        print(f"\n✓ {selected_habit['name']} has been ticked!")               



while True:
    choice = input(f'''
======== Habit Tracker ========

Date: {today}

        1. Add Habit

        2. View Habits

        3. Search Habit

        4. Statistics

        5. Delete Habit

        6. Tick Habit

        7. Exit



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
        print('<< Tick Habit >>')
        tick_habit()

    elif choice == '7':
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break

    else:
        print('Invalid choice! Please try again...')
print('-----------------------------------')