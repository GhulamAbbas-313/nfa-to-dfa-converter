from graphviz import Digraph

dot = Digraph(comment='NFA-ε to DFA Converter Flowchart')

# Nodes
dot.node('A', 'Input: NFA / ε-NFA', shape='box')
dot.node('B', 'Check for ε-transitions?', shape='diamond')
dot.node('C', 'Compute ε-closures', shape='box')
dot.node('D', 'Subset Construction (Powerset Method)', shape='box')
dot.node('E', 'Build Equivalent DFA', shape='box')
dot.node('F', 'Visualize Transitions', shape='box')
dot.node('G', 'Display Output DFA', shape='box')

# Edges
dot.edge('A', 'B')
dot.edge('B', 'C', label='Yes')
dot.edge('B', 'D', label='No')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')

# Render to PNG and open it
dot.render('nfa_to_dfa_flowchart', format='png', view=True)
