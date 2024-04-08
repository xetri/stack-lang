import sys
from collections import deque

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} <filename>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    source = f.read()

    tokens : deque[str] = deque()
    
    for tks in source.split("\n"):
        for tk in tks:
            for t in tk.split(" "):
                if len(t):
                    tokens.append(t)
    
    stack : deque[int] = deque()
    
    for t in tokens:
        try:
            if t == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a) 
            elif t == '%':
                a = stack.pop()
                b = stack.pop()
                stack.append(b % a)
            elif t == '.':
                print(stack.pop())
            elif t == ',':
                a = input()
                stack.append(int(a))
            else:
                stack.append(int(t))
        except ValueError:
            print(f"Only integers are valid operand, got '{t}'", file=sys.stderr)

