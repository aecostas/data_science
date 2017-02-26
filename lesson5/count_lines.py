import logging
import sys
import string

from util import logfile

logging.basicConfig(filename=logfile, format='%(message)s',
                                       level=logging.INFO, filemode='w')


def word_count():
    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")
        
        # Your code here
        for word in data:
            word_final = word.translate(None, string.punctuation).lower()
            try:
                word_counts[word_final] += 1
            except KeyError:
                word_counts[word_final] = 1
    print word_counts
                
word_count()
