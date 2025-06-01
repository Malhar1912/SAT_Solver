import networkx as nx
import time
from cnf_generator import generate_random_cnf
from dpll_solver import dpll_visual, backtrack_count, conflict_count
from visualization import draw_decision_tree

if __name__ == "__main__":
    num_vars = 4
    num_clauses = 6
    clause_len = 3

    cnf = generate_random_cnf(num_vars, num_clauses, clause_len)

    print("Generated CNF:")
    for clause in cnf:
        print(clause)

    G = nx.DiGraph()
    start_time = time.time()
    result, assignment, G = dpll_visual(cnf, G=G)
    end_time = time.time()

    print("\nResult:", "SATISFIABLE" if result else "UNSATISFIABLE")
    if result:
        print("Assignment:", assignment)

    print(f"\n⏱ Total Time: {end_time - start_time:.4f} seconds")
    print(f"🔁 Backtracks: {backtrack_count}")
    print(f"💥 Conflicts: {conflict_count}")

    draw_decision_tree(G)
