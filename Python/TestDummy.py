# def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
 
# c = calc()
# c(1)
# c(2)
# c(3)

############################################################

def closr():                
    i = 10
    j = 10
    tal = 0

    def mul(x):   
        nonlocal tal
        tal = tal + i * x + j       
        print(tal)  
    return mul

y = closr() 
# print(y(1))
# print(y(1),y(2),y(3))
y(1)
y(2)
y(3)

# Output
# >>> 20
# >>> 50
# >>> 90
# >>> None None None

############################################################

# # lambda 사용 

# def closr():                
#     i = 10
#     j = 10

#     return lambda x: i * x + j  # 람다 표현식을 반환 

# y = closr() 
# print(y(1),y(2),y(3),y(4),y(5))

# # Output
# # >>> [20, 30, 40, 50, 60]

############################################################

# nonlocal를 사용하는 이유 
# def outer():
#     a = 10
#     def inner():
#         a += 10
#         print('a:', a)
#     inner()
# outer()

# Output
# >>> UnboundLocalError: local variable 'a' referenced before assignment


# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         a += 10
#         print('a:', a)
#     inner()
# outer()

############################################################

# ## 클로저 형태의 함수 

# def closr(): # 1. 선언 
#     i = 10
#     j = 10

#     def mul(x):            # 4. 호출
#         return i * x + j   # 5. 함수 밖의 변수 호출해서 연산 후 리턴  

#     return mul             # 3. mul 함수자체를 반환 -> ()는 사용하면 x 

# y = closr() # 2. 호출 
# print(y(1),y(2),y(3),y(4),y(5))

# # Output
# # >>> 20 30 40 50 60 

# dum = [ y(i) for i in range(1,6)]
# print(dum) 

# # Output
# # >>> [20, 30, 40, 50, 60]

############################################################

# # global a
# a = 1
 
# def test():
#     # global a
#     a = 3
#     b = 2
 
#     return a + b
 
 
# print('>>> test\n',test())
# print('>>> a\n',a)

############################################################

# ## global변수 사용 

# x = 1 
# def Fst_Phase():
#     x = 50         # Fst_Phase의 지역변수 x
#     def Fst_Part():
#         x = 70     # Fst_Part의 지역변수 x
#         def Fst_Step():
#             global x
#             x = x + 80
#             print(x)

#         Fst_Step()

#     Fst_Part()

# Fst_Phase()


# # Output

############################################################

# 6
# def Outer():
#     x = 35        # 지역변수 x
#     def Inner():
#         nonlocal x
#         x = 25    
#     Inner()
#     print(x)      # 지역변수 출력 

# Outer() 

############################################################

# 5
# def Outer():
#     x = 35        # 지역변수 x
#     def Inner():
#         x = 25    
#     Inner()
#     print(x)      # 지역변수 출력 

# Outer()

############################################################

# 4
# def Func():
#     Code = 'Func의 test'

#     def FuncInFunc():
#         print(Code)
        
#     FuncInFunc()

# Func()

############################################################

# # 3
# def Func():
#     Code = 'Func의 test'

#     def FuncInFunc():
#         print(Code)
        
#     return FuncInFunc()

# Func()

############################################################

# 2

# x = 100  
# def val():
#     x = 10
#     print(x) # 전역변수 

# val()
# print(x)

############################################################

# 1 

# x = 100  # 전역 변수 
# def val():
#     print(x) # 전역변수 

# val()
# print(x)

############################################################