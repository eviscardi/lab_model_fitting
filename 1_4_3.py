def f(x):
    y = x**2 - 4*x + 4
    return y

# val = []    
# for x in range(-20,20):
#     val.append(f(x))
# print x

least = f(-20) 
for z in range(-20,21):
    if f(z) < least:
            least = f(z)
            leastx = z
print leastx