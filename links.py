#!/usr/bin/python

import sys,csv,numpy as np

#create alphabet matrix and count matrix
string = 'abcdefghijklmnopqrstuvwxyz'
list_string = list(string)
alpha_mat = [['0' for x in xrange(26)] for x in xrange(26)]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] = list_string[i]
for j in range(0,26):
        for i in range(0,26):
                alpha_mat[i][j] += list_string[j]
#for p in range(0,26):
#	print alpha_mat[p]
count_mat = [[0 for x in xrange(26)] for x in xrange(26)]

#take in arguments from command line
file_in = str(sys.argv[1])
file_out = str(sys.argv[2])

#open read and write filestreams for I/O
filestream_in = open(file_in,'r+')
filestream_out = open(file_out,'w')

#read file and grab text, clean up for processing
text = filestream_in.readlines()
for k in range(0,len(text)): 
	text[k] = ''.join(e for e in text[k] if not e.isdigit())
	text[k] = ''.join(f for f in text[k] if f.isalnum())
long_string = ''.join(text)
long_string_char = list(long_string.lower())

#start processing to get counts in alpha table and create karyotype file
for l in range(0,len(long_string_char) - 1):
	temp = long_string_char[l]
	compare = long_string_char[l+1]
	tuple_let = temp + compare
	for m in range(0,26):
		for n in range(0,26):
			if tuple_let == alpha_mat[m][n]:
				#print n,m,tuple_let
				count_mat[m][n] = count_mat[m][n] + 1
for r in range(0,26):
	print count_mat[r]
counter_arr = [0 for x in xrange(26)]
for s in range(0,26):
	for t in range(0,26):
		for u in range(0,count_mat[s][t]):
			counter_arr[t] = counter_arr[t] + 1
			counter_arr[s] = counter_arr[s] + 1
			filestream_out.write(list_string[s] + ' ' + str(counter_arr[s]) + ' ' + str(counter_arr[s]) + ' ' + list_string[t] + ' ' + str(counter_arr[t]) + ' ' + str(counter_arr[t]) + '\n')  
#write output file and close filestreams
filestream_in.close()
filestream_out.close()
