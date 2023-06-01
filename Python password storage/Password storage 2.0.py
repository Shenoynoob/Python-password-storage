import os

def main():
    file_path = "passwords.txt"
    current_directory = os.getcwd()
    print("Password file location:", os.path.join(current_directory, file_path))

    while True:
        print("\n==== Password Manager ====")
        print("1. Store a password")
        print("2. View stored passwords")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            password = input("Enter the password to store: ")
            with open(file_path, "a+") as file:
                file.seek(0)
                existing_passwords = file.read().splitlines()

                if password in existing_passwords:
                    print("Password already exists.")
                else:
                    file.write(password + "\n")
                    print("Password stored successfully.")

        elif choice == "2":
            with open(file_path, "r") as file:
                passwords = file.read().splitlines()

                if not passwords:
                    print("No passwords stored.")
                else:
                    print("Stored passwords:")
                    for password in passwords:
                        print(password)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
