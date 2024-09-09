#
# Dissociated Press
#

import random

# Read a text file and return a list of words
def read_text(fname):
  fd = open(fname, "r")
  wl = [ "." ]
  for s in fd.readlines():
    line = s.rstrip()
    words = line.split()
    for w in words:
      word = w.rstrip(",.':;?!-_\"").lstrip('\'"_').lower()
      wl.append(word)
      if w[-1] == "." and w.lower() != "dr.":
        wl.append(".")
  return wl

# take a list of words, and return set of all n-grams
def find_ngrams(wl, n):
  ngrams = set()
  for i in range (len(wl)-n+1): #n개의 단어로 형성된 n-gram을 생성하기 위한 range.
    ngram = tuple(wl[i : i+n])
    ngrams.add(ngram)
  return ngrams

  raise NotImplementedError

# given a set of ngrams, return a list of ngrams whose first word is "."
def find_starters(ngrams):
  starters = []
  for ngram in ngrams:
    if ngram[0] == ".":
      starters.append(ngram)
  return starters
  raise NotImplementedError

# take set of n-grams, and return a map that maps (n-1)-grams
# to the set of all possible last words
def make_ngram_map(ngrams):
  ngram_map = {}
  for ngram in ngrams:
    key = ngram[:-1] # ngram[start:end] -> from 'start' to 'end-1'(end 값은 리턴 되지 않음!)
    last_word = ngram[-1]
    if key not in ngram_map: #키가 dictionary(i.e. map)에 없으면
      ngram_map[key] = set() #그 키에 대한 빈 집합을 생성 (단어들을 넣기 위해)
    ngram_map[key].add(last_word) # 마지막 단어를 해당 키의 set에 추가.
  return ngram_map
  raise NotImplementedError
 
def print_word(w):
  if w != ".":
    print(" ", end="")
  print(w, end="")

#
# Generate and print a text consisting of count words,
# 
def dissociated_press(fname, n, count):
  words = read_text(fname)
  ngrams = find_ngrams(words, n)
  ngmap = make_ngram_map(ngrams)
  # start with a random n-gram that starts with a "period"
  starters = find_starters(ngrams)
  current = random.choice(starters)
  # skip period at the beginning and print first word without leading space
  print(current[1], end="")
  for w in current[2:]:   
    print_word(w)
  wcount = n
  while wcount < count:
    head = current[1:]                # take last n-1 words printed so far
    choices = ngmap.get(head)         # find n-grams starting with head
    if choices is None:
      print()
      return                          # cannot continue
    w = random.choice(list(choices))  # pick a random word 
    current = head + (w,)
    print_word(w)
    wcount += 1
  print()
  print(ngmap)
  print()

  

if __name__ == "__main__":
  # dissociated_press("kaist.txt", 2, 100)
  # print()
  dissociated_press("independence.txt", 3, 100)
  print()
  # dissociated_press("president.txt", 3, 100)
  # print()
  # dissociated_press("alice.txt", 4, 200)
