import math

UsableTypeSmall = ['yocto','zepto','atto','femto','pico','nano','micro','mili','centi','deci']
UsableTypeBig = ['deka','hecto','kilo','mega','giga','tera','peta','exa','zetta','yotta']

InputUnit = 1
InputNumb = ''
OrgNumbPublic = ''

def InputNumbers():
    InputNumb1 = float(input("input desired number: "))
    InputNumb = InputNumb1
    CheckAvaible()

#big numbers
def CalcToOrgBig():
    if InputUnit == 'yotta':
        OrgNumb = InputNumb * 10^24
    elif InputUnit == 'zetta':
        OrgNumb = InputNumb * 10^21
    elif InputUnit == 'exa':
        OrgNumb = InputNumb * 10^18
    elif InputUnit == 'peta':
        OrgNumb = InputNumb * 10^15
    elif InputUnit == 'tera':
        OrgNumb = InputNumb * 10^12
    elif InputUnit == 'giga':
        OrgNumb = InputNumb * 10^9
    elif InputUnit == 'mega':
        OrgNumb = InputNumb * 10^6
    elif InputUnit == 'kilo':
        OrgNumb = InputNumb * 10^3
    elif InputUnit == 'hecto':
        OrgNumb = InputNumb * 10^2
    elif InputUnit == 'deka':
        OrgNumb = InputNumb * 10
    print(InputNumb)
    OrgNumbPublic = OrgNumb
        
    CalcToFinalBig()

def CalcToFinalBig():
    
    if InputUnit == 'yotta':
        FinalNumb = OrgNumbPublic / 10^24
    elif InputUnit == 'zetta':
        FinalNumb = OrgNumbPublic / 10^21
    elif InputUnit == 'exa':
        FinalNumb = OrgNumbPublic / 10^18
    elif InputUnit == 'peta':
        FinalNumb = OrgNumbPublic / 10^15
    elif InputUnit == 'tera':
        FinalNumb = OrgNumbPublic / 10^12
    elif InputUnit == 'giga':
        FinalNumb = OrgNumbPublic / 10^9
    elif InputUnit == 'mega':
        FinalNumb = OrgNumbPublic / 10^6
    elif InputUnit == 'kilo':
        FinalNumb = OrgNumbPublic / 10^3
    elif InputUnit == 'hecto':
        FinalNumb = OrgNumbPublic / 10^2
    elif InputUnit == 'deka':
        FinalNumb = OrgNumbPublic / 10
    print(OrgNumbPublic)

#smaller numbers
def CalcToOrgSmall():
    if InputUnit == 'deci':
        OrgNumb = InputNumb * 10^-1
    elif InputUnit == 'centi':
        OrgNumb = InputNumb * 10^-2
    elif InputUnit == 'mili':
        OrgNumb = InputNumb * 10^-3
    elif InputUnit == 'micro':
        OrgNumb = InputNumb * 10^-6
    elif InputUnit == 'nano':
        OrgNumb = InputNumb * 10^-9
    elif InputUnit == 'pico':
        OrgNumb = InputNumb * 10^-12
    elif InputUnit == 'femto':
        OrgNumb = InputNumb * 10^-15
    elif InputUnit == 'atto':
        OrgNumb = InputNumb * 10^-18
    elif InputUnit == 'zepto':
        OrgNumb = InputNumb * 10^-21
    elif InputUnit == 'yocto':
        OrgNumb = InputNumb * 10^-24
        
    CalcToFinalSmall()

def CalcToFinalSmall():
    if InputUnit == 'deci':
        FinalNumb = OrgNumb / 10^-1
    elif InputUnit == 'centi':
        FinalNumb = OrgNumb / 10^-2
    elif InputUnit == 'mili':
        FinalNumb = OrgNumb / 10^-3
    elif InputUnit == 'micro':
        FinalNumb = OrgNumb / 10^-6
    elif InputUnit == 'nano':
        FinalNumb = OrgNumb / 10^-9
    elif InputUnit == 'pico':
        FinalNumb = OrgNumb / 10^-12
    elif InputUnit == 'femto':
        FinalNumb = OrgNumb / 10^-15
    elif InputUnit == 'atto':
        FinalNumb = OrgNumb / 10^-18
    elif InputUnit == 'zepto':
        FinalNumb = OrgNumb / 10^-21
    elif InputUnit == 'yocto':
        FinalNumb = OrgNumb / 10^-24
        
    print(FinalNumb)
    
def CheckAvaible():
    InputUnit = input("input unit: ")
    
    if InputUnit in UsableTypeSmall:
        CalcToOrgSmall()
    elif InputUnit in UsableTypeBig:
        CalcToOrgBig()
    else:
        print('error no value found')
        
while True:
    InputNumbers()
    
