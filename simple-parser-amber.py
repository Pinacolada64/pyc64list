class CodeParser:
    keywords = ('if', 'then', 'for', 'next', 'print')
    txtptr = 0
    line = ''
    debug = True

    def find_keyword(self):
        if self.debug:
            self.display_pointer
        if self.line[self.txtptr:self.txtptr + 1] == ' ':
            self.txtptr += 1
            return '[space]'
        result = None
        result_length = 0
        for keyword in self.keywords:
            length = len(keyword)  # for comparing length of keyword & updating txtptr position
            # Found a keyword, set a result.
            if self.line[self.txtptr:self.txtptr + length] == keyword:
                result = keyword
                result_length = length
            # Did not find a result, keep looking
            else:
                continue
        if result:
            self.txtptr += result_length
            return result
        elif self.debug:
            print('No keywords found at position: {}'.format(self.txtptr))
            print('Instead, found "{}"'.format(self.line[self.txtptr:self.txtptr + 1]))
            print("Skipping ahead to next keyword.")
            # Look for next space, then advance pointer there.
        while self.txtptr < len(self.line):
            if ' ' not in self.line:
                self.txtptr += 1
            else:
                self.txtptr += 1
                return '[skip]'

    def parse_line(self):
        while self.txtptr < len(self.line):
            result = self.find_keyword()
            print('Found end of "{}" keyword at position {}.'.format(result, self.txtptr))
            # reached end of line?
            if self.txtptr == len(self.line):
                print "end of line"
                self.txtptr = 0
                break
        return

    def display_pointer(self, num):
        """Advance txtptr by <num> characters"""
        if self.txtptr < len(self.line):
            self.txtptr += num
            print("CodeParser pointer at: {}".format(self.txtptr))

test = CodeParser()
# match position:
# (0-based)            1111111111222
#            01234567890123456789012
test.line = "if then for next print"
test.parse_line()

test.line = "bad token. print no do-not."
test.parse_line()

# desired output (I think)
# txtptr should always end up 1 char after match,
# unless at end of line, in which case it should return None

# found kw: 'if'
# txtptr at 2
# found kw: ' '
# txtptr at 3
# found kw: 'then'
# txtptr at 7
# found kw: ' '
# txtptr at 8
# found kw: 'for'
# txtptr at 11
# found kw: ' '
# txtptr at 12
# found kw: 'next'
# txtptr at 16
# found kw: ' '
# txtptr at 17
# found kw: 'print'
# txtptr at 22
# end of line
# this is a nonsensical BASIC line, but a test of keeping track where the
# parser is in the line, and capturing individual tokens, including spaces

# In a sense, 'find' is the opposite of the [] operator. Instead of taking
# an index and extracting the corresponding character, it takes a character
# and finds the index where that character appears. If the character is not
# found, the function returns -1.

# This is the first example we have seen of a return statement inside a loop.
# If word[index] == letter, the function breaks out of the loop and returns
# immediately.

# If the character doesn't appear in the string, the program exits the loop
# normally and returns -1.

# This pattern of computation--traversing a sequence and returning when we
# find what we are looking for--is called a search.

# from http://www.greenteapress.com/thinkpython/html/thinkpython009.html
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
            index = index + 1
        return -1

# Amber(#3) yaps. If you want the /beginning/ of the token position, you'll need to save txtptr and report beginning position after advancing txtptr to next position.
# Amber(#3) yaps. Maybe store in self.start_token_position ?
# Amber(#3) yaps. Also, using l and k as variables made things much more difficult, especially confusing l and 1.
# Amber(#3) usually defaults to "for each in thing:"
# Amber(#3) yaps. Then I know I'm iterating through the thing and getting each part.
