
table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,1,0,0,0,2],
		[0,0,0,0,0,0,0],
		[0,0,1,0,0,0,2],
		[0,0,1,0,0,0,2]]


for i in range(len(table)):
	print(table[i])


def check4_vertically(table:list, player:int) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if s <= 2 and table[s][i]== player and  table[s+1][i]== player and table[s+2][i]== player and table[s+3][i]== player :
				return True
						
			else:
				continue	
				
	return False
	
	
	

player=2
if check4_vertically(table,player) == True:
	print(player,"WIN")
