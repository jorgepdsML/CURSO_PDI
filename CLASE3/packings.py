l=[20,30,40]
def promedio(a,b,c):
    d=(a+b+c)/3
    return d
v=promedio(20,30,40)
print("VALOR PROMEDIO :",v)
v2=promedio(*l)
print("VALOR PROMEDIO :",v2)

