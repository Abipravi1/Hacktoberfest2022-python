# Tower Of Hanoi using recursion
def toh(n,ts, td, tm):
  if(n==1):
    print(str(n)+"["+ts+"->"+td+"]")
  else:
    toh(n-1,ts,tm,td)
    print(str(n)+"["+ts+"->"+td+"]")
    toh(n-1,tm,td,ts)
n=int(input("Enter no. of discs-"))
ts=(input("Enter id of source tower-"))
td=(input("Enter id of destination tower-"))
tm=(input("Enter id of mediator tower-"))
toh(n,ts,td,tm)
