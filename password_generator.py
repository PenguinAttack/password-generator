# Password Generator
# this script will generate a random password and save it to a text file.
# user inputs (1) name of text file and (2) username

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
upperalphabet = alphabet.upper()
special = "@!#$%&*<=>?"
abs2 = alphabet + upperalphabet

pw_len = 8 # length of password
pwlist = []

# Name of text file your username and password will be saved to
response = raw_input("Please enter name for text doc ")
filetype = ".txt"
#dir = "/directory/" # to add a directory to save your file edit this line and the one below it
name = response+filetype # change to dir+response+filetype
response_2 = raw_input("Please enter username ")

# Generate password
for i in range(pw_len//3):
    pwlist.append(alphabet[random.randrange(len(alphabet))])
    pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
    pwlist.append(special[random.randrange(len(special))])
    pwlist.append(abs2[random.randrange(len(abs2))])
    pwlist.append(str(random.randrange(10)))
    pwlist.append(alphabet[random.randrange(len(alphabet))])
    pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
for i in range(pw_len-len(pwlist)):
    pwlist.append(alphabet[random.randrange(len(alphabet))])

random.shuffle(pwlist)
pwstring = "".join(pwlist)

file = open(name, "w")
file.write(response)
file.write('\n')
file.write(response_2)
file.write('\n')
file.write(pwstring)
file.close()

print(name)
print(response_2)
print(pwstring)

