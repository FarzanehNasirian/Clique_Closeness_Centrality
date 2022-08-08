import pandas as pd
import numpy as np


def Branch(G, dist_mtx, x, Tree, F, U, S, LB, UB):
    
    for k in range(len(U[x])):
        
        #unique name to child node
        child_idx = x + '_' + str(k)
        
        #create F, U, and S for child node
        F[child_idx] = F[x] | {U[x][k]}
        U[child_idx] = list(set(U[x]) & set(G.get_all_neighbors(U[x][k])) - set(U[x][:k]))
        if x == 'root':
            S[child_idx] = [v for v in G.iter_vertices() if dist_mtx[U[x][k]][v] == UB]
        else:
            temp_S = []
            for v in S[x]:
                if dist_mtx[U[x][k]][v] == UB:
                    temp_S.append(v)
            S[child_idx] = set(temp_S)
            
        #compute LB for child node
        LB[child_idx] = UB
        for s_v in S[child_idx]:
            for u_v in U[child_idx]:
                if dist_mtx[s_v][u_v] == UB - 1:
                    LB[child_idx] = UB - 1
                    break
                    
    #add created children to Tree
    temp_dict = {x + '_' + str(k): len(S[x + '_' + str(k)]) for k in range(len(U[x]))}
    Tree.extend(dict(sorted(temp_dict.items(), key=lambda x:x[1], reverse=True)).keys())
    
    return(Tree, F, U, S, LB)


def Binary_search_tree(G, dist_mtx):
    
    #compute max-distance closeness centrality
    node_eccent = {v:dist_mtx[v].a.max() for v in G.iter_vertices()}   #node eccentricity
    graph_radius = min(node_eccent.values())  #graph radius
    C_G = [v for v in G.iter_vertices() if node_eccent[v] == graph_radius]  #set C_G

    #initialize root
    Tree = []
    F = {'root':set()}  #clique selected through the search 
    U = {'root':C_G}    #candidate nodes
    S = {'root':set()}  #nodes with distance of graph_radius to F
    LB = {'root':graph_radius - 1}
    UB = graph_radius
        
    #start the search
    D_star = [np.random.choice(C_G)]
    Tree, F, U, S, LB = Branch(G, dist_mtx, 'root', Tree, F, U, S, LB, UB)
    while Tree:
        x = Tree[-1]
        Tree = Tree[:-1]
        if S[x]:
            if U[x]:
                if LB[x] < UB:
                    Tree, F, U, S, LB = Branch(G, dist_mtx, x, Tree, F, U, S, LB, UB)
        else:
            UB -= 1
            D_star = F[x]
            break
                
    return(D_star, UB)     

