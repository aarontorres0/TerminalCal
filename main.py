from calendar_cli.calendar import list_past_events, list_upcoming_events, view_saved_ics
from calendar_cli.config import load_ics_url, save_ics_url


def main():
    ics_url = load_ics_url()

    while True:
        print("\n--- Calendar CLI ---")
        print("1. List Upcoming Events")
        print("2. List Past Events")
        print("3. Save .ics URL")
        print("4. View Saved .ics URL")
        print("q. Quit")
        print("\n")
        choice = input("Choose an option: ")

        if choice == '1':
            if ics_url:
                list_upcoming_events(ics_url)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '2':
            if ics_url:
                list_past_events(ics_url)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '3':
            ics_url_input = input("Enter the .ics URL: ")
            save_ics_url(ics_url_input)
            ics_url = load_ics_url()
            print(f".ics URL '{ics_url_input}' saved.")
        elif choice == '4':
            print(view_saved_ics())
        elif choice.lower() in ['q', 'quit', 'e', 'exit']:
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()
