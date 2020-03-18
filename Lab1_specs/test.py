def ss(x):
    i = 0
    if x < 0:
        return -1
    else:
        start = 1
        while (start * start - x) > 1e-9 or ((start * start - x) < - 1e-9):
            start = (start + x / start) / 2.0
            i = i + 1
            # print(i, start)
        return int(start)


def myfind(s, char):
    pos = s.find(char)
    if pos == -1: # not found
        return len(s) + 1
    else:
        return pos

def next_tok(s): # returns tok, rest_s
    if s == '':
        return (None, None)
    # normal cases
    poss = [myfind(s, ' '), myfind(s, '['), myfind(s, ']')]
    min_pos = min(poss)
    if poss[0] == min_pos: # separator is a space
        tok, rest_s = s[ : min_pos], s[min_pos+1 : ] # skip the space
        if tok == '': # more than 1 space
            return next_tok(rest_s)
        else:
            return (tok, rest_s)
    else: # separator is a [ or ]
        tok, rest_s = s[ : min_pos], s[min_pos : ]
        if tok == '': # the next char is [ or ]
            return (rest_s[:1], rest_s[1:])
        else:
            return (tok, rest_s)

str_tree = '''
1 [2 [3 4       5          ] 
   6 [7 8 [9]   10 [11 12] ] 
   13
  ]
'''
str_tree = str_tree.replace('\n','')
print(str_tree)
next_tok(str_tree)
x = [1,2,3,4,2]
print(x.index(2))
