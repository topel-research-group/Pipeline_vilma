#!/usr/bin/env python3

import sys

contig_name = sys.argv[1]
contig_length = int(sys.argv[2])
blast_pos = open(sys.argv[3], "r")
pos = []

# Create a list of the contig length, 
# and give every position the value zero.
for x in range(contig_length):
	pos.append(0)

# Update the list with the blast result
for position in blast_pos.readlines():
	pos[int(position.split("\t")[1]) - 1] = 1

# Finaly print the result to screen
base = 1
for position in pos:
	print(contig_name + "\t" + str(base) + "\t" + str(position))
	base += 1
