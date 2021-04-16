def swap(x,y):
  assert type(x)==list and type(y)==list
  tmp=x[:]
  x=y[:]
  y=tmp
return


x=[1]
y=[2]
swap(x,y)
print x,y
