'''
Igor Vintonyak 11/07/2020-eternity


Game with a vertical plate 6 X 7 where players take turns placing the figure (circles) on top, the figure falls by gravity and takes the first free place (bottom). The winner is  the player who has 4 pieces in a row vertically, horizontally, or diagonally.
'''
#1. FUNCTION

	#1.1) table 7X6 with 0 in free space


def create_matrix(qline:int,qcolumn:int) ->list :
	'''qline: quanti righe, qcolumn: quanti colonne.Rida lista vuota  '''
	matrix=[]
	for rr in range(qline):
		line=[]
		for b in range(qcolumn):
			line.append(0)
		matrix.append(line)
	return(matrix)

#1.2) Do physics (the chip should fall down)


def input_physics(input_number:int, matrix:list) -> list:
	'''input_number: column number entered by user; matrix: data table '''
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
			print("BUG in fuction input_physics ")
						
	return(matrix)


#1.3) Make a check on width

def check4_horizontally(table:list) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if i <= 3 and table[s][i]== 1 and  table[s][i+1]== 1 and table[s][i+2]== 1 and table[s][i+3]== 1 :
				print("YOU WIN")
				return True
						
			else:
				continue	
				
	return False
		
#1.4) Make a check on vertically

def check4_vertically(table:list) -> bool:
	for s in range(len(table)):
		
		for i in range(len(table[1])):
		
			if s <= 2 and table[s][i]== 1 and  table[s+1][i]== 1 and table[s+2][i]== 1 and table[s+3][i]== 1 :
				print("YOU WIN")
				return True
						
			else:
				continue	
					
	return False

	
#1.5) Make a check on diagonally

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

#2. MAIN

#2.1) WIN?
	
qLine = 6
qColumn = 7 

table= create_matrix(qLine,qColumn)

table =[[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0]]

i = 0
while i < 20:
	user_input=(int(input("You choose number..? : "))-1)

	table=input_physics(user_input,table)

	control_H = check4_horizontally(table)
	control_V = check4_vertically(table)
	control_D =check4_horizontally(table)

	for i in range(len(table)):
		print(table[i])

	if control_H == False and control_V == False and control_D == False:
		print("NEXT ROUND")
	i +=1

