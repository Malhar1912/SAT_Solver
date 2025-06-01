🧠 DPLL SAT Solver with Decision Tree Visualization
This project implements a SAT solver based on the DPLL (Davis–Putnam–Logemann–Loveland) algorithm, enhanced with powerful heuristics such as:

Unit Propagation to simplify clauses,

Pure Literal Elimination to quickly assign literals that appear with only one polarity,

And a graph-based visualization of the decision tree using the networkx and matplotlib libraries.

This visualization helps to intuitively understand the backtracking decisions and conflicts encountered during the SAT solving process.

📁 Project Structure
├── cnf_generator.py      # Generates random CNF formulas
├── sat_helpers.py        # Helper functions for unit propagation and pure literals
├── dpll_solver.py        # Core DPLL algorithm with decision tree generation
├── visualization.py      # Graph visualization utilities using networkx and matplotlib
├── main.py               # Main execution script to run the solver
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🚀 How to Run
1. Clone the Repository
git clone https://github.com/your-username/dpll-sat-visualizer.git
cd dpll-sat-visualizer
2. Install Dependencies
pip install -r requirements.txt
3. Run the Solver
python main.py
📌 Features:

Random CNF Generation:
Generates k-CNF formulas with a configurable number of variables and clauses for testing.

DPLL SAT Solver:
Employs recursive backtracking combined with unit propagation and pure literal heuristics for efficient solving.

Decision Tree Visualization:
Visualizes each assignment decision and backtracking step as nodes in a decision tree graph, making it easier to follow the solving process.

🖼️ Sample Visualization
The decision tree graph clearly indicates:

The current variable assignments at each node,

Timestamp of each decision,

Green nodes for satisfiable branches,

Red nodes marking conflicts where backtracking occurs.



📋 Example CNF Formula
# Sample CNF with 4 variables and 6 clauses:
[[1, -3, 2], [-1, 2, 4], [3, -4, 1], [-2, 3, -1], [-4, 2, 1], [4, -3, -2]]

📚 References
Davis, M., & Putnam, H. (1960). A Computing Procedure for Quantification Theory.

Handbook of Satisfiability, Biere et al.

Official documentation for networkx and matplotlib.

✅ Future Enhancements
Support for CNF input from DIMACS files.

Interactive and web-based visualization of the decision tree (e.g., using Plotly or PyVis).

Integration of advanced SAT solver techniques such as clause learning and backjumping.

🧑‍💻 Author
Malhar Pangarkar
