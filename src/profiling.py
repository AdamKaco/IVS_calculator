import sys
import re

i = 0
ans_x = 0
nmbs = []

for line in sys.stdin:
    nmbs = re.findall(r"\d+", line)

for nmb in nmbs:
    ans_x = ans_x + int (nmb) #call our function
    i += 1

ans_x = ans_x/i #call our function
print (ans_x)