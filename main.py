import json
file_path = "habits.json"
try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("The data file is corrupted. Starting with an empty habit list...")
    data = {}


def save_data(habit_name=None):
    if habit_name:
        data['habits'].append(habit_name)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if 'habits' not in data:
    data['habits'] = []
    save_data()


def get_continue_choice():
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
        print(' << Add Habit >>')
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
                    save_data()
                    print(f'Habit {habit_name} has been added!')
                    break
    elif choice == '2':
        print('<< View Habits >>')
        if not data['habits']:
            print('No habit found...')
        else:
            for number, habit in enumerate(data["habits"], start=1):
                print(f'{number}: {habit}')

    elif choice == '3':
        print('<< Search Habit >>')
        if not data['habits']:
            print('You don\'t have any habits yet...')
        else:
            while True:
                search_input = input('Enter your habit: ')
                search_input = search_input.title().strip()

                if search_input in data['habits']:
                    print(f'Habit {search_input} found! ')
                    continue_choice_input = get_continue_choice()
                    if continue_choice_input == 'n':
                        break
                else:
                    print('Habit not found! ')
                    continue_choice_input = get_continue_choice()
                    if continue_choice_input == 'n':
                        break
    elif choice == '4':
        print('<< Statistics >>')
        print(f'Total Habits: {len(data["habits"])}')
    elif choice == '5':
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break
    else:
        print('Invalid choice! Please try again...')
