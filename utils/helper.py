import json
import os

from dotenv import load_dotenv
from pychrome import Browser

# Load environment variables from a .env file
load_dotenv()

# Create a new Chrome browser instance
browser = Browser()


def callback(**kwargs):
    try:
        print("Received callback:", json.dumps(kwargs, indent=2))
    except Exception as e:
        print("Error during serialization:", e)


def execute_js_code(tab, js_code):
    tab.Runtime.evaluate(expression=js_code)


def start_new_tab():
    # Connect to an open tab (you can open a new tab using browser.new_tab())
    tab = browser.new_tab()
    tab.start()
    # Enable the necessary domains
    tab.Page.enable()
    tab.Runtime.enable()

    # Set the callback for the Runtime.evaluate method
    tab.set_listener("Runtime.executionContextCreated", callback)
    return tab


def start_existing_tab(idx: int):
    tab = browser.list_tab()[idx]
    print(browser.list_tab())
    return tab


class BaseData:
    last_called_time: float = 0
    valid_api_key: str = os.getenv("API_KEY")
    browser = browser
