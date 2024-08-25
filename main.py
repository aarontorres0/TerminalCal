from calendar_cli.calendar import (
    download_past_events,
    download_upcoming_events,
    list_past_events,
    list_upcoming_events,
    view_saved_ics,
)
from calendar_cli.config import load_ics_url, save_ics_url

VALID_TIMEZONES = [
    'America/Adak', 
    'America/Anchorage', 
    'America/Chicago', 
    'America/Denver', 
    'America/Detroit', 
    'America/Indiana/Indianapolis', 
    'America/Los_Angeles', 
    'America/New_York', 
    'America/Phoenix', 
    'America/Sitka', 
    'America/Juneau', 
    'America/Boise'
]

def get_valid_timezone():
    print("Please select a timezone from the following list:")
    for tz in VALID_TIMEZONES:
        print(f"  - {tz}")
    
    while True:
        timezone = input("Enter your preferred timezone: ").strip()
        if timezone in VALID_TIMEZONES:
            return timezone
        else:
            print("Invalid timezone. Please choose from the list provided.")

def main():
    ics_url = load_ics_url()
    timezone = get_valid_timezone()

    while True:
        print("\n--- Calendar CLI ---")
        print("1. List Upcoming Events")
        print("2. List Past Events")
        print("3. Save New .ics URL")
        print("4. View Saved .ics URL")
        print("5. Download Upcoming Events")
        print("6. Download Past Events")
        print("7. Change Timezone")
        print("8. View Saved Timezone")
        print("q. Quit")
        print("\n")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            if ics_url:
                list_upcoming_events(ics_url, False, timezone)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '2':
            if ics_url:
                list_past_events(ics_url, False, timezone)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '3':
            ics_url_input = input("Enter the .ics URL: ").strip()
            save_ics_url(ics_url_input)
            ics_url = load_ics_url()
            print(f".ics URL '{ics_url_input}' saved.")
        elif choice == '4':
            print(view_saved_ics())
        elif choice == '5':
            if ics_url:
                download_upcoming_events(ics_url, timezone)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '6':
            if ics_url:
                download_past_events(ics_url, timezone)
            else:
                print("No .ics URL is saved. Please save a URL first.")
        elif choice == '7':
            timezone = get_valid_timezone()
            print(f"New timezone is {timezone}")
        elif choice == '8':
            print(f"Saved timezone is {timezone}")
        elif choice.lower() in ['q', 'quit']:
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
