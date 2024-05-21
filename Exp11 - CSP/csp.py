import random

def backtrack_search(assignment, variables, domain, constraints):
    # If all variables have been assigned, return the assignment
    if len(assignment) == len(variables):
        return assignment.copy()

    # Select an unassigned variable
    unassigned_var = select_unassigned_variable(assignment, variables)
    if unassigned_var is None:
        return None

    # Randomize the order of domain values
    random.shuffle(domain)

    # Try each value in the domain
    for value in domain:
        assignment[unassigned_var] = value

        # If the assignment is consistent, recursively search
        if is_consistent(unassigned_var, value, assignment, constraints):
            result = backtrack_search(assignment, variables, domain, constraints)
            if result is not None:
                return result

        # If the assignment is not consistent, or if the search did not find a solution, backtrack
        assignment[unassigned_var] = None

    return None

def select_unassigned_variable(assignment, variables):
    # Return the first variable that is not yet assigned
    for var in variables:
        if var not in assignment:
            return var
    return None

def is_consistent(variable, value, assignment, constraints):
    # Check if a variable-value assignment is consistent with the constraints
    for constraint in constraints:
        if variable in constraint[0]:
            related_variable = constraint[0][0] if constraint[0][1] == variable else constraint[0][1]
            if related_variable in assignment and assignment[related_variable] == value:
                return False
    return True

if __name__ == "__main__":
    assignment = {}
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    domain = ['Monday', 'Tuesday', 'Wednesday']

    # Define the constraints based on the graph edges
    constraints = [
        (('A', 'B'),),
        (('A', 'C'),),
        (('B', 'C'),),
        (('B', 'D'),),
        (('B', 'E'),),
        (('D', 'E'),),
        (('C', 'E'),),
        (('C', 'F'),),
        (('E', 'F'),),
        (('E', 'G'),),
        (('F', 'G'),)
    ]

    solution = backtrack_search(assignment, variables, domain, constraints)
    print(solution)