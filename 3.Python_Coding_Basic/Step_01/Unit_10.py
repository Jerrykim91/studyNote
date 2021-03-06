# Unit_10.py
# 리스트와 튜플 사용하기

txt ="""
# 리스트와 튜플 사용하기 

- 리스트 
    - 리스트 = [값1, 값2 ,값3,.... ]      
    
        -  리스트에 여러 자료형 저장할수 있다.
        - 빈 리스트 => 리스트 = [] , 리스트 = list() 생성 가능 
            - 빈리스트는 쓸모는 없어 보이지만 보통 빈리스트를 만들어 값을 추가하는 방식으로 사용 
        - range 를 사용하여 리스트 만들기 
            - range는 연속된 숫자를 생성 
                => 리스트 = list(range(횟수))       
                => 리스트 = list(range(시작 , 끝))  -> 시작과 끝인데(시작 , 끝-1)     
                => 리스트 = list(range(시작 , 끝, 증가폭)) -> 해당 값을 증가하면서 숫자를 생성     
            
            
- 튜플 
    - 튜플 = (값1, 값2 ,값3,....)
    
    - 튜플 = 값1, 값2 ,값3,....     
        => 괄호로 묶지 않아도 값만 콤마로 구분해도 튜플     
        - 리스트처럼 값을 일렬로 저장 => 안에 저장된 요소를 변경, 추가, 삭제를 할 수 없다.      
            => 쉽게 말해 **읽기 전용 리스트** 
        - 리스트처럼 여러 자료형 저장할수 있다.
        - **보통 튜플은 요소가 변경되지 않고 유디 되어야 할 때 사용됨**
        - 잦은 요소 변경은 리스트로 사용!!
        - 요소가 하나만 든 튜플은     
            => 튜플 = (값,), 튜플 = 값,    
"""
print(txt)
print('-'*40)

# 리스트 패킹 
a = list(range(1,10))
print(a)

# 시작과 끝인데(시작 , 끝-1 )
b = list(range(5,12)) 
print(b)
print('-'*40)

# 증가 폭을 사용하는 방법 
#=> range()증가 폭을 지정하면 해당 값을 증가하면서 숫자를 생성 
c = list(range(-4,10,2))
print(c)

# 10부터 1씩 감소하며 0은 포함 되지 않는다 그래서 1까지 생성된다. 
d = list(range(10, 0, -1))
print(d)
print('-'*40)

# 튜플 패킹
a = 1,2,3,4,5 
print(a)
b = (1, 2, 3, 4, 5)
print(b)


# 요소가 하나만 든 튜플은 => 튜플 = (값,), 튜플 = 값,  
# 값이 한개인 튜플이 필요한 이유 
# => 함수를 사용하다 보면 값이 아닌 튜플을 넣어야 하는 경우가 발생 
# => 이때 값은 한개지만 튜플을 넣을때 (값,)과 같은 형식으로 사용  

# range를 이용해 튜플 생성하기
a = tuple(range(10))
print(a)


b = tuple(range(10))       
c = tuple(range(1 , 10))     #-> 시작과 끝인데(시작 , 끝-1)     
d = tuple(range(10 , 0, -1)) #-> 해당 값을 증가하면서 숫자를 생성 
print(b,c,d)
print('-'*40)

# 튜플을 리스트로 만들고 리스트를 튜플로 만들기 -1
a = [1,2,3,4]
tuple(a)

# 튜플을 리스트로 만들고 리스트를 튜플로 만들기 -2
b = (5,6,7,8)
list(b)

# 리스트와 튜플안에 문자열을 넣으면 => 문자 리스트, 문자 튜플이 생성 
list('hello'),tuple('hello')
# 문자열 'hello'가 문자 하나하나가 리스트의 요소로 들어가서 문해된 형태로 출력이 된다.

# 리스트와 튜플로 변수만들기 
a,b,c = [1,2,3]
print(a,b,c)
d,e,f = (5,6,7)
print(d,e,f)

# 리스트와 튜플 변수로 변수여러개를 만들 수 있음 
# 다음과 같이 리스트와 변수 여러개에 할당하는 것을 리스트 언패킹(list unpacking), 튜플언페킹이라고 함(tuple unpacking)

x = [1,2,3]
a,b,c = x
print(a,b,c)

print('='*5)

y = (5,6,7)
d,e,f = y
print(d,e,f)

print('-'*40)

