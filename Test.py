# -*- coding: utf-8 -*-

from recommendations import critics

print(critics['Lisa Rose']['Lady in the Water'])

print(critics['Toby']['Snakes on a Plane'])

print(critics['Toby'])


from math import sqrt
print(sqrt(pow(4.5-4,2)+pow(2-1,2)))

print(1/sqrt(pow(4.5-4,2)+pow(2-1,2)))

print(1/(1+sqrt(pow(4.5-4,2)+pow(2-1,2))))

ttt={'aa':{'a':0,'b':1},'bb':{'a':11,'b':22}}

print('test')

sum1 = sum(ttt['aa'][item]
            for item in ttt['aa'] if item in ttt['bb'])
print("sum1:",sum1)

print(ttt['aa']['a'])

for key in ttt:
    print(key)