#Mailroom Part 1
import sys

donor_db == [("John Smith", [500.00, 150.00, 20.00]),
             ("Jane Doe", [340.00, 30.00, 200.00]),
             ("Jason Bourne", [240.00, 140.00]),
             ("")]

def exit_program():
    print("Thank you. Bye")
    sys.exit()

def main():
    """Mailroom main program loop with menu"""

    menu = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

    while True:
        choice = input(menu)
        if choice == '1':
            print("Selected 1")
        elif choice == '2':
            print("Selected 2")
        elif choice == '3':
            exit_program()
        else:
            print("bad choice")

if __name__ == "__main__":
    main()
