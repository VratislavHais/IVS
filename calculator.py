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


def errWindow(text):
    """!@brief Vytvori okno s chybovou hlaskou.
       @param text Chybova hlaska ktera se ma zobrazit.
    """
    stack.clear()
    box.showerror("Error", text)
    
    
def infoWindow(label, text):
    """!@brief Vytvori okno s infem.
       @param label Pojmenovani okna.
       @param text Zobrazovany text.
    """
    box.showinfo(label, text)
    
    
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
            #nejaka pekna chybova hlaska -> nemelo by k tomu dojit
            return False
        elif (retVal == 2):
            return 2
    return True
 
def appendText(text):
    """!@brief Funkce slouzici k pripojeni textu pro vypis na "display" kalkulacky.
        @param text Obsahuje text ktery se ma vypsat na "display".
    """
    global isResult, string, memButtons
    if (isResult):
        memButtons[2].config(state = DISABLED)
        stack.clear()
        if (isNumber(text) or text == "(" or ((text in scientificButtonsName) and not text == " ! ")):
            string.set(text)
        else:
            string.set("0")
        isResult = False
        return
    tmp = string.get()
    if ((tmp[-1] == "0") and (re.search("\d", text) or re.search("[a|b|c|d|e|f]", text))):
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
        errWindow("Do desetinneho cisla neni mozne\n pridat desetinnou tecku!")
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
        errWindow("Obratit znamenko se da pouze u cisla")
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
    global string, isResult, memButtons
    array = re.split(" ", string.get())
    array = filter(None, array)
    array.append("$")
    stack.push("$")
    tmp = solveProblem(array, stack, precTable)
    if (not tmp):
        errWindow("Chybny vyraz!")
    elif (tmp == 2):
        return
    else:
        if (stack.size() > 2 or stack.top() == "$"):
            errWindow("Chybny vyraz!")
            stack.clear()
        else:
            memButtons[2].config(state = NORMAL)
            isResult = True
            result = str(stack.top())
            string.set(result)
        
def delete():
    """!@brief Smazani znaku (ci funkce) z displaye.
    """
    global string, isResult
    if (isResult):
        string.set("0")
        isResult = False
    else:
        tmp = string.get()
        tmp = tmp.split(" ")
        tmp = filter(None, tmp)
        try:
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
    
def basic():
    """!@brief Slouzi ke skryti tlacitek z vedecke kalkulacky.
    """
    global scientificButtons, buttons
    for i in scientificButtons:
        i.grid_forget()
        
        
def scientific():
    """!@brief Zobrazi tlacitka vedecke kalkulacky.
    """
    global scientificButtons, buttons
    decimal()
    col = 4
    row = 1
    for i in scientificButtons:
        i.grid(row = row, column = col, sticky = W + E)
        row += 1
        if (row > 5):
            row = 1
            col += 1
            
def evalGraf(axisX, axisY):   
    """!@brief Vykresli graf ze zadanych hodnot.
        @param axisX Uzivatelem zadane hodnoty osy x.
        @param axisY Uzivatelem zadane hodnoty osy y.
    """       
    pass    
    """plt.xlabel("x"+r"$ \rightarrow $")
    plt.ylabel("y"+r"$ \rightarrow $")
    axisX = axisX.split(",")
    axisY = axisY.split(",")
    try:
        xAxis = []
        for i in axisX:
            xAxis.append(float(i))
        yAxis = []
        for i in axisY:
            yAxis.append(float(i))
        plt.plot(xAxis, yAxis)
        plt.show()
    except:
        errWindow("Chybny vstup!")
        return False"""
        
def graf():
    """!@brief Otevre okno pro zadavani hodnot na vykresleni grafu
    """
    top = Toplevel()
    top.title("Graph")
    top.focus_set()
    Label(top, text = "Zadejte hodnoty na ose x:").grid(row = 0, column = 0)
    Label(top, text = "Zadejte hodnoty na ose y:").grid(row = 2, column = 0)
    entryX = Entry(top)
    entryX.grid(row = 1, column = 0)
    entryY = Entry(top)
    entryY.grid(row = 3, column = 0)
    Button(top, text="OK", command = lambda: evalGraf(entryX.get(), entryY.get())).grid(row = 4, column = 0)

def calculateBMI(mass, height):
    """!@brief Vypocita BMI z uzivatelem zadanych hodnot
        @param mass Uzivatelem zadana vaha
        @param height Uzivatelem zadana vyska
    """
    if (not isNumber(mass)):
        errWindow("Hmotnost musi byt cislo")
        return
    if (not isNumber(height)):
        errWindow("Vyska musi byt cislo")
        return
    mass = float(mass)
    height = float(height) / 100
    if (mass <= 0 or height <= 0):
        errWindow("Vyska i vaha musi byt vetsi nez 0")
        return
    result = mass / (height * height)
    if (result < 18.5):
        infoWindow("podvaha", "Kategorie:\tpodvaha\nZdravotni rizika:\tvysoka")
        return
    elif (result < 25):
        infoWindow("norma", "Kategorie:\tnorma\nZdravotni rizika:\tminimalni")
        return
    elif (result < 30):
        infoWindow("nadvaha", "Kategorie:\tnadvaha\nZdravotni rizika:\tnizka az lehce vyssi")
        return
    elif (result < 35):
        infoWindow("obezita 1. stupne", "Kategorie:\tobezita 1. stupne\nZdravotni rizika:\tzvysena")
        return
    elif (result < 40):
        infoWindow("obezita 2. stupne", "Kategorie:\tobezita 2. stupne\nZdravotni rizika:\tvysoka")
        return
    else:
        infoWindow("obezita 3. stupne", "Kategorie:\tobezita 3. stupne\nZdravotni rizika:\tvelmi vysoka")
        return
        
    

def bodyMassIndex():
    """!@brief Otevre okno pro zadavani hodnot na vypocet BMI
    """
    top = Toplevel()
    top.title("BMI")
    top.focus_set()
    Label(top, text = "Vyska: ").grid(row = 0, column = 0)
    Label(top, text = "cm").grid(row = 0, column = 3)
    Label(top, text = "Hmotnost :").grid(row = 1, column = 0)
    Label(top, text = "kg").grid(row = 1, column = 3)
    Label(top).grid(row = 2, column = 2)
    entryMass = Entry(top)
    entryMass.grid(row = 1, column = 2)
    entryHeight = Entry(top)
    entryHeight.grid(row = 0, column = 2)
    Button(top, text="OK", command = lambda: calculateBMI(entryMass.get(), entryHeight.get())).grid(row = 3, column = 0, columnspan = 3)

def helpMe():
    """!@brief Vypise napovedu
    """
    msg = "kalkulacka zvlada zpracovani slozitejsich vyrazu predem definovanych matematickych funkci.\n"
    msg += "Basic -> obsahuje zakladni matematicke funkce:\n"
    msg += "\t+ -> soucet cisel\n\t- -> rozdil dvou cisel\n\t* -> vynasobeni dvou cisel\n"
    msg += "\t/ -> podil dvou cisel\n\t^ -> umocneni (cislo ^ mocnina)\n\t() -> klasicke zavorky\n"
    msg += "\nScientific -> obsahuje zakladni a rozsirene matematicke funkce + 2 konstanty:\n"
    msg += "\tsin -> sinus cisla\n\tcos -> cosinus cisla\n\ttan -> tangens cisla\n\tcotg -> cotangens cisla\n"
    msg += "\tlog -> logaritmus o zakladu 10 z cisla\n\tln -> prirozeny logaritmus cisla\n\t"
    msg += "e -> eulerovo cislo (2.71828)\n\tπ -> ludolfovo cislo (3.14159)\n\t"
    msg += "graph -> vyskoci okno, do ktereho se zadaji hodnoty os x a y. Po stisknuti OK se vykresli graf\n"
    bmi = "\tBMI\t\tKategorie\t\tZdravotni rizika\n"
    bmi += "\t<18.5\t\tpodvaha\t\tvysoka\n"
    bmi += "\t18.5 - 24.9\tnorma\t\tminimalni\n"
    bmi += "\t25.0 - 29.9\tnadvaha\t\tnizka az lehce vyssi\n"
    bmi += "\t30.0 - 34.9\tobezita 1. stupne\tzvysena\n"
    bmi += "\t35.0 - 39.9\tobezita 2. stupne\tvysoka\n"
    bmi += "\t>40\t\tobezita 3. stupne\tvelmi vysoka"
    #infoWindow("Help", msg)
    top = Toplevel()
    top.title("Help")
    top.focus_set()
    Label(top, text = "Kalkulacka", fg = "green", font=("times new roman bold", 14), justify = CENTER).grid(row = 0, column = 0)
    Label(top, text=msg, justify = LEFT).grid(row = 1, column = 0)
    Label(top, text = "BMI", fg = "green", font=("times new roman bold", 14), justify = CENTER).grid(row = 2, column = 0)
    Label(top, text = bmi, justify = LEFT).grid(row = 3, column = 0)

def memClear():
    global memory
    memory = ""
    
def memSet():
    global memory, string
    memory = string.get() + " "    
    
def memRecal():
    global memory
    appendText(memory)
    

window = Tk()
window.title("Calculator")
window.resizable(width = False, height = False)
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
mainMenu = Menu(window)
menuCalculator = Menu(mainMenu, tearoff = 0)
menuCalculator.add_command(label="Basic", command = basic)
menuCalculator.add_command(label="Scientific", command = scientific)
menuCalculator.add_separator()
menuCalculator.add_command(label="Decimal", command = decimal)
menuCalculator.add_command(label="Octal", command = octal)
menuCalculator.add_command(label="Hexadecimal", command = hexadecimal)
menuCalculator.add_command(label="Binary", command = binary)
menuCalculator.add_separator()
menuCalculator.add_command(label="Exit", command = window.destroy)
mainMenu.add_cascade(label="Settings", menu=menuCalculator)

mainMenu.add_command(label="BMI", command = bodyMassIndex)
mainMenu.add_command(label = "Help", command = helpMe)

window.config(menu=mainMenu)

problemResultLabel = Label(window, textvariable = string, font=("times new roman bold", 12), anchor = E, bg="white", width = 20)
problemResultLabel.grid(row = 0, column = 0, pady=3, columnspan = 7, sticky = W + E)
buttonNames = [" ( ", " ) ", " ^ ", " / ", "7", "8", "9", " * ", "4", "5", "6", " - ", "1", "2", "3", " + ", "0", ".", "+/-", "C", "=", "←"]
scientificButtonsName = [" sin ", " cos ", " tan ", " cotg ", " ! ", " log ", " ln "]
buttons = []
scientificButtons = []
counter = 0
for row in range(4):
    for col in range(4):
        buttons.append(Button(window, text = buttonNames[4 * row + col], width = 5, height = 1, command = lambda name=buttonNames[4*row + col]:appendText(name)))
        buttons[counter].grid(row = (row + 1), column = col, sticky = W + E)
        counter += 1
buttons.append(Button(window, text = buttonNames[16], width = 5, height = 1, command = lambda name=buttonNames[16]:appendText(name)))
buttons[counter].grid(row = 5, column = 0, columnspan = 2, sticky = W + E)
counter += 1
buttons.append(Button(window, text = buttonNames[17], width = 5, height = 1, command = insertDot))
buttons[counter].grid(row = 5, column = 2, sticky = W + E)
counter += 1
buttons.append(Button(window, text = buttonNames[18], width = 5, height = 1, command = negation))
buttons[counter].grid(row = 5, column = 3, sticky = W + E)
counter += 1
buttons.append(Button(window, text = buttonNames[19], width = 3, height = 3, command = clear))
buttons[counter].grid(row = 2, column = 6, sticky = W + E + S + W, rowspan = 2)
counter += 1
buttons.append(Button(window, text = buttonNames[20], width = 3, height = 3, command = getResult))
buttons[counter].grid(row = 4, column = 6, sticky = W + E + S + W, rowspan = 2)
counter += 1
buttons.append(Button(window, text = buttonNames[21], width = 3, height = 1, command = delete))
buttons[counter].grid(row = 1, column = 6, sticky = W + E + S + W)
memory = ""
memButtons = []
memButtons.append(Button(window, text = "MR", width = 3, height = 1, command = memRecal))
memButtons[0].grid(row = 8, column = 2, sticky = W + E + S + W)
memButtons.append(Button(window, text = "MC", width = 3, height = 1, command = memClear))
memButtons[1].grid(row = 8, column = 1, sticky = W + E + S + W)
memButtons.append(Button(window, text = "MS", width = 3, height = 1, command = memSet, state = DISABLED))
memButtons[2].grid(row = 8, column = 3, sticky = W + E + S + W)


for i in scientificButtonsName:
    scientificButtons.append(Button(window, text = i, width = 5, height = 1, command = lambda name=i:appendText(name)))
scientificButtons.append(Button(window, text = "e", width = 5, height = 1, command = lambda name = " 2.71828 ":appendText(name)))
scientificButtons.append(Button(window, text = "π", width = 5, height = 1, command = lambda name = " 3.14159 ":appendText(name)))
scientificButtons.append(Button(window, text = "graph", width = 5, height = 1, command = graf, state = DISABLED))

hexButtons = []
hexButtons.append(Button(window, text = "A", width = 5, height = 1, command = lambda name = "a":appendText(name)))
hexButtons.append(Button(window, text = "B", width = 5, height = 1, command = lambda name = "b":appendText(name)))
hexButtons.append(Button(window, text = "C", width = 5, height = 1, command = lambda name = "c":appendText(name)))
hexButtons.append(Button(window, text = "D", width = 5, height = 1, command = lambda name = "d":appendText(name)))
hexButtons.append(Button(window, text = "E", width = 5, height = 1, command = lambda name = "e":appendText(name)))
hexButtons.append(Button(window, text = "F", width = 5, height = 1, command = lambda name = "f":appendText(name)))


window.mainloop()
