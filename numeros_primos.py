# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:42:01 2020

@author: ADMINISTRADOR
"""

# Etapas


"""
Objetivo: Criar uma Lista que armazene números primos
# Etapa = Criar uma função para passarmos o parâmetro que será o tamanho da 
          lista 
"""

# Criando a Classe

class listaprimo():
    def __init__(self,size):
        self.lista = []
        self.size = size
            
        
        i = 0
        while i < int(self.size):
            
            if (i==2) or (i==3) or (i==5) or (i==7):
                self.lista.append(i)
                #print("A lista está crescendo...\n", self.lista)
            elif (i%2!=0) and (i%3!=0) and (i%5!=0) and (i%7!=0):
                self.lista.append(i)
                #print("A lista está crescendo...\n", self.lista)
            #else:
                #print("O número não é primo \n" + str(i))
            i=i+1
        
        return print(self.lista)


#Lista = listaprimo(input ("Entre com o valor máximo da sua lista: "))


