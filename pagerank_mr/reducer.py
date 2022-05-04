#!/usr/bin/env python

from sys import stdin

index = {}

for line in stdin:

        row = line.rstrip('\n').split()
		print(row)
        #neighbor = row[1].split(',')
	
        #index[row[0]] = [neighbor,float(row[2])]


#for doc_id in index:
#	print ('%s\t%s' % (doc_id, index[doc_id]))
	

"""

output = {}
for doc_id in index:
	size = len(index[doc_id][0])

	for doc in index[doc_id][0]:
		if doc in output:
			output[doc] += index[doc_id][1]/size
		else:
			output[doc] = index[doc_id][1]/size	

for doc_id in output:
	output[doc_id] = output[doc_id]*0.85 +0.15


#for doc_id in index:
#	if doc_id in output:
#		index[doc_id][1] = output[doc_id]
		
		
for doc_id in output:
	#postings = ','.join(index[doc_id][0])		
	print ('%s\t%s' % (doc_id, output[doc_id]))
"""