#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Markus Thilo'
__version__ = '0.0.1_2024-09-26'
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
				return None
		for candidate in candidates:
			if self.startswith(candidate):
				return candidate
		return None

	def join_tolerant(self, iterable):
		'''Join iterable to list but be tolerant to missing items'''
		return self.join([f'{str(item).strip()}' for item in iterable if item])

	def sequence(self, max_len):
		'''Split string to sequences following punctuation'''
		def devide(string):
			for delimiter in '.!?:;()[]{}|,\n ':
				splitted = string.split(delimiter, 1)
				if len(splitted) == 1:
					continue
				if len(splitted[0]) <= max_len:
					return f'{splitted[0]}{delimiter}', splitted[1]
			return string[:max_len], string[max_len:]
		if len(self) <= max_len:
			return [self]
		raw_sequences = list()
		leftover = self
		while leftover:
			good, leftover = devide(leftover)
			raw_sequences.append(good)
		clean_sequences = [raw_sequences[0].strip()]
		for raw in raw_sequences[1:]:
			clean = raw.strip()
			if len(clean_sequences[-1])+len(clean) > max_len:
				clean_sequences.extend([clean_sequences[-1], clean])
			else:
				clean_sequences.append(f'{clean_sequences[-1]}{clean}')
		return clean_sequences
