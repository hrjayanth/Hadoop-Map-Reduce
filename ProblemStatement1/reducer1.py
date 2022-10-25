import sys

current_batsman = None
current_batsman_runs = 0

for line in sys.stdin:
    line = line.strip()
    batsman, run = line.split('\t')

    try:
        run = int(run)
    except ValueError:
        continue

    if current_batsman == batsman:
        current_batsman_runs += run
    else:
        if current_batsman:
            print('{}\t{}'.format(current_batsman, current_batsman_runs))
        current_batsman = batsman
        current_batsman_runs = run

if current_batsman == batsman:
    print('{}\t{}'.format(current_batsman, current_batsman_runs))