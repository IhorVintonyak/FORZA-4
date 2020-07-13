
table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,2,2,1,2,0,0],
		[0,0,0,0,0,0,0],
		[0,1,1,1,0,0,0]]


for i in range(len(table)):
	print(table[i])

def check4_horizontally(table:list, player:int) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if i <= 3 and table[s][i]== player and  table[s][i+1]== player and table[s][i+2]== player and table[s][i+3]== player :
				return True
						
			else:
				continue	
				
	return False

player=1
if check4_horizontally(table,player) == True:
	print(player,"WIN")
