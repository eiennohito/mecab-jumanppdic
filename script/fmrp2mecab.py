#!/usr/bin/env python3

import sys

dictionary = {}

# して_して_する_動詞_*_サ変動詞_タ系連用テ形
# あいまいで,0,0,0,*,ダ列タ系連用テ形,ナ形容詞,ダ列タ系連用テ形,あいまいだ,曖昧だ/あいまいだ,

def main():



	with open(sys.argv[1]) as infile:
		for line in infile:
			line = line.strip()
			comment = line.find(' #')
			if comment != -1:
				line = line[:comment]
			words = line.split(' ')
			for w in words:
				fields = w.split('_')
				otherfields = [
					fields[3],
					fields[4],
					fields[5],
					fields[6],
					fields[2],
					fields[1]
				]
				print(f"{fields[0]}\t{','.join(otherfields)}")
			print('EOS')


if __name__ == '__main__':
	main()