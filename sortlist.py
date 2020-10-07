# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:46:23 2020

@author: ADMINISTRADOR
"""

"""
Objetivo: Criar uma Lista aleatória de números inteiros de 1 até 1000;
# Etapa = Criar uma função para passarmos o parâmetro que será o tamanho da 
          lista 
"""


import random

#size = int (input ("Entre com o tamanho da sua lista: "))
#size = int(size())
class sortlist():
    def __init__(self,size):                
        self.size = size
        self.list = []    
    
        for items in range(0,int(self.size)):            
            #value = random.randrange(1,int(self.size))
            value = random.randrange(1,1000)
            #value = str(value)
            self.list.append(value)
        
        self.list.sort()
        return print(self.list)

sortlist = sortlist(input ("Entre com o tamanho da sua lista: "))
