table =[[0,0,0,0,0,0,1],
		[0,0,0,0,0,1,1],
		[0,0,0,0,1,1,1],
		[0,0,0,1,1,1,1],
		[0,0,1,1,1,1,1],
		[0,1,1,1,1,1,1]]


user_input=int(input("You choose number..? : "))

def input_physics(input_number:int, matrix:list) -> list:
	for r in range (len(matrix)) :
		if r == 0 and matrix[r][input_number] == 1:
			print("ERROR")
			
		elif matrix[r][input_number] == 0 and r+1< len(matrix):
			print()
		
		elif matrix[r][input_number] !=0:
			matrix[r-1][input_number] = 1 

		elif r+1 == len(matrix):
			matrix[r][input_number] = 1
			
		else:
			print("BUG")
			
			
	return(matrix)

table=input_physics(user_input,table)

for i in range(len(table)):
	print(table[i])
