import random
import sys
import math
from BJ_Objects import *
import BJ_Strat1, BJ_Strat2, BJ_Strat3, BJ_Strat4

print('***Welcome to Sam\'s Blackjack Table***\n')
print('This simulator will run X games under 4 different player strategies.  Player starts out with $1,000, making $25 bets.  The strategies are as follows:\n\n')
print('Strategy 1 - Standard Play: Player\'s goal is to get as close to 21 as possible without busting.  Will stop hitting once 17 is reached.')
print('Strategy 2 - Double Down on Hard 11: In addition to Standard Play, the Player will now double down on all hard 11s (thus doubling the payout on a win).')
print('Strategy 3 - Hit on Soft 18: In addition to Standard Play, the Player will hit on soft 18 when the dealer\'s upcard is showing 9,10, or Ace.')
print('Strategy 4 - Double Down on Hard 10: In addition to Standard Play, the Player will now double down on all hard 10s, when the dealer\'s upcard is 9 or less.\n\n')

simulation_runs = int(input('How many games would you like to simulate?: '))
independent_games = int(input('Fresh deck after each game (Input 1) or Standard reshuffling after exhausted deck (Input 0) : '))

BJ_Strat1.standardplay(simulation_runs,independent_games)
BJ_Strat2.DD_Hard_Eleven(simulation_runs,independent_games)
BJ_Strat3.Hit_Soft_18(simulation_runs,independent_games)
BJ_Strat4.DD_Hard_Ten(simulation_runs,independent_games)