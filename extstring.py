#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Markus Thilo'
__version__ = '0.0.1_2024-10-10'
__license__ = 'GPL-3'
__email__ = 'markus.thilo@gmail.com'
__status__ = 'Testing'
__description__ = 'Extended methods for strings'

from itertools import chain

class ExtString(str):
	'''Extended methods for strings'''

	def starts_with_iter(self, candidates):
		'''Extends startswith to an iterable argument'''
		if isinstance(candidates, str):
			if self.startswith(candidates):
				return candidates
			else:
				return
		for candidate in candidates:
			if self.startswith(candidate):
				return candidate
		return

	def join_tolerant(self, iterable):
		'''Join iterable to list but be tolerant to missing items'''
		return self.join([f'{str(item).strip()}' for item in iterable if item])

	def sequence(self, max_len):
		'''Split string to sequences following punctuation'''
		sequences = list()
		leftover = self
		while leftover:
			if len(leftover) <= max_len:
				sequences.append(leftover)
				break
			for delimiter in '.!?:;()[]{}|#@\',/\\\n \0':
				if delimiter == '\0':
					sequences.append(leftover[:max_len])
					leftover = leftover[max_len:]
					break
				splitted = leftover.split(delimiter, 1)
				if len(splitted) > 1 and len(splitted[0]) <= max_len:
					sequences.append(f'{splitted[0].strip()}{delimiter}')
					leftover = splitted[1].strip()
					break
		return sequences
