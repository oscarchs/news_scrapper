#!/usr/bin/env python

from sys import stdin

pagerank = {}
d = 0.85

for line in stdin:
  row = line.rstrip('\n').split()
  nodes = row[0].split(':')
  node_from = nodes[0]
  node_to = nodes[1]
  value = float(row[1])
  if node_from in pagerank.keys():
	  pagerank[node_from] += value
  else:
	  pagerank[node_from] = value

for page in pagerank:
  pagerank[page] = (1.0-d) + d * pagerank[page]
  print ('%s\t%s' % (page, pagerank[page]))

  
