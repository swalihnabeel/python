
### largest number q ###



# from functools import reduce
# lis=[32,43,56,1,73,3]

# def add(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# v=reduce(add,lis)
# print(v)
 
    ###voting question###
 
    
# lis=[{"name":"swalih","age":21},{"name":"bharath","age":22},{"name":"shadil","age":18},{"name":"yahya","age":30},{"name":"arshad","age":17},{"name":"ruhaim","age":22},{"name":"vishnu","age":16},{"name":"anas","age":12},{"name":"shameem","age":24},{"name":"shahul","age":28}]

# def x(a):

#     if a["age"]>=18:
#         return a
    
# result=filter(x,lis)
# print("eligible voters are:")
# for k in result:
#     print(k["name"])



###palindrome question###

# user=list(input("enter word :"))
# b=[]
# c=""
# for i in user:
#     b.insert(0,i)
# for i in user:
#     if i==" ":
#         user.append(c)
#     else:
#         c+=i    
# if user==b:
#     print(c +" is palindrome")
# else:
#     print(c+ " is not palindrome")


### longest word ###


# from functools import reduce
# user=input("enter a word :")
# b=[]
# c=""
# l1=[]
# for i in user:
#     if i==" ":
#         b.append(c)
#         c+=i
#         c=""
#     else:    
#         c+=i 
# b.append(c)
# for i in b:
    
#     l1.append(len(i))
    
# def add(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# v=reduce(add,l1)   
# l=l1.index(v)
# print(b[l])




    ### celsius to fahrenheit ###



# user= float(input("enter a celsius temperature : "))

# def eq():
    

#     x=((user-32)*5)/9
#     print(x , "C")
    
# eq()



    ### factorial ###


# from functools import reduce
# user = int(input("enter a number : "))
# l1=[]
# for i in range(1,user+1):
#     l1.append(i)

# def fact(a,b):
#     result= a*b
#     return result
# x=reduce(fact,l1)
# print("factorial is", x)


     ### vowels ###
     

# user = input("enter a word : ")
# l1=[]

# for i in user:
#     if i=="a" or i=="A" or i=="e" or i=="E" or i== "i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
#         l1.append(i)
        
# print("vowel count in word is",len(l1))

  ##another way##

# x = input("Enter a word:")
# y = 0

# for i in x:
#     if i=="a" or i=="A" or i=="e" or i=="E" or i== "i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
#         y = y+1
        
# print ("The count of Vowels in Word",x,"is :",y)
        
        
    
    ### reverce word in sentence ###
    
# user = input("enter a sentence: ")

# a=[]

# c=""

# for i in user:
#     if i==" ":
#         a.insert(0,c)    
#         c=""
        
#     else:
#         c+=i
# a.insert(0,c)

# for j in a:
#     print(j,end=" ")


        ### remove duplicate elements ###
        
        
# user = input("enter element: ")
# l1=[]
# c=""
# for i in user:
#     if i==" ":
#         l1.append(c)
#         c=""
#     else:
#         c+=i
# l1.append(c)

# l2=[]
# l3=[]

# for i in l1:
#     if i in l2:
#         l3.append(i)
#     else:
#         l2.append(i)
        
# for i in l2:
#     print(i, end=" ")


    ### capitalise First word of a sentence ###
    
# user = input("enter a sentence: ")
# b=[]
# c=""
# for i in user:
#     if i==" ":
#         b.append(c)
#         c=""
#     else:
#         c+=i
# b.append(c)

# for i in b:
#     a=str(i)
#     print(a.capitalize(),end=" ")

    
    
     ### ascending order ###


# from functools import reduce     
# l1=[20,18,34,56,33,3]
# l2=[]
# a=len(l1)
# i=1
# while i<=a:
#     def cmp(a,b):
#         if a<b:
#             return a
#         else:
#             return b
#     re=reduce(cmp,l1)
#     i+=1
#     l2.append(re)
#     l1.remove(re)
    
# print(l2)
    
    
   ### multiples of 3 or 5 ###
   
# from functools import reduce
# user = int(input("enter a number: "))
# a=[]
# for i in range(1,user):
#     if i%3==0 or i%5==0:
#         a.append(i)
        
# def sum(a,b):
#     x=a+b
#     return x
# re=reduce(sum,a)
# print(re)


   ### prime number ###
   
