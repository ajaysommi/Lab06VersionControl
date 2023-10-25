def encode(raw_password):
    encoded_password = ""; raw_password_list = list(str(raw_password))
    for i in range(len(raw_password_list)):
        encoded_password += str(int(raw_password_list[i]) + 3)
    return encoded_password
def main():
    stored_password = ''
    loopActive = True
    while loopActive:
        print("Menu: ")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            raw_to_encode = int(input("Please enter your passcode to encode: "))
            print(encode(raw_to_encode))
            stored_password += encode(raw_to_encode)
            print("Your password has been encoded and stored!")

        elif user_input == 2:
            print(f"The encoded password is {stored_password}, and the original password is ")

if __name__ == '__main__':
    main()