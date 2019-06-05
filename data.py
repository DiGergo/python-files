import re
import collections

text = open("data.txt").read().lower()
words = re.findall("\w+", text)
print(collections.Counter(words).most_common(10))