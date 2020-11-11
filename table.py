import requests

def proccess_mass(inp):
    if len(inp) == 1:
        return str(inp[0])
    return str(inp)

def proccess_type(inp):

    inp = str(inp)

    if inp == "nonmetal":
        inp = "no metàlic"
    elif inp == "noble gas":
        inp = "gas noble"
    elif inp == "post-transition metal":
        inp = "metall post-transició"
    elif inp == "transition metal":
        inp = "metall de transició"
    elif inp == "actinoid":
        inp = "actinoide"
    elif inp == "alkaline earth metal":
        inp = "metall alcalino-terrós"
    elif inp == "alkali metal":
        inp = "metall alcalí"
    elif inp == "halogen":
        inp = "halògen"
    elif inp == "metalloid":
        inp = "metal·loide"
    elif inp == "lantanoid":
        inp = "lantanoide"

    return inp

def proccess_state(inp):
    if inp == "solid":
        inp = "sòlid"
    elif inp == "":
        inp = "sintètic"
    elif inp == "liquid":
        inp = "líquid"

    return inp



def printElement3(*args):
    print("new Element(", end="")
    for i in range(len(args)-1):
        print(args[i], end=", ")
    print(args[len(args)-1] + ");")

def printElement2(el, name):
    printElement3(name, "caca")


def printElement(el, name):
    return 'new Element("' + el['symbol'] + '", ' + str(el['atomicNumber']) + ', "' + proccess_type(el['groupBlock']) + '", "' + name + '", "' + proccess_mass(el['atomicMass']) + '", "' + el['electronicConfiguration'] + '", "' + proccess_state(el['standardState']) + '"),\n'

req = "https://neelpatel05.pythonanywhere.com"
r = requests.get(req)
if r.status_code == 200:
    obj = r.json()
    f = open("names_cat.csv", "r", encoding="utf-8")
    text = f.read()
    names = text.split(",")
    
    res = ''
    for i, it in enumerate(obj):
        res += printElement(it, names[i])

    f = open("result.txt", "w", encoding="utf-8")
    f.write(res)
    f.close()
else:
    print("Error " + str(r.status_code))