import sys
def m_on_marc(x,y,z):
    for p in range(0,z):
        x=x+1
        print(x*y)
t = int(sys.stdin.readline())
f = float(sys.stdin.readline())
g = int(sys.stdin.readline())
m_on_marc(t,f,g)