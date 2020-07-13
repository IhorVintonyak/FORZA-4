table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,1,0,1,0,0,0]]


def input_physics(input_number:int, matrix:list,player:int) -> list:
	for r in range (len(matrix)) :
		if r == 0 and matrix[r][input_number] != 0:
			print("ERROR")
		
		elif matrix[r][input_number] != 0 :
			if player == 1:
				matrix[r-1][input_number] = 1 
			else:
				matrix[r-1][input_number] = 2 
			
			return(matrix)

		elif r+1 == len(matrix):
			if player == 1:
				matrix[r][input_number] = 1
			else:
				matrix[r][input_number] = 2 
			
			return(matrix)

player=1

i=0

while i < 20:
	
	user_input=int(input("You choose number..? : "))
	table=input_physics(user_input,table,player)
	
	if player == 1: 
		player = 2
	else:
		player = 1
	
	i+=1

	for i in range(len(table)):
		print(table[i])
