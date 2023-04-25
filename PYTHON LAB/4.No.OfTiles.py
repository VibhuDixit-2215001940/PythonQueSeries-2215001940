a,b=input('Enter the dimension of floor: ').split(' ')
c = int(a)
d = int(b)
area_floor = c*d
x,y=input('Enter the dimension of tile: ').split(' ')
p = int(x)
q = int(y)
area_tile = p*q
no = area_floor / area_tile
print("The total no. of tile required are: ",no)

