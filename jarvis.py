# Simple Jarvis Chatbot with Functions
# Author: Parth Londase

import datetime
import webbrowser

def show_help():
    """Displays available commands."""
    print("Jarvis: I can do these things:")
    print("- time : tell the current time")
    print("- date : tell today's date")
    print("- youtube : open YouTube")
    print("- google : open Google")
    print("- search <topic> : search on Google")
    print("- exit : quit the program")

def get_time():
    """Returns current time as a string."""
    now = datetime.datetime.now()
    return now.strftime("Current time is %I:%M %p")

def get_date():
    """Returns today's date as a string."""
    today = datetime.date.today()
    return today.strftime("Today is %B %d, %Y")

def open_youtube():
    """Opens YouTube in browser."""
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube..."

def open_google():
    """Opens Google in browser."""
    webbrowser.open("https://www.google.com")
    return "Opening Google..."

def search_google(topic):
    """Searches Google for the given topic."""
    webbrowser.open(f"https://www.google.com/search?q={topic}")
    return f"Searching for {topic}..."

def main():
    print("Hello, I am Jarvis! Type 'help' to see what I can do.")
    while True:
        command = input("\nYou: ").lower()
        
        if command in ("exit", "quit", "stop"):
            print("Jarvis: Goodbye!")
            break
        elif command == "help":
            show_help()
        elif command == "time":
            print("Jarvis:", get_time())
        elif command == "date":
            print("Jarvis:", get_date())
        elif command == "youtube":
            print("Jarvis:", open_youtube())
        elif command == "google":
            print("Jarvis:", open_google())
        elif command.startswith("search "):
            topic = command.replace("search ", "")
            print("Jarvis:", search_google(topic))
        else:
            print("Jarvis: Sorry, I don't understand. Type 'help' for options.")

if __name__ == "__main__":
    main()
