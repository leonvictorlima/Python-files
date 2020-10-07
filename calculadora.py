# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:33:46 2020

@author: ADMINISTRADOR
"""

#Objetivo: Criar uma calculadora para efetuar operações básicas;

print("\n1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")

opcao= int(input("Entre com a opção na calculadora: "))

def soma(arg01, arg02):
        return arg01 + arg02
    
def subtracao(num01, num02):
        return num01 - num02

def multiplicacao(arg01, arg02):
        return arg01 * arg02

def divisao(arg01, arg02):
        return arg01/arg02
    
if opcao == 1:
    arg01 = int(input("Entre com o primeiro valor: "))
    arg02 = int(input("Entre com o segundo valor: "))
    print("O valor da soma é: "+ str(soma(arg01,arg02)))

elif opcao == 2:
    arg01 = int(input("Entre com o primeiro valor: "))
    arg02 = int(input("Entre com o segundo valor: "))
    print("O valor da subtração é: "+ str(subtracao(arg01,arg02)))

elif opcao == 3:
    arg01 = int(input("Entre com o primeiro valor: "))
    arg02 = int(input("Entre com o segundo valor: "))
    print("O valor da subtração é: "+ str(multiplicacao(arg01,arg02)))

elif opcao == 4:
    arg01 = int(input("Entre com o primeiro valor: "))
    arg02 = int(input("Entre com o segundo valor: "))
    print("O valor da subtração é: "+ str(divisao(arg01,arg02)))

else:
    print("Valor inválido, tente novamente.")
