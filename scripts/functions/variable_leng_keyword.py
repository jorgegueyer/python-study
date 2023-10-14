def display(p,**karg): # Dictionary
    print(p)
    print(karg)
    return None

display(4,b=5,a=4)
display(5,a=4,b=5,c=6)
display('goodbye',a='hi',b=False,c=10)