#!/usr/bin/python

# A list of Commodore 64 BASIC token values
tokens = (0x20, 0x80, 0x81, 0x82)

# A list of Commodore 64 BASIC keywords
keywords = (' ', 'end', 'for', 'next')

# An empty dictionary to start
mytable = {}

# Loading mytable full of goodness
for each_index, each in enumerate(tokens):
    mytable[keywords[each_index]] = each

def keyword_to_token(kw):
    """Given 'keyword', return value of keyword"""
    try:
        return mytable[kw]
    except Exception as error:
        print('Caught this error: ' + repr(error))

# Testing the keyword_to_token method:

print mytable  # Debug - shows mytable on run

print keyword_to_token('end') # should return 128 (0x81)

print keyword_to_token('for')
print keyword_to_token('next')
print keyword_to_token('bad_token')
