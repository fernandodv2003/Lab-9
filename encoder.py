# By: Fernando Vazquez

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) + 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

#Example usage
encoded_password = "00009962"
decoded_password = decode(encoded_password)
print("The encoded password is:", encoded_password)
print("The decoded password is:", decoded_password)

