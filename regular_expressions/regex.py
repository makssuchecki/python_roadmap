import re
# re.match() Function
# attempts to match RE pattern at the start of string with optional flags
# re.match(pattern, string, flags=0)

# re.search() Function
# searches for first occurence of RE pattern within the string, with optional flags
# re.search(pattern, string, flags=0)

# re.findall() Function
# returns all non-overlapping matches of pattern in string
# re.findall(pattern, string, flags=0)

# re.sub() Function
# replaces all occurences of the RE pattern in string with repl
# re.sub(pattern, repl, string, max=0)

# re.compile() Function
# compiles a regular expression pattern into a regular expression object
# re.compile(pattern, flags=0)

# re.finditer() Function
# returns an iterator yielding match objects over all non-overlapping matches for the RE pattern in string
# re.finditer(pattern, string, flags=0)

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
if match:
    print('found', match.group())
else:
    print('did not find')


match = re.search(r'iii', 'piiig') # found
match = re.search(r'igs', 'piiig') # not found 

match = re.search(r'..g', 'piiig') # found

match = re.search(r'\d\d\d', 'p123g') # found
match = re.search(r'\w\w\w', '@@abcd!!') # found

match = re.search(r'^b\w+', 'foobar') # not found
match = re.search(r'b\w+', 'foobar') # found

# Email examples
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())

match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))

# Find all
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
    print(email)


tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
for tuple in tuples:
    print(tuple[0])
    print(tuple[1])


# Raw strings
normal="Hello\nWorld"
print(normal)

raw=r"Hello\nWorld"
print(raw) 

# Metacharacters
# . ^ $ * + ? { } [ ] \ | ( )