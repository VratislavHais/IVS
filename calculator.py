# -*- coding: utf-8 -*-

"""@package docstring
    Documentation for this module.
     
     More details.
"""
import math
import re
from Tkinter import *
import tkMessageBox as box
#import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        """Vytvori novy ADT zasobnik. Zasobnik je vyuzivany pro vyhodnocovani operaci
        """
        self.items = []
        
    def isEmpty(self):
        """Zkontroluje naplneni zasobniku. Funkce vraci True pokud je zasobnik prazdny
        """
        return self.items == []
    
    def push(self, item):
        """Vlozi prvek do zasobniku.
        """
        self.items.append(item)
        
    def pop(self):
        """Vyjme prvek ze zasobniku a vrati jej.
        """
        return self.items.pop()
    
    def top(self):
        """Vrati prvek ze zasobniku (prvek neni odstranen)
        """
        if (not self.isEmpty()):
            return self.items[len(self.items)-1]
    
    def size(self):
        """Vraci aktualni pocet prvku v zasobniku.
        """
        return len(self.items)
        
    def remove(self, index):
        """Odebere prvek ze zasobniku na urcitem indexu.
           @param index Pozice na zasobniku, ze ktere se ma prvek odstranit.         
        """        
        del self.items[index]
        
    def clear(self):
        """Vycisteni zasobniku.
        """
        while (not self.isEmpty()):
            self.pop()
    
    def getIndexOfTopTerm(self):  #potreba pouze na odsraneni zavorek
        """Vraci index nejvyssiho terminalu. Funkce se pouziva pouze na zjisteni nasledujici zavorky.
        """
        for i in range(self.size()-1, 0, -1):
            if (self.items[i] == "("):
                return i
        
    def getTopTerminal(self):
        """Vraci nejvrchnejsi terminal na zasobniku.
        """
        for i in range(self.size()-1, -1, -1):
            if (self.items[i] == "+"):
                return "+"
            elif (self.items[i] == "-"):
                return "-"
            elif (self.items[i] == "*"):
                return "*"
            elif (self.items[i] == "/"):
                return "/"
            elif (self.items[i] == "^"):
                return "^"
            elif (self.items[i] == "sin"):
                return "sin"
            elif (self.items[i] == "cos"):
                return "cos"
            elif (self.items[i] == "tan"):
                return "tan"
            elif (self.items[i] == "cotg"):
                return "cotg"
            elif (self.items[i] == "log"):
                return "log"
            elif (self.items[i] == "ln"):
                return "ln"
            elif (self.items[i] == "("):
                return "("
            elif (self.items[i] == ")"):
                return ")"
            elif (self.items[i] == "$"):
                return "$"
        return False


    
    
def factorial(value):
    """!@brief Funkce na vypocet faktorialu.
       @param value Hodnota, jejiz faktorial pozadujeme.
    """
    if (value < 0):
        errWindow("Faktorial zaporneho cisla\n neni definovan")
        return False
    elif (value == 1 or value == 0):
        return 1
    else:
        return (value * factorial(value - 1))
    
def isNumber(string):
    """!@brief Funkce na zjisteni, zda je retezec cislo.
       @param string Retezec, u ktereho to potrebujeme zjistit.
    """    
    try:
        float(string)
        return True
    except:
        return False

def evalRule(index, stack, precTable, item):
    """!@brief Funkce vyhodnocujici pravidla.
        @param index Obsahuje umisteni pravidla v tabulce pro dany znak.
        @param stack Zasobnik.
        @param precTable Dvojrozmerne pole obsahujici pravidla.
        @param item Prave zpracovavany znak.
    """
    try:
        tmp = precTable[stack.getTopTerminal()][index]
        if (tmp == ">"):
            number1 = stack.pop()
            operation = stack.pop()
            if (operation == "sin"):
                stack.push(math.sin(number1))
            elif (operation == "cos"):
                stack.push(math.cos(number1))
            elif (operation == "tan"):
                stack.push(math.tan(number1))
            elif (operation == "cotg"):
                if (math.tan(number1) == 0):
                    errWindow("Cotg 0 neni definovan")
                    return 2
                stack.push((1/math.tan(number1)))
            elif (operation == "log"):
                stack.push(math.log10(number1))
            elif (operation == "ln"):
                stack.push(math.log(number1))
            else:
                number2 = stack.pop()
                if (operation == "+"):
                    stack.push(number1 + number2)
                elif (operation == "-"):
                    stack.push(number2 - number1)
                elif (operation == "*"):
                    stack.push(number1 * number2)
                elif (operation == "/"):
                    if (number1 == 0):
                        errWindow("Nelze delit nulou")
                        return 2
                    stack.push(number2 / number1)
                elif (operation == "^"):
                    stack.push(math.pow(number2, number1))
            return "a"              #a stands for again
        elif (tmp == "<"):
            stack.push(item)
            return True
        elif (tmp == "="):
            stack.remove(stack.getIndexOfTopTerm())
            return True
        elif (tmp == "end"):
            return True
        else:
            return False
    except:
        return False
    
    
def solveProblem(problem, stack, precTable):
    """!@brief Funkce zpracuje znak, podle ktereho zavola fci evalRule s pozadovanymi parametry.
        @param problem Obsahuje matematicky vyraz zadany uzivatelem.
        @param stack Zasobnik.
        @param precTable Precedencni tabulka tvorena dvojrozmernym polem
    """
    global system    
    index = 0
    for i in problem:
        retVal = "a"
        if (i == "+"):
            index = 0
        elif (i == "-"):
            index = 1
        elif (i == "*"):
            index = 2
        elif (i == "/"):
            index = 3
        elif (i == "^"):
            index = 4
        elif (i == "sin"):
            index = 5
        elif (i == "cos"):
            index = 6
        elif (i == "tan"):
            index = 7
        elif (i == "cotg"):
            index = 8
        elif (i == "log"):
            index = 9
        elif (i == "ln"):
            index = 10
        elif (isNumber(i)):
            stack.push(float(i))
            continue
        elif (i == "("):
            index = 12
        elif (i == ")"):
            index = 13
        elif (i == "$"):
            index = 14
        elif (i == "!"):
            index = factorial(stack.pop())         #zde je index pouzit jako pomocna promenna na ulozeni hodnoty
            stack.push(index)
            continue
        
        while (retVal == "a"):
            retVal = evalRule(index, stack, precTable, i)            
        if (not retVal):
            return False
        elif (retVal == 2):
            return 2
    return True
 
def appendText(text):
    """!@brief Funkce slouzici k pripojeni textu pro vypis na "display" kalkulacky.
        @param text Obsahuje text ktery se ma vypsat na "display".
    """
    global isResult, string
    if (isResult):
        stack.clear()
        if (isNumber(text) or text == "(" or ((text in scientificButtonsName) and not text == " ! ")):
            string.set(text)
        else:
            string.set("0")
        isResult = False
        return
    tmp = string.get()
    if ((tmp[-1] == "0") and (re.search("\d", text))):
        if (len(tmp) > 1):
            if (tmp[-2] == " "):
                string.set(tmp[:-1] + text)
            else:
                string.set(tmp + text)
        else:
            string.set(text)
    elif ((re.search("\s0$", tmp) or re.search("^0$", tmp)) and ((text in scientificButtonsName) or (text == " ( ")) and (not text == "!")):
        string.set(tmp[:-1] + text)
    else:
        string.set(tmp + text) 

def insertDot():
    """!@brief Obstarava vypis tecky na display. Provadi osetreni vice tecek v jednom cisle a zamezuje vypisu cisla ve tvaru .125
    """
    global string
    if (re.search("\d+\.\d*$", string.get())):
        print "chyba"
        return False
    elif (re.search("\d$", string.get())):
        appendText(".")
    else:
        appendText("0.")

        
def negation():
    """!@brief Funkce pro otoceni znamenka cisla. Provadi osetreni obraceni znamenka doposud neexistujiciho cisla.
    """
    global string        
    if (re.search("-\d+\.?\d*$", string.get())):
        tmp = string.get()
        tmp = tmp.split(" ")
        tmp[-1] = tmp[-1].replace("-", "")
        string.set(" ".join(tmp))
    elif (re.search("\d+\.?\d*$", string.get())):
        tmp = string.get()
        tmp = tmp.split(" ")
        tmp[-1] = "-" + tmp[-1]
        string.set(" ".join(tmp))
    else:
        print "chyba"
        return False
        
def clear():
    """!@brief Vymaze obsah displaye
    """
    global string
    stack.clear()
    string.set("0")
    
def getResult():
    """!@brief Vyhodnoti matematicky problem a v pripade spravneho zadani prikladu vypise vysledek na display.
    """
    global string, isResult
    array = re.split(" ", string.get())
    array = filter(None, array)
    array.append("$")
    stack.push("$")
    tmp = solveProblem(array, stack, precTable)
    if (not tmp):
        print "chyba"
    elif (tmp == 2):
        return
    else:
        if (stack.size() > 2 or stack.top() == "$"):
            errWindow("Chybny vyraz!")
            stack.clear()
        else:
            isResult = True
            result = str(stack.top())
            string.set(result)
        
def delete():
    """!@brief Smazani znaku (ci funkce) z displaye.
    """
    global string, system, isResult
    if (isResult):
        string.set("0")
        isResult = False
    else:
        tmp = string.get()
        tmp = tmp.split(" ")
        tmp = filter(None, tmp)
        try:
            if (system == 16):
                int(tmp[-1], 16)
            else:
                float(tmp[-1])
            tmp[-1] = tmp[-1][:-1]
        except:
            del tmp[-1]
        try:    
            if (tmp[0] == "" or tmp[0] == "("):
                tmp = "0"
        except:
            tmp = "0"
        string.set(" ".join(tmp))
  

isResult = False   
stack = Stack()
#                  +    -     *    /    ^  sin  cos  tan  cotg log  ln    id  (     )    $
precTable = {"+":[">", ">", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "-":[">", ">", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "*":[">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "/":[">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "^":[">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "sin":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "cos":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "tan":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "cotg":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "log":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "ln":[">", ">", ">", ">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", ">"],
             "id":[">", ">", ">", ">", ">", "n", "n", "n", "n", "n", "n", "n", "n", ">", ">"],
             "(":["<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "=", "n"],
             ")":[">", ">", ">", ">", ">", ">", ">", ">", ">", ">", ">", "n", "n", ">", ">"],
             "$":["<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "n", "end"]}
             
string = StringVar()             
string.set("0")