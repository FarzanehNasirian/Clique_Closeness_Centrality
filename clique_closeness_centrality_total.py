import pandas as pd
import numpy as np


def Branch(G, dist_mtx, tcc, x, Tree, F, U, H, LB):
    
    for k in range(len(U[x])):
        
        #unique name to child node
        child_idx = x + '_' + str(k)
        
        #create F, U, and H for child node
        F[child_idx] = F[x] + [U[x][k]]   
        U[child_idx] = list(set(U[x]) & set(G.get_all_neighbors(U[x][k])) - set(U[x][:k]))  
        v_0 = F[child_idx][0]
        nodes = F[child_idx] + U[child_idx]
        if x == 'root':
            H[child_idx] = set(v for v in G.iter_vertices() if dist_mtx[v][v_0] == np.take(dist_mtx[v], nodes).min() + 1)
        else:
            H[child_idx] = set()
            for j in H[x]:
                for v in nodes:
                    if dist_mtx[j][v] == dist_mtx[j][v_0] - 1:
                        H[child_idx].add(j)
            
        #compute LB for child node
        LB[child_idx] = tcc[v_0] - len(H[child_idx])
                    
    #add created children to Tree
    temp_dict = {x + '_' + str(k): LB[x + '_' + str(k)] for k in range(len(U[x]))}
    Tree.extend(dict(sorted(temp_dict.items(), key=lambda x:x[1], reverse=True)).keys())
    
    return(Tree, F, U, H, LB)


def Binary_search_tree(G, dist_mtx):
    
    #total-distance closeness centrality
    tcc = dict()
    for v in G.iter_vertices(): tcc[v] = dist_mtx[v].a.sum()
    min_tcc = min(tcc.values())

    #initialize root
    Tree = []
    F = {'root':[]}  #clique selected through the search 
    U = {'root':[v for v in G.iter_vertices()]}    #candidate nodes
    H = {'root':set()}  #nodes closer to F|U than to the first child of the path
    LB = {'root':0}
    UB = min_tcc
        
    #start the search
    D_star = np.random.choice([k for k,v in tcc.items() if v == min_tcc])
    opt_sols = []
    Tree, F, U, H, LB = Branch(G, dist_mtx, tcc, 'root', Tree, F, U, H, LB)
    while Tree:
        x = Tree[-1]
        Tree = Tree[:-1]
        if U[x]:
            if LB[x] < UB:
                Tree, F, U, H, LB = Branch(G, dist_mtx, tcc, x, Tree, F, U, H, LB)
        else:
            if LB[x] < UB:
                UB = LB[x]
                D_star = F[x]
                
    return(D_star, UB)     

