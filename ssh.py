#!/usr/bin/python

import commands
import sys

machines = ["church", "turing",
            "blum", "lovelace", "cook",   "hopper", "dean",
            "yao",  "liskov",   "church", "easley", "kruskal"
            "ziff", "snake", "sherri", "terri",
            # "kodos", "kang", "mcbain"
	    ]
maxlen = max(map(len, machines))


if len(sys.argv) < 2:
    print "usage: ", sys.argv[0], " command-for-remote-execution"
    sys.exit(1) #if user gives invalid input, program will exit with error
else:
    allargs = reduce(lambda s1, s2: s1 + ' ' + s2, sys.argv[1:])
	#allargs is a string of all the commands concatenated together and separated by spaces 


results = map(lambda m : (m,0)[0:1] + commands.getstatusoutput("ssh " + m + ".cs.haverford.edu " + allargs),
              machines)

#alter ssh line to be closer to
#"ssh " + username@

# NOTE: our program should ask for the user's username and password as arguments
# OR we can do the following

'''
import getpass
pass = getpass.getpass()
the_pass = getpass.getpass()
'''

#map - execute all commands on each machine
#(m,0)[0:1] - makes the machine name into a tuple
# we can replace (m,0)[0:1] with just (m,)
#ex. 'easley' becomes ('easley',)

#commands.getstatusoutput("") 
#via a tuple, tells if command was successfully executed (0 indicates success)
#and executes the string in the parentheses

#returns a list of tuples, each containing the machine name, if the command execution was successful, and the commands executed
#ex of a tuple: ('easley', 0, "some commands")


good = filter(lambda m_r_o: m_r_o[1] == 0, results)
# good is a list of tuples that reported success (0)
bad  = filter(lambda m_r_o: m_r_o[1] != 0, results)
# good is a list of tuples that failed (not 0)

def print_with_name(prefix, m_r_o):
	print
	for line in m_r_o[2].split("\n"):
		print prefix + m_r_o[0].rjust(maxlen) + ": " + line
		
#rjust - right justify with maxlen to make it nicely formatted!
#prefix is below -"Got an error on" or ""

# m_r_o[2] is the output of the tuple
#m_r_o[2].split("\n") -splits the output at each newline (\n)
#each "line" or string resulting from the split 
# m_r_o refers to each tuple (machine, result, output)

for m_r_o in bad:
	print_with_name("Got an error on ", m_r_o)
for m_r_o in good:
	print_with_name("", m_r_o)
