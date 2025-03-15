

my_var="God Shiva!"
# print(my_var)

my_list=[1,3,45,True,'Shiva',"Madhu",'java']

my_list[-1]="Java"
# print(my_list)
y=my_list.index(3,1,6)
# print(y)
even_list=[]
odd_list=[]

for i in range(1,20):
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)