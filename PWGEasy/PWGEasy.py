from random import choice
print("Welcome to PassWordGeneratorEasy [PWGEasy]")
user_choice = input("\033[1;32mPress 'Enter' to generate a strong password or type 'Close' to close the software:\n>>\033[m ").strip().capitalize()

coolwords = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "!", "@", "#", "$",
    "%", "&", "*", "(", ")", "-", "_", "+", "-", "/", "=", "<", ">", "[", "]",
    "{", "}", ":", ";", "?"
]

if user_choice == "" or user_choice == " " or user_choice == "Enter":
    while True:
        print(f"\033[1;32mPassword generated:\033[m\n {choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}{choice(coolwords)}")
        a = input("").strip().capitalize()
        if a == "Close":
            print("Closing...")
            break
elif user_choice == "Close":
    while True:
        print("Closing...")
        break
else:
    print(f"\033[1;32mError! You type {user_choice}\033[m")