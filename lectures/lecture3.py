"""
for i in ['Hiroki', 'John', 'Jess']:
    print('Hello, ' + i + '!')
print('***')
"""
# Python is designed with readability in mind.
# That's why it's based on spacing instead of brakets.

from pylab import *

# Create a list of sin(x)
# for x = 0, 0.1, 0.2, ..., 3.0
ans = []
for x in arange(0, 3.1, 0.1):
    ans.append(sin(x))
print(ans)

domain = arange(0, 4*pi, 0.01)
result = [sin(x) for x in domain if -sin(x) > 0]
#print(result)

#It's important to specify a domain as well!

plot(result)

# Initialization
knowledge = 100.

# Updating
def update(ck):           # ck = current knowledge
    tk = ck + 1.          # daily acquisition
    if random() <  0.01: # accident
        tk *= 0.5
    tk = (1. - 0.01) * tk # loss by sleep
    return tk             # tk = tomorrow's knowledge
# Observation
result = [knowledge]
for t in range(365):
    knowledge = update(knowledge)
    result.append(knowledge)
plot(result)