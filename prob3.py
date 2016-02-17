import sys
import multiprocessing

ncores = multiprocessing.cpu_count()

"""
counting each elements by key value granular
"""
def MapReducer(param):
  nama = param[0]
  phone = param[1]
  arr = param[2]
  results = False
  for el in arr:
    els = el.split(" ")
    if len(els) > 1:
      bval = els[0] == nama and els[1] == phone 
      results = results or bval
  return results
"""
read by lines
"""
def readbyline(path):
  word_list = []
  f = open(path, "r")
  for line in f:
    word_list.append(line)
  # print word_list
  return (''.join(word_list)).split("\n")
"""
chunks list
"""
def chunks(lst, n):
  for i in xrange(0, len(lst), n):
    yield lst[i:i+n]

# FUNCTIONS
def initialize(filename):
  global partitioned_text
  text = readbyline(filename)
  partitioned_text = list(chunks(text, len(text) / ncores))
  return partitioned_text

def check_blacklist(_nama,_phone):
  nama = _nama
  phone = str(_phone)
  pool = multiprocessing.Pool(processes=ncores,)
  arrtuples = []
  for part in partitioned_text:
    arrtuples.append((nama,phone,part))
  haystacks = pool.map(MapReducer, arrtuples)
  return any(haystacks)


# MAIN FUNCTION 
if __name__ == '__main__':
  if (len(sys.argv) != 4):
    print "Provide file name input and parameters to search"
    sys.exit(1)
  initialize(sys.argv[1])
  found = check_blacklist(sys.argv[2],int(sys.argv[3]))
  print found
  