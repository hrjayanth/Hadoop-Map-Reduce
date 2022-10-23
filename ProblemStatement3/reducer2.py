import sys

current_batsman = None
count = 0

for line in sys.stdin:
    line = line.strip()
    batsman, run = line.split('\t')

    if current_batsman == batsman:
        count = count+1
    else:
        if current_batsman:
            print (current_batsman, '\t' ,count)
        current_batsman = batsman
        count = 1

if current_batsman == batsman:
    print (current_batsman, '\t' ,count)
