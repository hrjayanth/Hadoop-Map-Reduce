import sys

current_fielder = None
current_fielder_catches = 0

for line in sys.stdin:
    line = line.strip()
    fielder, catches = line.split('\t')

    try:
        catches = int(catches)
    except ValueError:
        continue

    if current_fielder == fielder:
        current_fielder_catches += catches
    else:
        if current_fielder:
            print('{}\t{}'.format(current_fielder, current_fielder_catches))
        current_fielder = fielder
        current_fielder_catches = catches

if current_fielder == fielder:
    print('{}\t{}'.format(current_fielder, current_fielder_catches))