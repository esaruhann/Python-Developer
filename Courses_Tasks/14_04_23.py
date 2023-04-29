"""
import numpy as np

ary = np.zeros(27)
counter = 0
try:
    f = open("C:\\Users\edanu\Downloads\mbox-short.txt")
    for line in f:
            if line.startswith('From'):
                second_index = line.split()[1]

                if second_index[1] not in d:
                    d[words[1]] = 1       
                else:
                    d[words[1]] += 1 


except:
    print("File is not found")
firt = ary[0]
ary2 = []

for i in range(1, len(ary)):
    if firt != ary[i]:
        ary2.append(firt)
    firt = ary[i]
print("Mail adresses: ", ((ary2)))
print("Total mail: ", len(ary2))


# count the frequency of each email address
email_freq = {}
for email in ary:
    if email in email_freq:
        email_freq[email] += 1
    else:
        email_freq[email] = 1

# print the results
print("Email frequencies:")
for email, freq in email_freq.items():
    print(email, ": ", freq)

print("most frequent email sender ", max(
    email_freq, key=lambda email: email_freq[email]))
"""
d = dict()                      
fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        if words[1] not in d:
            d[words[1]] = 1       
        else:
            d[words[1]] += 1      

print(d) 

max_value = max(d.values())
key = max(d, key=d.get)
print(key + ': ' + str(max_value))


import re
# from course
p = re.compile('\w+')
p.findall("eda")

txt = "eda"
x = re.split("\s",txt)

from re import split

x = re.search(r"")
x.span()
x.group()

