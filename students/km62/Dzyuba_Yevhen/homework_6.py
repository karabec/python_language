#1
a = input(Raw).split()
for i in range(0, len(a), 2):
    print(a[i])
#2
list=[]
list=input().split()
for element in list:

    element=int(element)

    if element%2==0:

        print(element)
#3
x=0

print("Program shows numbers, greater then previous")

n=input("Enter a row of numbers")


list_int = n.split()

prev=int(list_int[0])


for element in list_int[1:]:

    element=int(element)

    x=element

    if x>prev:

        print(x,end=" ")

    prev=element
#4
n=input()

list=n.split()

prev=int(list[0])


for element in list[1:]:

    x=int(element)

    if (x>0 and prev>0) or (x<0 and prev<0):

        print(prev,element)

        break

    else:

        print(end="")

    prev=x

#5

counter = 0


n = input ()
list= n.split ( )

for i in range ( 1 , len ( list_int ) - 1 ) :

    if list[ i ] > list[ i - 1 ] and list[ i ] > list[ i + 1 ] :

        counter += 1
print(counter)
#6
index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)
#7
counter = 0

row = input ()

list = row.split ()

height = int(input())
for element in list:

    if int(element)<height:

        list.insert(counter,height)

        break

    counter+=1


print(counter+1)
#8
temp = 0

counter = 0
row = input ()

list = row.split ()


for element in list:

    if element != temp:

        temp = element

        counter +=1


print(counter)

#9
#input

row = input ()

print()


list = row.split ()



for i in range (1,len(list),2):

    Temp = list [i-1]

    list [i-1] = list[i]

    list[i] = Temp
print(" ".join(list))

#10
n=input()
list_numbers=n.split()
max_num = int ( list_numbers [ 0 ] )
min_num = int ( list_numbers [ 0 ] )
max_pos , min_pos = 0, 0
counter = 0
for i in range(len(list_numbers)):
    if int(list_numbers[i])>max_num:
        max_num = int( list_numbers[i] )
        max_pos = i
    if int(list_numbers[i])<min_num:
        min_num = int( list_numbers[i] )
        min_pos = i
temp = list_numbers[max_pos]
list_numbers[max_pos] = list_numbers[min_pos]
list_numbers[min_pos] = temp
print(" ".join(list_numbers))
#11

row = input ()

 a = int( input () )

list = row.split()

for i in range (a+1,len(list)):

    list[i-1]=list[i]

list.pop()
print(" ".join(list))
#12
a = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
#13
counter = 0
row = input()

list_a = row.split()


for i in list_a:

    for j in list_a:

        if i == j:

           counter+=1

    counter-=1
print (counter // 2)
#14
temp = 0

row = input ()
list = row.split ()

list_new = []


for element in list:

    if element != temp:

        temp = element

        if list.count(temp) ==1:

            list_new.append(temp)


print(" ".join(list_new))
#15
n, k = [int(s) for s in input().split()]

bahn = ['I'] * n

for i in range(k):
 
   left, right = [int(s) for s in input().split()]
   
 for j in range(left - 1, right):
 
       bahn[j] = '.'
print(''.join(bahn))
