import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other!'

match = re.search(patterns[0],text)

split_term='@'

email = 'user@gmail.com'

print(re.split(split_term,email))

print(match.start())

print(re.findall('match','test phrase match in middle match'))


def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string! But it has punctuation. How can we remove it ?'

test_patterns=['[^!.?]+']

multi_re_find(test_patterns,test_phrase)