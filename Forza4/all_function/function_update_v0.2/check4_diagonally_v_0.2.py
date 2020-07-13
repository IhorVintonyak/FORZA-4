
table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[2,0,0,0,0,0,1],
		[0,2,0,0,0,1,0],
		[0,0,0,0,0,0,0],
		[0,0,0,2,0,0,0]]


for i in range(len(table)):
	print(table[i])

def check4_diagonally(table:list,player:int) -> bool:
	for s in range(len(table)):
			
		for i in range(len(table[1])):
			
			if i <= 3 and s<=2 and table[s][i]== player and  table[s+1][i+1]== player and table[s+2][i+2]== player and table[s+3][i+3]== player :
				return True
					
			if i <= 3 and s>1 and table[s][i]== player and  table[s-1][i+1]== player and table[s-2][i+2]== player and table[s-3][i+3]== player :
				return True 
					
			else:
				continue	
					
	return False
			
			
player=2
if check4_diagonally(table,player) == True:
	print(player,"WIN")
