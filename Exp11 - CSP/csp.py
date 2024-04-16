DOMAIN = ['Monday', 'Tuesday', 'Wednesday']

def backtrack_search(assignment, VARIABLES):
    if len(assignment) == len(VARIABLES):  # Check if assignment is complete
        return assignment
    var = select_unassigned_variable(assignment, VARIABLES)
    for value in DOMAIN:
        if is_consistent(var, value, assignment):
            assignment.append((var, value))
            result = backtrack_search(assignment, VARIABLES)
            if result:
                return result
            assignment.pop()
    return None

def select_unassigned_variable(assignment, VARIABLES):
    for var in VARIABLES:
        if var not in [a[0] for a in assignment]:
            return var
    return None

def is_consistent(var, value, assignment):
    for (v, val) in assignment:
        if v == var and val == value:
            return False
    return True

def main():
    assignment = []
    VARIABLES = ['var1', 'var2', 'var3', 'var4', 'var5']
    solution = backtrack_search(assignment, VARIABLES)
    if solution:
        for var, value in solution:
            if var == 'var3':
                print(f"Assign {value} to {var}")
                return False
        print("True")
    else:
        print("None")

if __name__ == "__main__":
    main()
