#!/usr/bin/env python3

import sys

# らしかったろ,0,0,0,助動詞,*,タ系省略推量形,イ形容詞イ段,らしい,らしかったろ,*,NIL

cache = {}

stopwords = ['UNK', '"']

def process(line):
	for w in stopwords:
		if line.find(w) != -1:
			return

	pos1 = line.rfind(',')
	if pos1 == -1:
		return

	pos2 = line.rfind(',', 0, pos1-1)
	key = line[:pos2]
	kp = key.split(',')
	def process(i):
		item = kp[i]
		if len(item) == 0:
			return '*'
		return item

	key = ','.join(process(x) for x in [0, 1, 2, 3, 4, 5, 7, 6, 8, 9])

	rep = line[pos2+1: pos1]
	features = line[pos1+1:].split(' ')

	cached = cache.get(key, None)
	if cached is None:
		cached = (set(), set())
	reprset, featset = cached
	reprset.add(rep)
	featset.update(features)
	cache[key] = (reprset, featset)



def main():
	with open(sys.argv[1]) as infile:
		for line in infile:
			process(line.strip())

	for k, v in sorted(cache.items(), key=lambda x: x[0]):
		reprset, featset = v
		if "NIL" in featset: 
			featset.remove("NIL")
		reprs = "?".join(sorted(reprset))
		features = " ".join(sorted(featset))
		print(f"{k},{reprs},{features}")

if __name__ == '__main__':
	main()