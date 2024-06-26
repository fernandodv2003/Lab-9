# By: Fernando Vazquez
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


def decode(encrypted_password: str):
    arr = {}
    length = len(encrypted_password)
    for i in range(len(encrypted_password)):
        arr[i] = int(int(encrypted_password)/pow(10, length - 1 - i))
        encrypted_password = int(encrypted_password) % pow(10, length - 1 - i)

    for i in range(len(arr)):
        arr[i] = arr[i] - 3
        if arr[i] < 0:
            if arr[i] == -1:
                arr[i] = 9
            elif arr[i] == -2:
                arr[i] = 8
            elif arr[i] == -3:
                arr[i] = 7

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
                new_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, "
                      f"and the original password is {new_password}.")
                print()
        elif selection == 3:
            break


if __name__ == '__main__':
    main()

