import requests

def proccess_mass(inp):
    if len(inp) == 1:
        return str(inp[0])
    return str(inp)

def proccess_type(inp):
    return inp

def printElement3(*args):
    print("new Element(", end="")
    for i in range(len(args)-1):
        print(args[i], end=", ")
    print(args[len(args)-1] + ");")

def printElement2(el, name):
    printElement3(name, "caca")


def printElement(el, name):
    return 'new Element("' + el['symbol'] + '", ' + str(el['atomicNumber']) + ', "' + proccess_type(el['groupBlock']) + '", "' + name + '", ' + proccess_mass(el['atomicMass']) + ', "' + el['electronicConfiguration'] + '", "' + el['standardState'] + '"),\n'

req = "https://neelpatel05.pythonanywhere.com"
r = requests.get(req)
if r.status_code == 200:
    obj = r.json()
    f = open("names_cat.csv", "r")
    text = f.read()
    names = text.split(",")
    
    res = ''
    for i, it in enumerate(obj):
        res += printElement(it, names[i])

    f = open("result.txt", "w")
    f.write(res)
    f.close()
else:
    print("Error " + str(r.status_code))