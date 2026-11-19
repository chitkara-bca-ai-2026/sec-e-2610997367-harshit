import os

def box(title):
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)

def append_entry(filename, entry):
    with open(filename, 'a') as f:
        f.write(entry + '\n')
    print("[SUCCESS] New entry logged to 'daily_log.txt'.\n")

def display_log(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            entries = f.readlines()
        box('DAILY LOG BOOK')
        count = 0
        for entry in entries:
            count += 1
            print(f"[{count:02}] {entry.strip()}")

        print(f"\nTotal Logged Entries: {count}") 
    else:
        print("No log entries exist yet.")

box("OFFICE DAILY LOG BOOK")

while True:
    print("Select an operation:\n1. Add Log Entry\n2. Display Complete Log\n3. Exit")
    choice = int(input("Enter choice (1-3): "))
    if choice == 3:
        print('Thank you for using the Daily Log Book. Goodbye!')
        break 
    if choice == 1:
        entry = input('Enter log entry: ')
        append_entry('daily_log.txt', entry)
    if choice == 2:
        display_log('daily_log.txt')
        

        
