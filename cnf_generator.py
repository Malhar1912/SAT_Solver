import random

def generate_random_cnf(n_vars, n_clauses, clause_len=3):
    cnf = []
    for _ in range(n_clauses):
        clause = set()
        while len(clause) < clause_len:
            var = random.randint(1, n_vars)
            lit = var if random.choice([True, False]) else -var
            clause.add(lit)
        cnf.append(list(clause))
    return cnf
