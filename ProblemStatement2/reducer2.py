import sys

scores=[]
for line in sys.stdin:
    line = line.strip()
    batsman,batsman_runs = line.split('\t')
    try:
        batsman_runs = int(batsman_runs)
        batsman = batsman.strip()
    except ValueError:
        continue
    scores.append([batsman_runs, batsman])

top_N=sorted(scores,reverse=True)[0:10]

for t in top_N:
    print('{}\t{}'.format(t[1], t[0]))
