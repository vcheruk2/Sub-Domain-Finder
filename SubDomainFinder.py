# This code needs to be compiled using Admin privileges.
# Upon successful execution of this code it prints the exisiting sub-domains for a given Top-Level domain.

import os

print ""

lst = []
ctr = 0
x = True

hostname = raw_input("Enter the Top level Url : <eg. google.com>")
response = os.system("ping -c 1 " + hostname)

if response == 0:
	while x == True:
		for i in xrange(97,123):
			test = os.system("ping -c 1 "+chr(i)+"."+hostname)
			if test == 0:
				lst.append(chr(i)+"."+hostname)
				ctr += 1
		x = False
	x = True
	while x == True:
		for i in xrange(97,123):
			for j in xrange(97,123):
				test = os.system("ping -c 1 "+chr(i)+chr(j)+"."+hostname)
				if test == 0:
					lst.append(chr(i)+chr(j)+"."+hostname)
					ctr += 1
		x = False
	x = True
	while x == True:
		for i in xrange(97,123):
			for j in xrange(97,123):
				for k in xrange(97,123):
					test = os.system("ping -c 1 "+chr(i)+chr(j)+chr(k)+"."+hostname)
					if test == 0:
						lst.append(chr(i)+chr(j)+chr(k)+"."+hostname)
						ctr += 1
		x = False
	x = True
	while x == True:
		for i in xrange(97,123):
			for j in xrange(97,123):
				for k in xrange(97,123):
					for l in xrange(97,123):
						test = os.system("ping -c 1 "+chr(i)+chr(j)+chr(k)+chr(l)+"."+hostname)
						if test == 0:
							lst.append(chr(i)+chr(j)+chr(k)+chr(l)+"."+hostname)
							ctr += 1
		x = False
else:
	print "Top level Hostname is down, Exiting the Program"

print ""
print "There are "+ctr+" Valid Sub-Level domains for "+hostname+" and they are"
print lst
print ""
