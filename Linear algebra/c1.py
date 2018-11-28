import re

c = [[1,2,3],[1,2,3]]

a = re.sub(r',',' ',('[\n'+' \n'.join(str(e) for e in c)+'\n]'))
print(a)
