from math import *
#constants:
g = 9.81

#setting every possible attribute:
l=0
t=0
D=0
m=0
maximaleAuslenkung = 0
f=0


#gegeben:
maximaleAuslenkung = 0.2 #muss in Aufgabe gegeben werden
l = 1 #muss in Aufgabe gegeben werden
t = 0#bei t = 0 max geschwindigkeit  weil cos(0) = max
f = 0.5

def getT(modus):
    if f != 0:
        return 1 / f
    else:
        if "pendel" in modus:
            return 2 * pi * sqrt(l/g)
        elif "gali" in modus:
            return 2 * pi * sqrt(0.5*l/g)
        elif "feder" in modus:
            return 2 * pi * sqrt(m/D)

#rechnen:
T = getT("pendel")
w = 2 * pi / T
s = maximaleAuslenkung * sin(w*t)       #s(t)
v = maximaleAuslenkung * cos(w*t)*w     #v(t)
a = maximaleAuslenkung * -sin(w*t)*w*w  #a(t)



#calc in a loop the change over time

print(f"Periodendauer T:  {round(T,2)}")
print(f"w:  {round(w,2)}")
print(f"s(t) bei s({t}):  {round(s,2)}")
print(f"v(t) bei v({t}):  {round(v,2)}")
print(f"a(t) bei a({t}):  {round(a,2)}")
