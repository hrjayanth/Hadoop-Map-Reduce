import sys

current_bowler = None
current_bowler_wickets = 0

for line in sys.stdin:
    line = line.strip()
    bowler, wickets = line.split('\t')

    try:
        wickets = int(wickets)
        bowler = bowler.strip()
    except ValueError:
        continue

    if current_bowler == bowler:
        current_bowler_wickets += wickets
    else:
        if current_bowler:
            print('{}\t{}'.format(current_bowler, current_bowler_wickets))
        current_bowler = bowler
        current_bowler_wickets = wickets

if current_bowler == wickets:
    print('{}\t{}'.format(current_bowler, current_bowler_wickets))