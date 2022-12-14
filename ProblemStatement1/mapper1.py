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
    print('{}\t{}'.format(batsman, batsman_runs))