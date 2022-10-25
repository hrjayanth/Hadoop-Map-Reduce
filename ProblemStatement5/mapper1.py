import sys

# -- IPL Match Data
# matchId
# innings
# overs
# ballnumber
# batsman
# bowler
# nonStriker
# extra_type
# batsman_run
# extras_run
# total_run
# non_boundary
# isWicketDelivery
# player_out
# kind
# fielders_involved
# BattingTeam

for line in sys.stdin:
    line = line.strip()
    matchId,innings,overs,ballnumber,batsman,bowler,nonStriker,extra_type,batsman_runs,extras_run,total_run,non_boundary,isWicketDelivery,player_out,kind,fielders_involved,BattingTeam = line.split(',')

    if isWicketDelivery == '1':
        if kind == 'caught':
            print('{}\t{}'.format(fielders_involved, 1))
        elif kind == 'caught and bowled':
            print('{}\t{}'.format(bowler, 1))
