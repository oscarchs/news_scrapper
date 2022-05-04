#!/usr/bin/env python

from sys import stdin

document_list = {}
document_output = {}

for line in stdin:
  row = line.rstrip('\n').split()
  node_from = row[0]
  node_to = row[1]
  tmp_key = node_from + ':' + node_to
  document_output[tmp_key] = node_from
  if node_from in document_list.keys():
    document_list[node_from].append(node_to)
  else:
    document_list[node_from] = [node_to]

N = len(document_list)
pr = float(1.0 / N)

for document in document_output:
  ci = len(document_list[document_output[document]])
  document_output[document] = float(pr/ci)
  print ('%s\t%s' % (document, document_output[document]))

