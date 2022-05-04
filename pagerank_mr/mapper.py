#!/usr/bin/env python

from sys import stdin

index = {}

for line in stdin:
  row = line.rstrip('\n').split()
  keyword = row[0]
  list_documents = ','.join([row[1]])
  index[keyword] = list_documents

for word in index:
  print ('%s\t%s\t%d' % (word, index[word],1))



                