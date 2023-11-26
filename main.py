def main():
    # Print the banner
    print("Welcome to Ryokan Genetique - https://ryokangenetique.com")

    # Options
    options = {
        "1": ("Book Cat Boarding Stay", "https://ryokangenetique.com/booking/"),
        "2": ("Book To View Cat Hotel", "https://ryokangenetique.com/cat-boarding-hotel-viewing-session/"),
        "3": ("Virtual Tour", "https://ryokangenetique.com/virtual-tour/"),
        "4": ("Cat Boarding Preparation", "https://ryokangenetique.com/cat-boarding-preparation/"),
        "5": ("Cat Boarding Requirement", "https://ryokangenetique.com/cat-boarding-requirements/"),
        "6": ("Contact us", "https://ryokangenetique.com/contact-us/"),
        "7": ("Whatsapp us", "https://wa.me/6586170470")
    }

    # Display options
    for key, (text, url) in options.items():
        print(f"{key}) {text} - {url}")

    # User input for selection
    choice = input("Please select an option: ")

    # Process the user input
    if choice in options:
        print(f"You selected: {options[choice][0]}")
        print(f"URL: {options[choice][1]}")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
