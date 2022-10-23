import sys

for line in sys.stdin:
    line = line.strip()
    batsman,batsman_runs = line.split('\t')

    try:
        batsman_runs = int(batsman_runs)
        batsman = batsman.strip()
        matchId, batsman = batsman.split('_')
    except ValueError:
        continue

    if(batsman_runs >= 100):
        print(batsman, '\t', batsman_runs)
