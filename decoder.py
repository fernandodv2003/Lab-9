<<<<<<<<< Temporary merge branch 1

=========
# Created by Yanka Deshkovski

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
>>>>>>>>> Temporary merge branch 2
