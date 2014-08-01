import sys
import random

def n_tuples(text, n):
    tuples = []
    for i in xrange(len(text) - n + 1):
        tuples.append(tuple(text[i:i+n]))
    return tuples

def generate_mapping(tuples):
    mapping = {}
    for tup in tuples:
        short_tup = tup[:-1] # All but last elt
        if short_tup not in mapping:
            mapping[short_tup] = []
        mapping[short_tup].append(tup[-1])
    return mapping
    
def gen_text(text, length, n, *mappings):
    tuples = n_tuples(text, n)
    mapping = {}
    for m in mappings:
        mapping = dict(mapping.items() + m.items()) # merge dictionaries
    seed = random.choice(mapping.keys())
    random_text = seed
    while len(random_text) < length:
        tuple_sized_slice = random_text[-(n-1):] # The last n-1 elts of tuple_sized_slice
        next_word = random.choice(mapping[tuple_sized_slice])
        random_text += (next_word,) # Singleton tuple
    return " ".join(random_text)

if len(sys.argv) > 1:
    TEXT = open(sys.argv[1], 'r').read()
    WORDS = TEXT.split(" ")
    books_to_gen_from = sys.argv[1:]
    length = int(raw_input("Length? "))
    n = int(raw_input("n? "))
    book_mappings = []
    for book in books_to_gen_from:
        book = open(book, "r").read().split(" ")
        book_tuples = n_tuples(book, n)
        book_map = generate_mapping(book_tuples)
        book_mappings.append(book_map)
    print gen_text(WORDS, length, n, *book_mappings)
else:
    print "Please include source files as command line arguments."
