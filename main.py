
def encoder(value):
    passcode = ''
    for digit in value:
        encoded_digit = str((int(digit) + 3) % 10)
        passcode += encoded_digit
    return passcode

def decoder(value):
    passcode = ''
    for digit in value:
        decoded_digit = str((int(digit) - 3) % 10)
        passcode += decoded_digit
    return passcode

def main():
    run = True
    while run:
        print("1. To encode /n 2. To decode /n 3. To exit")
        choice = input("Enter your choice (1 or 2 or 3): ")
        if choice == "1":
            digits = input("Enter an 8-digit password: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print(f'The encoded password is {encoder(digits)}, and the original password is {decoder(digits)}')
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()

if __name__ == '__main__':
    main()
