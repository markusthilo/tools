#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Markus Thilo'
__version__ = '0.0.1_2024-09-25'
__license__ = 'GPL-3'
__email__ = 'markus.thilo@gmail.com'
__status__ = 'Testing'
__description__ = 'Extended methods for strings'

class ExtString(str):
	'''Extended methods for strings'''

	@staticmethod
	def _deitter(*args):
		'''Return flattened list from iterable arguments'''
		flat = list()
		try:
			for arg in args:
				print('DEBUG', flat, arg)
				flat.extend(ExtString._deitter(arg))
		except:
			return list(args)
		return flat

	def startswith(self, *candidats):
		'''Extends startswith to an iterable argument'''
		if isinstance(candidats, str):
			return string.startswith(candidats)
		for candidate in candidats:
			if string.startswith(check):
				return candidate
		return None

	def join(self, iterable):
		'''Join iterable to list but be tolerant to missing items'''
		return self.join([f'{item.strip()}' for item in iterable if item])

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
