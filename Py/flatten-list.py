
alist = [1, 2, 3]
alist = [[11, 21, 30], [19, 63, 71], [81, 99]]

[element for sublist in alist for element in sublist]

import itertools

list(itertools.chain(*alist))
 
