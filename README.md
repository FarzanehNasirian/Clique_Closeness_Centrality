#Clique Closeness Centrality

This repository has the python modules of two combinatorial algorithms proposed by [Nasirian et al., 2020](https://www.sciencedirect.com/science/article/abs/pii/S0377221719309464) for identifying max- and total-disatance-closeness-central cliques. 
$$Given a graph G=(V,E) and a pair of nodes i,j\in V, let d_{ij} denote the distance between i and j in G. Then, the maximum- and total-distance- closeness centralities of a set S\subseteq V are defined as follows.

Given a vertex i\in V\setminus S, let \sigma(i,S)=\min_{j\in S}d_{ij} denote the distance of vertex i to set S. Then, 

	(a) maximum-distance-closeness centrality of S is C_m(S)=max_{i\in V\setminus S}\sigma(i,S), and
	(b) total-distance-closeness centrality of S is C_t(S)=\sum_{i\in V\setminus S}\sigma(i,S).$$

An example of max-disatance-closeness-central clique is illustrated below where 
 max-distance-closeness-central-cliques
![max_distance_closeness_central_clique](max_distance_closeness_central_clique.svg) 


![total_distance_closeness_central_clique](total_distance_closeness_central_clique.svg)