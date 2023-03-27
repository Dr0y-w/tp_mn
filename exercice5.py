#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# module pour LU et Cholesky
import numpy as np

def random_mat_diag_dom(n):
    """fabrique une matrice aléatoire n x n à diagonale str. dominante"""
    A = np.random.rand(n,n)
    for i in range(n) :
        A[i,i] += np.sum(A[i,:])
    return A

def donnees_exercice3_td2():
    """retourne la matrice, le second membre et la solution du systeme
    lineaire de l'exercice 3 de la feuille td2"""
    A = np.array([[1,2,3,4],[1,4,9,16],[1,8,27,64],[1,16,81,256]],float)
    b = np.array([2,10,44,190],float)
    x = np.array([-1,1,-1,1],float)
    return A,b,x

def lu_fact(A):
    # A est une matrice n x n dont on calcule la factorisation LU simple.
    # On renvoie 2 objets: 
    # 1. le tableau LU qui contient la factorisation de maniere compacte
    # 2. un entier donnant le statut du calcul :
    # istat = -1 si A n'est pas carree (NB: neanmoins on pourrait effectuer
    #            une factorisation sur une matrice rectangulaire)
    #          0 OK
    #          k > 0 : le pivot naturel a l'etape k est nul
    LU = A.copy()
    n,m = np.shape(A)
    if n != m:
        istat = -1
    else:
        istat = 0
    for k in range(1,n-1):
        if LU[k,k]!=0:
            for i in range(k+1,n):
                LU[i,k] = LU[i,k]/LU[k,k]
                for j in range(k+1,n):
                    LU[i,j] = LU[i,j]-LU[i,k]*LU[k,j]
    
        
        
    return LU, istat        
        
def lu_solve(LU,b):
    # resout Ax=b par descente-remontee connaissant la factorisation LU de A
    y = b.copy()
    n = len(y)
    # resolution de Ly = b
    
     . . . A COMPLETER . . .
     
    # resolution de Ux = y
    
     . . . A COMPLETER . . .
    
    return x

def chol_fact(A):
    # A est une matrice symétrique (définie positive) n x n dont on calcule
    # la factorisation de Cholesky A=CC^T.
    # On renvoie 2 objets: 
    # 1. le tableau C qui contient :
    #    - la matrice C dans sa partie triangulaire inférieure 
    #    - les coefficients supérieurs de A dans la partie triangulaire 
    #      supérieure (sans la diagonale)
    # 2. un entier donnant le statut du calcul :
    # istat = -1 si A n'est pas carree 
    #          0 OK
    #          k > 0 : erreur obtenue à l'étape k (matrice non définie positive)
    C = A.copy()
    n,m = np.shape(A)
    if n != m:
        istat = -1
    else:
        istat = 0
        
        . . . A COMPLETER (calcul de C). . .
    
    return C, istat
    
        