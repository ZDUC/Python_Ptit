import textwrap

t = int(input())
for i in range(t) :
    print(textwrap.shorten(input(), width = 100, placeholder = ''))
