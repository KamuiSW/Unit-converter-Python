import math

UsableTypeSmall = ['yocto','zepto','atto','femto','pico','nano','micro','mili','centi','deci']
UsableTypeBig = ['deka','hecto','kilo','mega','giga','tera','peta','exa','zetta','yotta', 'none']

def CheckAvaible():
    global InputUnit 
    InputUnit = input("input unit: ")
    
    if InputUnit in UsableTypeSmall:
        CalcToOrgSmall()
    elif InputUnit in UsableTypeBig:
        CalcToOrgBig()
    else:
        print('error no value found')

def InputNumbers():
    global InputNumb
    InputNumb = float(input("input desired number: "))
    CheckAvaible()
    
def EndUnitInput():
    global EndUnit
    EndUnit = input("input convert unit: ")
    
    if EndUnit in UsableTypeSmall:
        CalcToFinalSmall()
    elif EndUnit in UsableTypeBig:
        CalcToFinalBig()
    else:
        print('error no value found')

#big numbers
def CalcToOrgBig():
    global OrgNumbPublic
    if InputUnit == 'yotta':
        OrgNumb = InputNumb * 10**24
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'zetta':
        OrgNumb = InputNumb * 10**21
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'exa':
        OrgNumb = InputNumb * 10**18
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'peta':
        OrgNumb = InputNumb * 10**15
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'tera':
        OrgNumb = InputNumb * 10**12
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'giga':
        OrgNumb = InputNumb * 10**9
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'mega':
        OrgNumb = InputNumb * 10**6
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'kilo':
        OrgNumb = InputNumb * 10**3
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'hecto':
        OrgNumb = InputNumb * 10**2
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'deka':
        OrgNumb = InputNumb * 10
        OrgNumbPublic = float(OrgNumb)
    elif InputUnit == 'none':
        OrgNumb = InputNumb * 1
        OrgNumbPublic = float(OrgNumb)
    else:
        print('failed to get unit')
        return
    EndUnitInput()

def CalcToFinalBig():
    
    if InputUnit == 'yotta':
        FinalNumb = OrgNumbPublic / 10**24
        print(FinalNumb)
    elif InputUnit == 'zetta':
        FinalNumb = OrgNumbPublic / 10**21
        print(FinalNumb)
    elif InputUnit == 'exa':
        FinalNumb = OrgNumbPublic / 10**18
        print(FinalNumb)        
    elif InputUnit == 'peta':
        FinalNumb = OrgNumbPublic / 10**15
        print(FinalNumb)
    elif InputUnit == 'tera':
        FinalNumb = OrgNumbPublic / 10**12
        print(FinalNumb)
    elif InputUnit == 'giga':
        FinalNumb = OrgNumbPublic / 10**9
        print(FinalNumb)
    elif InputUnit == 'mega':
        FinalNumb = OrgNumbPublic / 10**6
        print(FinalNumb)
    elif InputUnit == 'kilo':
        FinalNumb = OrgNumbPublic / 10**3
        print(FinalNumb)
    elif InputUnit == 'hecto':
        FinalNumb = OrgNumbPublic / 10**2
        print(FinalNumb)
    elif InputUnit == 'deka':
        FinalNumb = OrgNumbPublic / 10
        print(FinalNumb)

#smaller numbers
def CalcToOrgSmall():
    global OrgNumbPublic
    if InputUnit == 'deci':
        OrgNumb = InputNumb * 10**-1
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'centi':
        OrgNumb = InputNumb * 10**-2
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'mili':
        OrgNumb = InputNumb * 10**-3
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'micro':
        OrgNumb = InputNumb * 10**-6
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'nano':
        OrgNumb = InputNumb * 10**-9
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'pico':
        OrgNumb = InputNumb * 10**-12
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'femto':
        OrgNumb = InputNumb * 10**-15
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'atto':
        OrgNumb = InputNumb * 10**-18
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'zepto':
        OrgNumb = InputNumb * 10**-21
        OrgNumbPublic = OrgNumb
    elif InputUnit == 'yocto':
        OrgNumb = InputNumb * 10**-24
        OrgNumbPublic = OrgNumb
    EndUnitInput()

def CalcToFinalSmall():
    if InputUnit == 'deci':
        FinalNumb = OrgNumbPublic / 10**-1
        print(FinalNumb)
    elif InputUnit == 'centi':
        FinalNumb = OrgNumbPublic / 10**-2
        print(FinalNumb)
    elif InputUnit == 'mili':
        FinalNumb = OrgNumbPublic / 10**-3
        print(FinalNumb)
    elif InputUnit == 'micro':
        FinalNumb = OrgNumbPublic / 10**-6
        print(FinalNumb)
    elif InputUnit == 'nano':
        FinalNumb = OrgNumbPublic / 10**-9
        print(FinalNumb)
    elif InputUnit == 'pico':
        FinalNumb = OrgNumbPublic / 10**-12
        print(FinalNumb)
    elif InputUnit == 'femto':
        FinalNumb = OrgNumbPublic / 10**-15
        print(FinalNumb)
    elif InputUnit == 'atto':
        FinalNumb = OrgNumbPublic / 10**-18
        print(FinalNumb)
    elif InputUnit == 'zepto':
        FinalNumb = OrgNumbPublic / 10**-21
        print(FinalNumb)
    elif InputUnit == 'yocto':
        FinalNumb = OrgNumbPublic / 10**-24
        print(FinalNumb)
        
while True:
    InputNumbers()
    
