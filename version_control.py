def encode(raw_password):
    encoded_password = ""; raw_password_list = list(str(raw_password))
    for i in range(len(raw_password_list)):
        encoded_password += str(int(raw_password_list[i]) + 3)
    return encoded_password


def decode(password):
    decode_str = ""
    int_list = []
    for i in password:
        int_list += i
    for item in int_list:
        a = int(item) - 3
        decode_str += str(a)
    return decode_str

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
            stored_password += encode(raw_to_encode)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == 2:
            print(f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}.")
        elif user_input == 3:
            loopActive = False


if __name__ == '__main__':
    main()