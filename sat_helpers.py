def is_satisfied(clause, assignment):
    return any(lit in assignment for lit in clause)

def is_conflict(clause, assignment):
    return all(-lit in assignment for lit in clause)

def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            unassigned = [lit for lit in clause if lit not in assignment and -lit not in assignment]
            if len(unassigned) == 1:
                unit = unassigned[0]
                if -unit in assignment:
                    return clauses, assignment  # conflict
                assignment.add(unit)
                changed = True
    return clauses, assignment

def pure_literal_assign(clauses, assignment):
    literals = set(lit for clause in clauses for lit in clause)
    for lit in literals:
        if -lit not in literals:
            assignment.add(lit)
    return clauses, assignment
