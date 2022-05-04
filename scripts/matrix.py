#!/usr/bin/env python

from sys import stdin
import re

matrix = []
for line in stdin:
  row = line.rstrip('\n').split()  
  documents = row[1]
  list_documents = documents.split(',')
  tmp = [re.sub(':[0-9]{1,999}', '', document) for document in list_documents]
  matrix.append(tmp)


adjacency_list = {}
for row in matrix:
  for element in row:    
    pivot = element    
    for neighbor in row:
      if pivot!=neighbor:
        key = pivot + ':' + neighbor
        adjacency_list[key] = {'from': pivot, 'to': neighbor}

for key in adjacency_list:
  print('%s\t%s' % (adjacency_list[key]["from"], adjacency_list[key]["to"]))
