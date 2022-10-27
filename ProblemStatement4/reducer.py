import sys

current_matchId_bowler = None
current_extras = 0

for line in sys.stdin:
    line = line.strip()
    matchId_bowler, extras = line.split('\t')
    try:
        extras = int(extras)
    except ValueError:
        continue

    if current_matchId_bowler == matchId_bowler:
        current_extras += extras
    else:
        if current_matchId_bowler:
            matchId, bowler = matchId_bowler.split('_')
            print('{}\t{}\t{}'.format(matchId, bowler, current_extras))
        current_matchId_bowler = matchId_bowler
        current_extras = extras

if current_matchId_bowler == matchId_bowler:
    matchId, bowler = matchId_bowler.split('_')
    print('{}\t{}\t{}'.format(matchId, bowler, current_extras))