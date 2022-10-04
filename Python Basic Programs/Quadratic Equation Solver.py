def roots_quad_eqn(a,b,c):
    d = (b**2)-(4*a*c)
    if d == 0:
        x1 = (-b)/(2*a)
        x2 = x1
        print("THE EQUATION HAS REAL & EQUAL ROOTS... ",x1,"and",x2)
        return(x1,x2,0,0,True)
    elif d>0:
        x1 = (-b+d)/(2*a)
        x2 = (-b-d)/(2*a)
        print("THE EQUATION HAS REAL & DISTINCT ROOTS... ",x1,"and",x2)
        return(x1,x2,0,0,True)
    else:
        img = (-d)**(1/2)
        real = (-b)/(2*a)
        print("THE EQUATION HAS IMAGINARY & CONJUGATE ROOTS... ",real,"+",img,"i and",real,"-",img,"i")
        return(real,real,img,img,False)   
a = float(input("ENTER THE COEFFICIENT OF x^2: "))
b = float(input("ENTER THE COEFFICIENT OF x^1: "))
c = float(input("ENTER THE COEFFICIENT OF x^0: "))
roots_quad_eqn(a,b,c)
