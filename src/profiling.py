import sys
import re
import mathlib
import sys

file = open("input_data_prof_10000.txt")
sys.stdin = file

i = 0
ans_x = 0
nmbs = []

for line in sys.stdin:
    nmbs = re.findall(r"\d+", line)

for nmb in nmbs:
    ans_x = mathlib.sum(ans_x, int(nmb))
    i = mathlib.sum(i,1)

ans_x = mathlib.div(ans_x,i)
print (ans_x)

ans_s = 0
for nmb in nmbs:
    ans_s = mathlib.sum(ans_s, mathlib.exp(int(nmb),2))
ans_s = mathlib.sub(ans_s, mathlib.mul(i,mathlib.exp(ans_x,2)))
i = mathlib.sub(i,1)
ans_s = mathlib.div(ans_s,i)
ans_s = mathlib.root(ans_s,2)
print (round(ans_s, 4))


