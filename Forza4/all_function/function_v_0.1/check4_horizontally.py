
table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,1,1,1,1,0,0]]


for i in range(len(table)):
	print(table[i])

def check4_horizontally(table:list) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if i <= 3 and table[s][i]== 1 and  table[s][i+1]== 1 and table[s][i+2]== 1 and table[s][i+3]== 1 :
				print("YOU WIN")
				return True
						
			else:
				continue	
				
	return False
			
check4_horizontally(table)
