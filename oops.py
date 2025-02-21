# class Sample:
#     x=10

# p=Sample()
# print(p.x)



# class Bird:
#     def __init__(self):
#         print("bird is ready")
        
#     def who(self):
#         print("bird")
        
#     def swim(self):
#         print("swimming faster")

# class Penguin(Bird):
#     def __init__(self):
#         print("my name is penguin")
        
#     def who(self):
#         print("second bird")
# x=Penguin()
# x.who()
        
  
  
# class Bird:
#     def __init__(self):
#         print("bird is ready")
        
#     def who(self):
#         print("bird")
        
#     def swim(self):
#         print("swimming faster")      
        
        
# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print("bird name is penguin")
    
#     def who(self):
#         super().who()
#         print("second bird ")

#     def run(self):
#         print("bird can run")

# x=Penguin()
# x.run()
    

# class Sample:
#     def flower(self):
#         print("lilly")
    
# class Sample2():
#     def flower(self):
#         print("rose")
        
# class Sample4():
#     def flower(self):
#         print("jamanthi")
    
# class Sample3(Sample , Sample2 , Sample4):
#     def flower(self):
#         super().flower()
#         print("lotus")
        
# x=Sample3()

# x.flower()


# class Sample:
#     def flower(self):
#         print("rose")
    
# class Sample2(Sample):
#     def flower(self):
#         super().flower()
#         print("lotus")
        
# class Sample3(Sample2):
#     def flower(self):
#         super().flower()
#         print("lilly")
        
# x=Sample3()
# x.flower()
        
    
    
# class Sample:
#     def __init__(self):
#         print("im great grand father")
#     def flower(self):
#         print("lotus")
    
# class Sample2(Sample):
#     def __init__(self):
#         super().__init__()
#         print("im grand father")
#     def flower(self):
#         super().flower()
#         print("sun flower")
        
# class Sample3(Sample2):
#     def __init__(self):
#         super().__init__()
#         print("im father")
#     def flower(self):
#         super().flower()
#         print("lilly")
        
# class Sample4(Sample3):
#     def __init__(self):
#         super().__init__()
#         print("im child")
#     def flower(self):
#         super().flower()
#         print("rose")
            
    
# x=Sample4()
# x.flower()




# class Football:
#     def __init__(self):
#         self.__maxgoal = 500
    
#     def scored(self):
#         print("Ronaldo scored {} goals".format(self.__maxgoal))
    
#     def set_max_goals(self,goals):
#         self.__maxgoal=goals

# x=Football()
# x.__maxgoal=800
# x.scored()
# x.set_max_goals(1000)
# x.scored()


# class Parrot:
#     def fly(self):
#         print("parrot can fly")
        
#     def swim(self):
#         print("parrot can't swim")

# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")
        
#     def swim(self):
#         print("penguin can swim")
        
# class Seagul:
#     def fly(self):
#         print("seagul can fly")
        
#     def swim(self):
#         print("seagul can swim")
        
# def test(bird):
#     bird.fly()
#     bird.swim()

    
# a=Parrot()
# b=Penguin()
# c=Seagul()


# test(a)
# test(b)
# test(c)


# class Sample:
#     def __init__(self,a):
#         self.a=a
        
#     def __add__(self,other):
#         return self.a + " " +other.a
    
# x=Sample("swalih")
# y=Sample("nabeel")
# print(x+y)
        
 
# class Sample:
#     def __init__(self,a):
#         self.a=a
        
#     def __add__(self,b):
#         return self.a + b.a

# x=Sample(10)
# y=Sample(30)

# print(x+y)               
       
       
# class Sample:
#     def __init__(self,a):
#          self.a = a
    
#     def __sub__(self,b):
#         return self.a - b.a

# x=Sample(20)
# y=Sample(10)
# print(x-y)


# class Sample:
#     def __init__(self,a):
#          self.a = a
    
#     def __truediv__(self,b):
#         return self.a / b.a

# x=Sample(20)
# y=Sample(10)
# print(x/y)  


# class Sample:
#     def __init__(self,a):
#          self.a = a
    
#     def __mul__(self,b):
#         return self.a * b.a

# x=Sample(20)
# y=Sample(10)
# print(x*y) 

# class Sample:
#     def __init__(self,a):
#          self.a = a
    
#     def __mod__(self,b):
#         return self.a % b.a

# x=Sample(20)
# y=Sample(3)
# print(x%y)



# class Sample:
#     def __init__(self,a):
#          self.c= a
    
#     def __floordiv__(self,b):
#         return self.c // b.c

# x=Sample(20)
# y=Sample(3)
# print(x//y) 




# class Book:
    
#     def __init__(self,title,auther,pages):
#         self.title=title
#         self.auther=auther
#         self.pages=pages
        
#     def __str__(self):
#         return f"{self.title} by {self.auther} ,{self.pages} pages"
    
# x=Book("aadujeevitham" , "Binyamin" , 900)
# print(str(x))
        
        
        
class Football:
    def __init__(self,name,goals,time,club):
        self.name=name
        self.goals=goals
        self.time=time
        self.club=club
    
    def __str__(self):
        return f"{self.name} scored {self.goals} goals in {self.time} minutse for {self.club}"
    
x=Football("lawendoski",5,9,"bayern ")
print(str(x))

    