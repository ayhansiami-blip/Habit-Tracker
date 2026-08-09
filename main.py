import json
import os
file_path = "habits.json"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
else:
    data = {}

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


def get_continue_choice():
    while True:
        continue_choice_input = input(
            'Would you like to continue? (Y/N) ')
        continue_choice_input = continue_choice_input.lower()
        if continue_choice_input == 'y':
            return continue_choice_input
        elif continue_choice_input == 'n':
            return continue_choice_input
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
        habit_name = input('Enter Habit Name: ')
        habit_name = habit_name.title().strip()
        if habit_name == '':
            print('Your habit name cannot be empty...')
        elif len(habit_name) < 3:
            print('Your habit name cannot be less then 3 chracters...')
        elif len(habit_name) > 30:
            print('Your habit name cannot be more then 30 charaters...')
        else:
            if 'habits' not in data:
                data['habits'] = []
            if habit_name in data['habits']:
                print('This habit already exists! ')
            else:
                with open(file_path, "w", encoding="utf-8") as file:
                    data['habits'].append(habit_name)
                    json.dump(data, file, indent=4)
                print(f'Habit {habit_name} has been added!')
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
            print('you don\'t have any habits yet...')
        else:
            while True:
                search_input = input('Enter your habit: ')
                search_input = search_input.title().strip()

                if search_input in data['habits']:
                    print(f'Habit {search_input} found! ')
                    continue_choice_input = get_continue_choice()
                    if continue_choice_input == 'y':
                        continue
                    elif continue_choice_input == 'n':
                        break
                else:
                    print('Habit not found! ')
                    continue_choice_input = get_continue_choice()
                    if continue_choice_input == 'y':
                        continue
                    elif continue_choice_input == 'n':
                        break
    elif choice == '4':
        print('<< Statistics >>')
        print(f'Total Habits: {len(data['habits'])}')
    elif choice == '5':
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break
