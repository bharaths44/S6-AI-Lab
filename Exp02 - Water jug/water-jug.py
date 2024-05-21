def WaterJugSolver(amt1, amt2, aim):
    visited_states = set()
    shortest_path = None

    def explore(amt1, amt2, path):
        nonlocal shortest_path

        if (amt1, amt2) in visited_states:
            return
        visited_states.add((amt1, amt2))

        if amt2 == aim:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path.copy()
            return

        # Fill jug 1
        if amt1 < jug1:
            explore(jug1, amt2, path + [(jug1, amt2)])

        # Fill jug 2
        if amt2 < jug2:
            explore(amt1, jug2, path + [(amt1, jug2)])

        # Empty jug 1
        if amt1 > 0:
            explore(0, amt2, path + [(0, amt2)])

        # Empty jug 2
        if amt2 > 0:
            explore(amt1, 0, path + [(amt1, 0)])

        # Pour from jug 1 to jug 2
        if amt1 > 0 and amt2 < jug2:
            pour = min(amt1, jug2 - amt2)
            explore(amt1 - pour, amt2 + pour, path + [(amt1 - pour, amt2 + pour)])

        # Pour from jug 2 to jug 1
        if amt2 > 0 and amt1 < jug1:
            pour = min(amt2, jug1 - amt1)
            explore(amt1 + pour, amt2 - pour, path + [(amt1 + pour, amt2 - pour)])

    explore(0, 0, [(0, 0)])  # Start exploring from the initial state

    if shortest_path is not None:
        print("Shortest solution found in", len(shortest_path)-1, "steps:")
        for step, state in enumerate(shortest_path):
            print(f"Step {step+1}: Jug 1 = {state[0]}, Jug 2 = {state[1]}")
    else:
        print("No solution found.")

# Step 2: Read the capacities of jug 1 and jug 2 from the user
jug1 = int(input("Enter the capacity of jug 1: "))
jug2 = int(input("Enter the capacity of jug 2: "))

# Step 3: Read the amount of water to be present in the second jug
aim = int(input("Enter the target amount of water in jug 2: "))

# Step 4: Call the WaterJugSolver function with the given capacities and target amount
WaterJugSolver(0, 0, aim)
