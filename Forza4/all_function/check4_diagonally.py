
table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1],
		[0,0,0,0,0,1,0],
		[0,0,0,0,1,0,0],
		[0,0,0,1,0,0,0]]


for i in range(len(table)):
	print(table[i])

def check4_horizontally(table:list) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if i <= 3 and s<=2 and table[s][i]== 1 and  table[s+1][i+1]== 1 and table[s+2][i+2]== 1 and table[s+3][i+3]== 1 :
				print("YOU WIN")
				return True
				
			if i <= 3 and s>1 and table[s][i]== 1 and  table[s-1][i+1]== 1 and table[s-2][i+2]== 1 and table[s-3][i+3]== 1 :
				print("YOU WIN")
				return True 
				
			else:
				continue	
				
	return False
			
			
controll = check4_horizontally(table)

if controll==False:
	print("NEXT ROUND")
