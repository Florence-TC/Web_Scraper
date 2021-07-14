message = input()
key = int(input())

decoded_message = ''

new_key = key.to_bytes(2, byteorder='little')
total = sum(new_key)
for char in message:
    new_char = chr(ord(char) + total)
    decoded_message += new_char
print(decoded_message)
