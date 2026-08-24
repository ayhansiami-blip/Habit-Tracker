import json
file_path = "habits.json"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("The data file is corrupted. Starting with an empty habit list...")
    data = {}


def save_data(habit_name=None):
    """
    Saves data to the JSON file.

    If a habit name is provided, it appends the habit to the list.
    Writes the updated data dictionary to the file.
    """
    if habit_name:
        data['habits'].append(habit_name)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if 'habits' not in data:
    data['habits'] = []
    save_data()


def get_continue_choice():
    """
    Prompts the user to decide whether to continue or not.

    Returns:
        str: 'y' if the user wants to continue, 'n' otherwise.
    """
    while True:
        user_input = input(
            'Would you like to continue? (Y/N) ')
        user_input = user_input.lower()
        if user_input == 'y':
            return user_input
        elif user_input == 'n':
            return user_input
        else:
            print('Didn\'t get that... Please try again...')


def add_habit():
    """
    Adds a new habit to the list.

    Prompts the user to enter a habit name.
    Validates the input (not empty, length between 3 and 30 characters).
    Prevents duplicate habits by checking the existing list.
    Saves the new habit to the JSON file if valid.
    """
    while True:
        habit_name = input('Enter Habit Name: ')
        habit_name = habit_name.title().strip()
        if habit_name == '':
            print('Your habit name cannot be empty...')
        elif len(habit_name) < 3:
            print('Your habit name cannot be less then 3 chracters...')
        elif len(habit_name) > 30:
            print('Your habit name cannot be more then 30 charaters...')
        else:
            if habit_name in data['habits']:
                print(
                    'This habit already exists! Please enter a different habit name.')
            else:
                save_data(habit_name)
                print(f'Habit {habit_name} has been added!')
                break


def view_habits():
    """
    Displays all habits in the list.

    If the list is empty, notifies the user.
    Otherwise, displays all habits with their index numbers.
    """
    if not data['habits']:
        print('No habit found...')
    else:
        for number, habit in enumerate(data["habits"], start=1):
            print(f'{number}: {habit}')


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
                if choice == 'n':
                    break
            else:
                print('Habit not found! ')
                choice = get_continue_choice()
                if choice == 'n':
                    break


def statistics():
    """
    Displays statistics about the habits.

    Calculates and displays the total number of habits in the list.
    """
    total_habits = len(data['habits'])
    print(f'Total Habits: {total_habits}')


while True:
    choice = input('''
===== Habit Tracker =====

1. Add Habit
2. View Habits
3. Search Habit
4. Statistics
5. Exit

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
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break
    else:
        print('Invalid choice! Please try again...')
