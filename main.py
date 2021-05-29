import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's,', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def find(letter):
    for i in alphabet:
        if letter == i:
            return alphabet.index(letter)
# Function to find the position of the letters in the alphabet for each character in the message


def msg_pos(msg_list):
    list_lower = []
    list_pos = []
    for i in msg_list:
        list_lower.append(i.lower())
    for i in list_lower:
        if i == ' ':
            list_pos.append(i)
        elif i.isnumeric():
            print('Sorry. This cipher machine does not work with numbers. Please adjust your message accordingly.')
            sys.exit()
        else:
            list_pos.append(find(i))
    return list_pos
# Uses the above function and then puts the positions in a list of integers. Characters which are spaces are put in the
# list as a string.


def shift(list_pos):
    global shiftNumber
    shifted_list = []
    for i in list_pos:
        if i == ' ':
            shifted_list.append(i)
        elif type(i) == int:
            i = i + shiftNumber
            if i > 25:
                i = i - 26
                shifted_list.append(i)
            else:
                shifted_list.append(i)
    return shifted_list
# Function to shift the list of position numbers of the letters up or down according to the shift number.


def shifted_letter(shifted_list):
    new_message = []
    global alphabet
    for i in shifted_list:
        if i == ' ':
            new_message.append(i)
        else:
            new_message.append(alphabet[i])
    return ''.join(new_message)
# Function to return the position numbers back to their appropriate letters.

# print(msg_pos(msg))  # testing msg_pos function
# print(shift([23, 24, 25]))  # testing shift function
# print(shifted_letter([24, 25, 0, ' ', 3]))  # testing shifted_letter function
# print(shifted_letter(shift(msg_pos(msg))))  # testing overall cipher


print('Hello. Welcome to the cipher machine created by yours truly, Julan Rai')
print('Please enter the message that you wish to encode:')
message = input()

while any(char.isdigit() for char in message):
    print('Please refrain from using digits in your message. Enter a new message:')
    message = input()

print('This cipher machine works through the Caesar Cipher. Please enter the number that you wish to shift your '
      'letters to:')

shiftNumber = int(input())
while shiftNumber > 25 or shiftNumber < 1:
    print('Please pick a number between 1 and 25:')
    shiftNumber = input()

print('Here is your encoded message:')
print(shifted_letter(shift(msg_pos(message))))
