from collections import OrderedDict
import string

words = list(input())

alpha_dict = OrderedDict()

for i in string.ascii_lowercase:
    alpha_dict[i] = 0

for w in words:
    alpha_dict[w] += 1

print(' '.join([ str(i) for i in alpha_dict.values()]))
