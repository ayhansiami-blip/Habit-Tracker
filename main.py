import json
import os
file_path = "habits.json"
if os.path.exists(file_path):
    with open("habits.json", "r", encoding="utf-8") as file:
        data = json.load(file)
else:
    data = {}

    with open("habits.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

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
        habit_name = habit_name.lower().strip()
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
                data['habits'].append(habit_name)

                with open("habits.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
                print(f'Habit {habit_name} has been added!')
    elif choice == '2':
        print('<< View Habits >>')
    elif choice == '3':
        print('<< Search Habit >>')
    elif choice == '4':
        print('<< Statistics >>')
    elif choice == '5':
        print('<< Exit >>')
        print('Thank you for using my program :) ')
        break
