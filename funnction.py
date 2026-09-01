# def kunal():

    # print("i am vikas")
# kunal()    


# def check_weather():    #this is how we call the function 
    # temperature=35      #if i haven't declare tem as a function then later it will not work
    # if temperature>25:
        # print("it is hot")
    # else:
        # print("it is nice weather")
# check_weather()


# how parameter work or change the scenario with function                  
# def greet (name):
#     print(f"my name is {name}")
# greet(kunal)    #this will not run or it is wrong bcz kunal is not defined
## now kunal is defined and don't forget to put into double quote


# def simple_intreset(principle,rate,time):
#     print(f"{principle*rate*time/100}")
# simple_intreset(principle=100,rate=21,time=4)

# def calculation(a,b):
#     print(f"{a+b}")
# calculation(a=5,b=6)    

# def calculation_return(a,b): # doesn't run properly .see this later
#     return a+b
# calculation_return(a=5,b=7)  


# def calculate():
#     a=37
#     if a%2==0:  # the sign% showing that number divided by 2 has remainder 0 then print even otherwise print odd.
        
#         print("even number")
#     else:
#         print("odd number")
# calculate()        

#in a class there is 50 students and i want to know that by entering score i know that he is pass or fail.if the passing mark is 20.
score=int(input("enter score:"))
if score >= 20:
    print("he is passed")
else:
    print("he is failed")
    
    
