import sys
import multiprocessing

ncores = multiprocessing.cpu_count()
core_multipliers = 1024

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
  if (len(sys.argv) != 2):
    print "Provide file name input"
    sys.exit(1)

  text = readbyline(sys.argv[1])
  splitfile = sys.argv[1].split(".")
  pool = multiprocessing.Pool(processes=ncores,)
  idealchunks = (len(text) / (ncores*core_multipliers))
  numchunks = idealchunks if (idealchunks > 0) else len(text)
  partitioned_text = list(chunks(text, numchunks))
  splitted_text = pool.map(Map, partitioned_text)
  groupped_text = Grouping(splitted_text)
  sorted_text = pool.map(Reduce, groupped_text.items())
  sorted_text.sort(kv_sort)

  with open(splitfile[0]+".out", "w+") as myfile:
    for kv in sorted_text:
      for i in range(0,kv[1]):
        myfile.write(kv[0])
        myfile.write("\n")