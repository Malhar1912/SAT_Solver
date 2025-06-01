import matplotlib.pyplot as plt
import networkx as nx

def draw_decision_tree(G, save_path="dpll_decision_tree.png"):
    pos = nx.spring_layout(G, seed=42)
    colors = [G.nodes[n].get('color', 'gray') for n in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2200, font_size=7)
    plt.title("DPLL Decision Tree")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
