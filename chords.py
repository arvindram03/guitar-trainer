import random
import time
import sys


import fire

class Chord(object):
	chords = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

	def generator(self, timing=4, tempo=1):
		print ('#################')
		print ('Timing =', timing)
		print ('Tempo =', tempo)
		print ('#################\n')
		while True:
			sys.stdout.write('## {} ## '.format(random.choice(self.chords)))
			sys.stdout.flush()
			for i in range(timing):
				time.sleep(10.0/float(tempo))
				sys.stdout.write('{} '.format(i+1))
				sys.stdout.flush()
			sys.stdout.write('\r')



if __name__ == '__main__':
	fire.Fire(Chord)