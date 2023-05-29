import json
import networkx as nx

# Load JSON data
with open('source_documents/new_dependencies.json') as f:
    data = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for file, dependencies in data.items():
    for dependency in dependencies:
        G.add_edge(file, dependency)

# Compute PageRank scores
pagerank_scores = nx.pagerank(G)

# Save PageRank scores to a file
with open('new_pagerank_scores.json', 'w') as f:
    json.dump(pagerank_scores, f)