standings = [(17, anton, 0, 0), (18, marina, 0, 0), (19, roman, 0, 0), (20, elina, 0, 0), (21, artem, 0, 0)]

def swissPairings():
	players = standings
	pairings = []
	n = 0
	
	if len(players) // 2 == 0:
	    while n != len(players) - 1:
	    	pair = (players[n][0], players[n][1], players[n + 1][0], players[n + 1][1])
	    	pairings.append(pair)
	    	n += 2
	else:
		while n != len(players) - 2:
	    	pair = (players[n][0], players[n][1], players[n + 1][0], players[n + 1][1])
	    	pairings.append(pair)
	    	n += 2
	    single_player = (players[-1][0], players[-1][1])
	    pairings.append(single_player)

	return pairings

print swissPairings()
