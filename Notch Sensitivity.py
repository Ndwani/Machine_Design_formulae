import math
Variables = {"notch radius":0, "ultimate strength" :0}
for i,j in Variables.items():
    Variables[i] = float(input("Input " + str(i)+ " : "))

Values = list(Variables.values())

Nc = 0


while True:
    Question = input('is this for bending or torsion? B or T? :')

    
    if Question.lower() == 'b':

        Nb =float(0.246-3.08*pow(10,-3)*Values[1] + 1.51*pow(10,-5)*pow(Values[1],2) - 2.67*pow(-10,-8)*pow(Values[1],3))

        Nc = math.sqrt(Nb)

        break
    elif Question.lower() == 't':

        Nt =float(0.190 -2.51*pow(10,-3)*Values[1] + 1.35*pow(10,-5)*pow(Values[1],2) - 2.67*pow(10,-8)*pow(Values[1],3))
        
        Nc = math.sqrt(Nt)

        break
    else:
        print('error wrong input try again. \n')

def NotchSen(a,r):

    R = float(math.sqrt(r))
    Q = round(1/(1+(a/R)),2)
    return Q
    
print(NotchSen(Nc,Values[0]))
