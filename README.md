
# 🧠 DPLL SAT Solver with Decision Tree Visualization

This project implements a SAT solver based on the classical **DPLL (Davis–Putnam–Logemann–Loveland)** algorithm enhanced with powerful heuristics like unit propagation and pure literal elimination. It features an intuitive **decision tree visualization** that illustrates the solver’s backtracking and conflict resolution steps using `networkx` and `matplotlib`.

---

## 🚀 Features

- **Random CNF Formula Generator:** Create k-CNF formulas with customizable numbers of variables and clauses for testing.
- **Efficient DPLL Solver:** Recursive backtracking with heuristics for unit propagation and pure literal elimination.
- **Decision Tree Visualization:** Graphically displays variable assignments, backtracking, and conflicts as a decision tree.
- **Color-coded Nodes:** Green nodes represent satisfiable branches, red nodes indicate conflicts where backtracking occurs.

---

## 📁 Project Structure

```
├── cnf_generator.py      # Generates random CNF formulas
├── sat_helpers.py        # Helper functions for unit propagation and pure literal elimination
├── dpll_solver.py        # Core DPLL algorithm implementation with decision tree support
├── visualization.py      # Visualization utilities for decision tree using networkx & matplotlib
├── main.py               # Main script to run solver and visualize results
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 💻 Installation and Usage

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/dpll-sat-visualizer.git
cd dpll-sat-visualizer
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the solver:

```bash
python main.py
```

This will execute the solver on a sample CNF formula and generate a decision tree visualization.

---

## 📋 Example CNF Formula

You can customize CNF formulas in `cnf_generator.py` or pass your own clauses. Example:

```python
[[1, -3, 2], [-1, 2, 4], [3, -4, 1], [-2, 3, -1], [-4, 2, 1], [4, -3, -2]]
```

---

## 🖼️ Visualization

The generated decision tree graph shows:

- Current variable assignments at each node
- Decision timestamps
- Green nodes for satisfiable paths
- Red nodes where conflicts cause backtracking

---

## 📚 References

- Davis, M., & Putnam, H. (1960). *A Computing Procedure for Quantification Theory*.
- Handbook of Satisfiability, Biere et al.
- [networkx Documentation](https://networkx.org/)
- [matplotlib Documentation](https://matplotlib.org/)

---

## ✅ Future Enhancements

- Support for standard **DIMACS CNF input files**.
- Interactive web-based visualizations (using Plotly, PyVis, etc.).
- Implementation of advanced SAT solver techniques like **clause learning** and **backjumping**.

---

## 🧑‍💻 Author

**Malhar Pangarkar**

---

Feel free to open issues or contribute via pull requests!

---

*Happy SAT solving!* 🎉

