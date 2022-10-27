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

    if(extra_type != 'NA'):
        print('{}\t{}'.format(matchId + '_' + bowler, extras_run))