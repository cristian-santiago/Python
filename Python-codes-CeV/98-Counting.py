'''
Make a count function with 3 parameters: init, end, pass.

a) 1 to 10, one by one
b) 10 to 0, two by two
c) a custom count


'''




a = list()

e =list()
i = int(input("Insert the initial value: "))
p = int(input("Insert the pass value: "))
e = int(input("Insert the final value: "))

l = list()


def v_up(x, y, z):
    r = i
    while True:
        l.append(r)
    
    
        if l[-1] <= e:
            a = l
        else: 
            l.pop()
            break
        r += p

    print(a)

def v_down(k, h, j):
    r = i
    while True:
        l.append(r)
    
    
        if l[-1] >= e:
            a = l
        else: 
            l.pop()
            break
        r -= p

    print(a)

v_up(i, p, e)
#v_down(i, p, e)

