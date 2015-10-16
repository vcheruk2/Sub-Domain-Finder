

import os
import subprocess
import commands
import sys
import re

lst = []
temp = []
add = []
list=[]

# Get the input from the user (Website)
data = raw_input("Enter a website here ")

x = os.popen("nslookup "+data).read()

fo = open("some.txt","rw+")
fo.write(x)


fo = open("some.txt","r")
for line in fo:
    if re.match("Address: ", line):
        lst.append(line)

print lst
length = len(lst)

print "length of the list is ", length
#print lst[0]


for i in xrange(0,length):
	ar=lst[i]
	
	temp.append(ar[9:])
	
	print temp

print "Add[0] is "+temp[0]

y = os.popen("host "+temp[0]).read()
print y
foo= open("out.txt","rw+")
foo.write(y)

foo= open("out.txt","r")
for l in foo:
	for part in l.split():
            if data in part:
                print "Yes"

open("some.txt",'w').close()
