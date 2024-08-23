import json
import os


def save_ics_url(ics_url):
    with open('calendar_config.json', 'w') as config_file:
        json.dump({'ics_url': ics_url}, config_file)


def load_ics_url():
    if not os.path.exists('calendar_config.json'):
        with open('calendar_config.json', 'w') as config_file:
            json.dump({}, config_file)

    try:
        with open('calendar_config.json', 'r') as config_file:
            config = json.load(config_file)
            return config.get('ics_url')
    except json.JSONDecodeError:
        print("Error reading the JSON file.")
        return None
