# Constants for maximum and minimum values
MAX_VALUE, MIN_VALUE = 1000, -1000
# Initialize alpha and beta
alpha, beta = MIN_VALUE, MAX_VALUE
# Initialize values
values = []

def minimax(depth, node_index, is_maximizing_player):
	global alpha, beta, values
	# Base case: if we've reached the maximum depth, return the node's value
	if depth == 3:
		return values[node_index]

	if is_maximizing_player:
		best_value = MIN_VALUE

		# Recur for left and right children
		for i in range(2):
			val = minimax(depth + 1, node_index * 2 + i, False)
			print(f"Node {node_index} value: {val}")
			best_value = max(best_value, val)
			alpha = max(alpha, best_value)

			# Alpha Beta Pruning
			if beta <= alpha:
				break

		return best_value

	else:
		best_value = MAX_VALUE

		# Recur for left and right children
		for i in range(2):
			val = minimax(depth + 1, node_index * 2 + i, True)
			print(f"Node {node_index} value: {val}")
			best_value = min(best_value, val)
			beta = min(beta, best_value)

			# Alpha Beta Pruning
			if beta <= alpha:
				print(f"{alpha} {beta}")
				break

		return best_value

# Driver Code
if __name__ == "__main__":
	values = [int(x) for x in input("Enter the values of nodes: ").split()]
	print("The optimal value is :", minimax(0, 0, True))

#-1 4 2 6 -3 -5 0 7
# 3 5 6 9 1 2 0 -1