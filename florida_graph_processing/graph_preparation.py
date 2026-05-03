import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: Load Data & Calculate Sigma
# ==========================================
df_dist = pd.read_csv('florida_distance.csv')

# Use median distance as the bandwidth (sigma)
sigma = df_dist['distance'].median()
print(f"Median Distance (sigma): {sigma:.2f} miles")

# ==========================================
# STEP 2: Transform Distance to Similarity Weight
# ==========================================
# Apply the Gaussian kernel formula
df_dist['weight'] = np.exp(-(df_dist['distance']**2) / (sigma**2))

# ==========================================
# STEP 3: Sparsify the Graph (Thresholding)
# ==========================================
lambda_threshold = 0.5
df_sparse = df_dist[df_dist['weight'] >= lambda_threshold]

print(f"Original edges (Fully Connected): {len(df_dist)}")
print(f"Remaining edges (Sparse Graph): {len(df_sparse)}")

# ==========================================
# STEP 4: Build NetworkX Graphs
# ==========================================
G_fully_connected = nx.from_pandas_edgelist(
    df_dist, source='county1', target='county2', edge_attr=['distance', 'weight']
)

G_sparse = nx.from_pandas_edgelist(
    df_sparse, source='county1', target='county2', edge_attr=['distance', 'weight']
)

# Ensure the sparse graph includes all nodes for consistent layout
G_sparse.add_nodes_from(G_fully_connected.nodes())

# ==========================================
# STEP 5: Plot the 3 Variations
# ==========================================
# Use a spring layout based on the fully connected graph so nodes stay in the exact same spots
pos = nx.spring_layout(G_fully_connected, seed=42)

# Create a figure with 3 columns
fig, axes = plt.subplots(1, 3, figsize=(24, 7))

# --- Plot 1: Before Thresholding (Raw/Fully Connected) ---
# Width=0.5 and alpha=0.5 for direct comparison
nx.draw(
    G_fully_connected, pos, ax=axes[0], 
    node_color='lightblue', with_labels=False, 
    edge_color='gray', width=0.5, alpha=0.5, node_size=50
)
axes[0].set_title("1. Before Thresholding\n(Fully Connected)", fontsize=14)

# --- Plot 2: After Thresholding (Uniform Edge Thickness) ---
# Width=0.5 and alpha=0.5 matching Plot 1
nx.draw(
    G_sparse, pos, ax=axes[1], 
    node_color='lightgreen', with_labels=False, 
    edge_color='gray', width=0.5, alpha=0.5, node_size=50
)
axes[1].set_title(f"2. After Thresholding (λ={lambda_threshold})\nUniform Edge Thickness", fontsize=14)

# --- Plot 3: After Thresholding (Weighted Edge Thickness) ---
# Extract weights and scale them up slightly so they are easy to see
edges = G_sparse.edges(data=True)
weights = [edge_data[2]['weight'] * 3.0 for edge_data in edges]

nx.draw(
    G_sparse, pos, ax=axes[2], 
    node_color='lightgreen', with_labels=False, 
    edge_color='black', width=weights, alpha=0.7, node_size=50
)
axes[2].set_title(f"3. After Thresholding (λ={lambda_threshold})\nWeighted Edge Thickness", fontsize=14)

plt.tight_layout()
plt.show()

# Save the sparsified dataframe for the next step of your pipeline
df_sparse.to_csv('florida_distance_sparse.csv', index=False)