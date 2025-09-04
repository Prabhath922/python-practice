import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"  # Free jokes API
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()  # Convert response to JSON
        print("\n🤣 Here's your joke:")
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}\n")
    else:
        print("⚠️ Failed to fetch a joke. Try again later.")

def main():
    while True:
        get_joke()
        choice = input("Want another joke? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()