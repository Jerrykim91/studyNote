
# 출처 : README.md 참조

class SuperClass(object):
    super_var = '수퍼 네임스페이스에 있는 변수'

class MyClass(SuperClass):
    class_var = '클래스 네임스페이스에 있는 변수'
    
    def __init__(self):
        self.instance_var = '인스턴스 네임스페이스에 있는 변수'
    

my_instance = MyClass()

# 엑세스 가능한 경우
print(my_instance.instance_var)
print(my_instance.class_var)
print(my_instance.super_var)
print(MyClass.class_var)
print(MyClass.super_var)
print(SuperClass.super_var)
print('-'*30)


# 엑세스 불가능한 경우
try:
    print(SuperClass.class_var)
except:
    print('class_var를 찾을 수가 없습니다.')
    
try:
    print(MyClass.instance_var)
except:
    print('instance_var를 찾을 수가 없습니다.')