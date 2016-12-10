# Password Generator Distribution Analyzer
# this script illustrates the uniform distribution of sampling

import random
import pandas
from collections import Counter
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"
upperalphabet = alphabet.upper()
special = "@!#$%&*<=>?"
abs2 = alphabet + upperalphabet
all_char = abs2 + special

pw_len = 20000
pwlist = []

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

letter_counts = Counter(pwstring)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')
plt.show()
