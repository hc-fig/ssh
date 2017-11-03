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
    sys.exit(1)
else:
    allargs = reduce(lambda s1, s2: s1 + ' ' + s2, sys.argv[1:])


results = map(lambda m : (m,0)[0:1] + commands.getstatusoutput("ssh "+m+".cs.haverford.edu "+allargs),
              machines)

good = filter(lambda m_r_o: m_r_o[1] == 0, results)
bad  = filter(lambda m_r_o: m_r_o[1] != 0, results)

def print_with_name(prefix, m_r_o):
	print
	for line in m_r_o[2].split("\n"):
		print prefix + m_r_o[0].rjust(maxlen) + ": " + line

for m_r_o in bad:
	print_with_name("Got an error on ", m_r_o)
for m_r_o in good:
	print_with_name("", m_r_o)
