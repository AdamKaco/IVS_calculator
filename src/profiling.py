import sys 
import re
import mathlib




i = 0
j = 0
k = 0
ans_x = 0
nmbs = []
#with open ('nmb_10000.txt') as file:
#    sys.stdin = file
for line in sys.stdin:
    nmbs = nmbs + re.findall(r"\d+", line)

#slower by 68% and not working correctly
"""
for line in sys.stdin:
    lengh = len(line)

    for j in range (0, lengh):
        if (line[j] == " "):
            k = mathlib.sum(k, 1)
            nmbs.append(0)
        elif(line[j+1] == " " or j+1 == lengh):
            nmbs[k] = mathlib.sum(nmbs[k], int(line[j]))
        else:
            nmbs[k] = mathlib.sum(nmbs[k], int(line[j]))
            nmbs[k] = mathlib.mul(nmbs[k], 10)
"""


for nmb in nmbs:
    ans_x = mathlib.sum(ans_x, int(nmb))
    i = mathlib.sum(i,1)

ans_x = mathlib.div(ans_x,i)
print ("x =", ans_x)

#smerodajna odchylka vypocet
ans_s = 0
for nmb in nmbs:
    ans_s = mathlib.sum(ans_s, mathlib.exp(int(nmb),2))
ans_s = mathlib.sub(ans_s, mathlib.mul(i,mathlib.exp(ans_x,2)))
i = mathlib.sub(i,1)
ans_s = mathlib.div(ans_s,i)
ans_s = mathlib.root(2, ans_s)

print ("s =", round(ans_s, 4))


