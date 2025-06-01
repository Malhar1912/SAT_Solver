import time
from sat_helpers import is_satisfied, is_conflict, unit_propagate, pure_literal_assign

backtrack_count = 0
conflict_count = 0

def dpll_visual(cnf, assignment=set(), G=None, parent=None, label="ROOT", depth=0):
    global backtrack_count, conflict_count

    timestamp = time.strftime("%H:%M:%S")
    node_name = f"{label}\n{assignment}\n[{timestamp}]"
    
    if G is not None:
        G.add_node(node_name)
        if parent:
            G.add_edge(parent, node_name)

    clauses, assignment = unit_propagate(cnf, assignment.copy())
    clauses, assignment = pure_literal_assign(clauses, assignment)

    if all(is_satisfied(clause, assignment) for clause in clauses):
        if G is not None:
            G.nodes[node_name]['color'] = 'green'
        return True, assignment, G

    if any(is_conflict(clause, assignment) for clause in clauses):
        if G is not None:
            G.nodes[node_name]['color'] = 'red'
        conflict_count += 1
        return False, None, G

    unassigned = set(abs(lit) for clause in clauses for lit in clause if lit not in assignment and -lit not in assignment)
    if not unassigned:
        if G is not None:
            G.nodes[node_name]['color'] = 'red'
        return False, None, G

    lit = next(iter(unassigned))

    # Try assigning True
    sat, result, G = dpll_visual(cnf, assignment | {lit}, G, node_name, f"x{lit}=T", depth+1)
    if sat:
        return True, result, G

    backtrack_count += 1

    # Try assigning False
    return dpll_visual(cnf, assignment | {-lit}, G, node_name, f"x{lit}=F", depth+1)
