# By: Fernando Vazquez
from decoder import Decoder
def encode(password: str):
    arr = {}
    length = len(password)
    for i in range(len(password)):
        arr[i] = int(int(password)/pow(10, length - 1 - i))
        password = int(password) % pow(10, length - 1 - i)

    for i in range(len(arr)):
        arr[i] = arr[i] + 3
        if arr[i] > 9:
            arr[i] = arr[i] % 10

    string = ''

    for i in range(len(arr)):
        string += str(arr[i])

    return string


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def main():
    encoded_password = ''

    new_password = ''
    while True:
        print_menu()
        selection = int(input("Please enter an option: "))
        if selection == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif selection == 2:
            if encoded_password == '':
                print("No password has been stored yet!")
                print()
            else:
                new_password = Decoder.decode(encoded_password)
                print(f"The encoded password is {encoded_password}, "
                      f"and the original password is {new_password}.")
                print()
        elif selection == 3:
            break


if __name__ == '__main__':
    main()

