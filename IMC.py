# -*- coding: cp1252 -*-
print "Programa Para calcular el IMC \nEl indice de masa corporal (IMC) \nes una medida de asociacion \nentre el peso y la talla \nde un individuo \n \n"
peso= input("Digite su Peso \n")
estatura = input("Digite Su Estatura \n")
imc = (peso)/(estatura**2)
print "Su IMC es de : "
print imc
print "---------------------------\n"
print "Clasificación de la OMS del estado \nnutricional de acuerdo con el IMC \nÍndice de Masa Corporal"
print "---------------------------\n"
print "INFRAPESO <18,50 \nDELGADEZ SEVERA <16,00 \n DELGADEZ NO MUY PRONUNCIADA 17,00-18,49"
print "\nNORMAL 18,5 - 24,99"
print "\nSOBREPESO >= 25,00 \nPREOBESO 25,00 - 29,99 \nOBESO >=30,00"
print "\nOBESO TIPO 1 30,00 - 34,99 \nOBESO TIPO 2 35,00 - 39,99 \nOBESO TIPO 3 >=40,00"
