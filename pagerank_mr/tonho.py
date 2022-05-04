#!/usr/bin/env python

from sys import stdin
import re
#import numpy as np
index = {}
#input
#libertad	9993:1,9995:1
#arequipa	9994:1
#retrocedi	9998:1

"""
{
    libertad: [9993:1, 9995:1]
}

{
    9993: 0.2434,

}
"""

universe = set()

total_adj = {}


doc_id_incidence = {}


for line in stdin:
  row = line.rstrip('\n').split()
    
  #asignando lista de postlist a cada keyword
  #counter[key] = counter[key] + value if data[0] in counter.keys() else value
  keyword = row[0]
  documents = row[1]
  #print(documents)
  documents = re.sub(':[0-9]', '', documents)
  print(documents)
  #print(type(keyword))
  #print(type(documents))
  #index[ keyword ] = index[ keyword ].append(documents) if keyword in index.keys() else [ documents ]

  #print(index)
  #if row[0] in index:
  #  index[row[0]].append(row[1])
  #else:   
  #  index[row[0]] = [row[1]]

  #for clave, valor in diccionario.items():
  #  print(clave, '\t', valor)
  
"""
        for doc_id in index[row[0]]:
            doc = doc_id.split(',')
            for ids in doc:
                if row[0] in total_adj:
                    total_adj[row[0]].append(ids.split(':')[0])

                else:
                    total_adj[row[0]] = [ids.split(':')[0]]
                universe.add(ids.split(':')[0])
"""        
"""
            
for doc_id in universe:
    for key in total_adj:
        if doc_id in total_adj[key]:
            # hallar de todo el array
            total_per_doc = len(total_adj[key])-1 if len(total_adj[key]) > 1 else len(total_adj[key])
            if doc_id in doc_id_incidence:
                doc_id_incidence[doc_id] += total_per_doc
            else:
                doc_id_incidence[doc_id] = total_per_doc

distribution = float(1.0/len(universe))
for doc_id in universe:
    for key in total_adj:
        if doc_id in total_adj[key]:
            for doc in total_adj[key]:
                if doc != doc_id:
                    doc_page_rank = distribution/doc_id_incidence[doc] if doc in doc_id_incidence else 0
                    print ('%s\t%s' % (doc_id, doc_page_rank))
"""


"""
#!/usr/bin/env python3
import sys

counter = {}
d = 0.85

for line in sys.stdin:
    line = line.strip()         
    print(line)
    
    line = line.strip()         
    data = line.split('\t')
    key = data[0]    
    value = float(data[1])
    counter[key] = counter[key] + value if data[0] in counter.keys() else value

for key, value in counter.items():
    score = (1.0-d) + d * value
    print(key,  score)
    """
#printf "a\tb\t0.25\t2\na\tc\t0.25\t3\nb\ta\t0.25\t2\nb\tc\t0.25\t3\nc\ta\t0.25\t2\nc\tb\t0.25\t2\nc\td\t0.25\t1\nd\tc\t0.25\t3\n" | ./reducer_mierda.py    