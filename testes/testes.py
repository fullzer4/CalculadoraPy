import numpy as np

Mx = input("Quantas linhas e colunas possui sua matriz x: (ex: 2:2) ")
My = input("Quantas linhas e colunas possui sua matriz y: (ex: 2:2) ")

if Mx == "1:1":
    MxaC1L1 = input("Insira o numero da coluna 1 linha 1 da Matriz x= ")

elif Mx == "1:2":
    MxaC1L1 = input("Insira o numero da coluna 1 linha 1 da Matriz x= ")
    MxaC2L1 = input("Insira o numero da coluna 2 linha 1 da Matriz x= ")

if My == "1:1":
    MyaC1L1 = input("Insira o numero da coluna 1 linha 1 da Matriz y= ")

elif My == "1:2":
    MyaC1L1 = input("Insira o numero da coluna 1 linha 1 da Matriz y= ")
    MyaC2L1 = input("Insira o numero da coluna 2 linha 1 da Matriz y= ")

Mxa = np.array(dtype=[[MxaC1L1], [MxaC2L1]])
Mya = np.array([[MyaC1L1], [MyaC2L1]])
print(Mxa @ Mya)

#https://schneiderfelipe.xyz/matrizes-e-vetores/ referencia
#falho