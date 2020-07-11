'''
Igor Vintonyak 11/07/2020-eternity


Game with a vertical plate 6 X 7 where players take turns placing the figure (circles) on top, the figure falls by gravity and takes the first free place (bottom). The winner is  the player who has 4 pieces in a row vertically, horizontally, or diagonally.
'''
#1) table 7X6 with 0 in free space

qLine = 6
qColumn = 7 

def create_matrix(qline:int,qcolumn:int) ->list :
	'''qline: quanti righe, qcolumn: quanti colonne.Rida lista vuota  '''
	matrix=[]
	for rr in range(qline):
		line=[]
		for b in range(qcolumn):
			line.append(0)
		matrix.append(line)
	return(matrix)


table= create_matrix(qLine,qColumn)


	
#2) Do physics (the chip should fall down)

user_input=int(input("You choose number..? : "))

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

table=input_physics(user_input,table)

for i in range(len(table)):
	print(table[i])
	
#3) Make a check on length and width



#4) Make a check on diagonally



#5) Add to the color lists where 1 is red and 2 is yellow.
