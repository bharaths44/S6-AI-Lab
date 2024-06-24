# # Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print (f"Disk : 1 Source : {source} Destination : {destination}")
		return
	

	TowerOfHanoi(n-1, source, auxiliary, destination)
	print (f"Disk : {n} Source : {source} Destination : {destination}")
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code
n = 4
TowerOfHanoi(n,'A','C','B') 
# A, C, B are the name of rods
