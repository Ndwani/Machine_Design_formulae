import math


#PARAMETERS
Variables = {'Grip length':0,'E- Modulus(Mlbf)':0, 'Nominal Diameter':0, 'Thickness of frustrum': 0}
for i,j in Variables.items():
     Variables[i]= float(input('Input the ' + str(i) + ' : ')) #this were the values entered by user will be assigned to each variable
    

Values = (list(Variables.values())) #stores the Values above in the same order as the variables in the variable dictionary
R = float((math.pi*30)/180) #Coverting 30 degress to radians
Epow = float(input('what power is E- Modulus raised to? :')) #exponent value 
Ask = input('Are the materials the same? Y or N : ') 
    

#FUNTIONS

def MatstiffSame(g,E,N): #if the clamped materials are the same
    A = (0.5777*g + 0.5*N)
    B = (0.557*g + 2.5*N)
    Km = round((0.5774*math.pi*E*N)/(2*math.log(5*(A/B),math.e)), 3)
     
    return Km

def MatstiffDiff(g,E,N,t): #if the clamped materials differ
     ask1 = input('is this frustrum in between? Y or N : ')
     if ask1.lower() == 'n':
          Dw = 1.5*N # washer diameter is 1.5 times the nominal diameter
     else:
          ask2= float(input('Enter the thickness of top or bottom frustrum : '))
          Dw = (1.5*N) + 2*ask2*math.tan(R)
     #C = float(math.tan(R))
     A = (g*t + Dw - N)*(Dw + N)
     B = ((g*t + Dw + N)*(Dw - N))
     Km = round((0.5774*math.pi*E*N)/(math.log((A/B),math.e)), 3)
     return Km

#RESULTS

if Ask.lower() == 'y':
     
     print(str(MatstiffSame(Values[0],(Values[1]* pow(10,Epow)),Values[2])) + " lbf/in")
     print('or\n')
     print(str(MatstiffSame(Values[0],Values[1],Values[2])) + " Mlbf/in")
else:
     print(str(MatstiffDiff(Values[0],(Values[1]* pow(10,Epow)),Values[2],Values[3])) + " lbf/in")
     print('or\n')
     print(str(MatstiffDiff(Values[0],Values[1],Values[2],Values[3])) + " Mlbf/in")
