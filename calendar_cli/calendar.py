import datetime

import pytz
import requests
from ics import Calendar

from calendar_cli.config import load_ics_url


def view_saved_ics():
    ics_url = load_ics_url()
    if not ics_url:
        return "No .ics URL is saved. Please save a URL first."

    return f"URL: {ics_url}"


def fetch_events(ics_url):
    try:
        response = requests.get(ics_url)
        response.raise_for_status()
        return Calendar(response.text).events
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error parsing calendar data: {e}")
    return []


def format_datetime(dt, timezone="UTC"):
    dt = dt.astimezone(pytz.timezone(timezone))
    date_str = dt.strftime("%Y-%m-%d")
    time_str = dt.strftime("%I:%M%p").lower().lstrip("0")
    return f"{date_str} {time_str}"


def list_upcoming_events(ics_url, downloading_events):
    events = fetch_events(ics_url)
    if not events:
        print("No events found or failed to fetch events.")
        return

    timezone = "America/New_York"
    now = datetime.datetime.now(pytz.timezone(timezone))
    upcoming_events = [event for event in events if event.begin > now]

    if downloading_events:
        return upcoming_events
    elif not upcoming_events:
        print("\n")
        print("-" * 40)
        print("|" + " " * 10 + "NO UPCOMING EVENTS" + " " * 10 + "|")
        print("-" * 40)
    else:
        print("\nUpcoming Events:")
        print("-" * 40)
        for event in upcoming_events:
            start_time = format_datetime(event.begin, timezone)
            end_time = format_datetime(event.end, timezone)
            print(f"Name: {event.name}")
            print(f"Date: {start_time.split(' ')[0]}")
            print(f"Start Time: {start_time.split(' ')[1]}")
            print(f"End Time: {end_time.split(' ')[1]}")
            print("-" * 40)


def list_past_events(ics_url, downloading_events):
    events = fetch_events(ics_url)
    if not events:
        print("No events found or failed to fetch events.")
        return

    timezone = "America/New_York"
    now = datetime.datetime.now(pytz.timezone(timezone))
    past_events = [event for event in events if event.end < now]

    if downloading_events:
        return past_events
    elif not past_events:
        print("\n")
        print("-" * 40)
        print("|" + " " * 12 + "NO PAST EVENTS" + " " * 12 + "|")
        print("-" * 40)
    else:
        print("\nPast Events:")
        print("-" * 40)
        for event in past_events:
            start_time = format_datetime(event.begin, timezone)
            end_time = format_datetime(event.end, timezone)
            print(f"Name: {event.name}")
            print(f"Date: {start_time.split(' ')[0]}")
            print(f"Start Time: {start_time.split(' ')[1]}")
            print(f"End Time: {end_time.split(' ')[1]}")
            print("-" * 40)


def download_upcoming_events(ics_url, filename="upcoming_events.txt"):
    events = list_upcoming_events(ics_url, True)
    timezone = "America/New_York"
    with open(filename, "w") as file:
        file.write("Upcoming Events:\n")
        file.write("-" * 40)
        for event in events:
            start_time = format_datetime(event.begin, timezone)
            end_time = format_datetime(event.end, timezone)
            file.write(f"\nName: {event.name}\n")
            file.write(f"Date: {start_time.split(' ')[0]}\n")
            file.write(f"Start Time: {start_time.split(' ')[1]}\n")
            file.write(f"End Time: {end_time.split(' ')[1]}\n")
            file.write("-" * 40)
    print(f"Upcoming events downloaded to {filename}")


def download_past_events(ics_url, filename="past_events.txt"):
    events = list_past_events(ics_url, True)
    timezone = "America/New_York"
    with open(filename, "w") as file:
        file.write("Past Events:\n")
        file.write("-" * 40)
        for event in events:
            start_time = format_datetime(event.begin, timezone)
            end_time = format_datetime(event.end, timezone)
            file.write(f"\nName: {event.name}\n")
            file.write(f"Date: {start_time.split(' ')[0]}\n")
            file.write(f"Start Time: {start_time.split(' ')[1]}\n")
            file.write(f"End Time: {end_time.split(' ')[1]}\n")
            file.write("-" * 40)
    print(f"Past events downloaded to {filename}")
