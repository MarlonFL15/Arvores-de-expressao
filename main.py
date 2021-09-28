from functions import resolve
from functions import createTree

print(resolve('(50 / (5+5)) + 9 - (2*2)'))

r = createTree('(50 / (5+5)) + 9 - (2*2)')
print(r.resolve())