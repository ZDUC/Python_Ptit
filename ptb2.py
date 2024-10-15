import math
a,b,c=[int(x) for x in input().split()]
delta=b*b-4*a*c
if delta<0 : print("ptvn")
elif delta==0 : print((-b/2*a))
else : print(((-b-math.sqrt(delta))/(2*a)), "and", ((-b+math.sqrt(delta))/(2*a)))