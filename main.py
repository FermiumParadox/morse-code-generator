# pip install MorseCodePy
from MorseCodePy import encode

# welcome message
print("******** Welcome to - Morse Code Generator *********")

while True:
    # ask the user for input
    text = input("Enter a text you would like to generate: ").strip().lower()

    # check if the input is valid
    # if valid change it to morse code else ask the input again
    if text:
        encoded_string: str = encode(text, language='english')
        # show the output
        print(f'The generated morse code for "{text}" is "{encoded_string}"')
        # check if the user wants to continue or exit
        while True:
            user_choice = input("Do you wish to continue? (y/n): ").lower()

            if user_choice == 'y':
                break
            elif user_choice == 'n':
                print("Goodbye!")
                exit()
            else:
                print("Invalid input, please type 'y' or 'n'")
    else:
        print("Invalid input, please try again")


