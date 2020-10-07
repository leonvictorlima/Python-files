# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:11:26 2020

@author: ADMINISTRADOR
"""

class exclusive():
    def iniciar(self,word):
        
        self.word = word
        self.word = self.word.lower()
        lista = []
        size = len(self.word)
        for letter in self.word:
            i= self.word.index(letter)+1
            while i < size:
                if(letter == self.word[i]) and (letter not in lista):
                    lista.append(letter)
                #else: print("Não são iguais\n")
                i=i+1
        
        return print(lista)

exclusive = exclusive()
exclusive.iniciar(input("Entre com a palavra: "))