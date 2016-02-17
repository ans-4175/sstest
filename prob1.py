import sys
from multiprocessing import Pool

"""
counting each elements by key value granular
"""
def Map(arr): 
  results = []
  for el in arr:
    results.append((el, 1))
  return results
"""
grouping by key
"""
def Grouping(arr):
  bucket = {}
  for seq in arr:
    for s in seq:
      try:
        bucket[s[0]].append(s)
      except KeyError:
        bucket[s[0]] = [s]
  return bucket
"""
reduce by summing occurences
"""
def Reduce(Maparr):
  return (Maparr[0], sum(kv[1] for kv in Maparr[1]))
"""
read by lines
"""
def readbyline(path):
  word_list = []
  f = open(path, "r")
  for line in f:
    word_list.append (line)
  return (''.join(word_list)).split()
"""
chunks list
"""
def chunks(lst, n):
  for i in xrange(0, len(lst), n):
    yield lst[i:i+n]
"""
Sort by value ascending
"""
def kv_sort (a, b):
  if int(a[0]) > int(b[0]):
    return 1
  elif int(a[0]) < int(b[0]):
    return -1
  else:
    return 1
 
if __name__ == '__main__':
  if (len(sys.argv) != 3):
    print "Provide file name input and output"
    sys.exit(1)

  nthread = 4
  text = readbyline(sys.argv[1])
  pool = Pool(processes=nthread,)
  partitioned_text = list(chunks(text, len(text) / nthread))
  splitted_text = pool.map(Map, partitioned_text)
  groupped_text = Grouping(splitted_text)
  sorted_text = pool.map(Reduce, groupped_text.items())
  sorted_text.sort(kv_sort)

  with open(sys.argv[2], "ab") as myfile:
    for kv in sorted_text:
      for i in range(0,kv[1]):
        myfile.write(kv[0])
        myfile.write("\n")