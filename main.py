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
        habit_name = habit_name.lower()
        if habit_name.strip() == '':
            print('Your habit name cannot be empty...')
        if len(habit_name.strip()) < 3:
            print('Your habit name cannot be less then 3 chracters...')
        if len(habit_name.strip()) > 30:
            print('Your habit name cannot be more then 30 charaters...')

    elif choice == '2':
        print('<< View Habits >>')
    elif choice == '3':
        print('<< Search Habit >>')
    elif choice == '4':
        print('<< Statistics >>')
    elif choice == '5':
        print('Exit')
