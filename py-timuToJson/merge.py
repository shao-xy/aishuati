#!/usr/bin/env python3

import sys
import os
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('questions', help='题目文件')
	parser.add_argument('keys', help='答案文件')
	parser.add_argument('output', help='输出文件')
	args = parser.parse_args()
	return args.questions, args.keys, args.output

def main():
	questions_path, keys_path, output_path = parse_args()

	# Ignore IOErrors
	fin_questions = open(questions_path, 'r')
	fin_keys = open(keys_path, 'r')
	fout = open(output_path, 'w')
	keys_cnt = 0
	warned = False
	while True:
		line = fin_questions.readline()
		if not line:	break

		if line != '\n' or warned:
			fout.write(line)
		else:
			key_line = fin_keys.readline()
			if not key_line:
				if not warned:
					print(f'\n警告：答案文件中，只有{keys_cnt}行，题目文件后续空行均保留。')
					print('\n警告：正在复制剩余行')
					warned = True
				key_line = '\n'
			else:
				keys_cnt += 1
			fout.write(key_line)

	if fin_keys.read():
		print(f'警告：答案文件中{keys_cnt}行之后被舍弃。')

	fin_questions.close()
	fin_keys.close()
	fout.close()

if __name__ == '__main__':
	sys.exit(main())
