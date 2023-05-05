
Constants = {'a':0,'b':0,'Ultimate strength Value only':0}
for i,j in Constants.items():
    Constants[i] = float(input(" Enter " + str(i) + " constant: "))


Jar = list(Constants.values())

Ka = Jar[0]*pow(Jar[2],Jar[1])
print(round(Ka,2))
                         
