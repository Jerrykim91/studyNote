
# 출처 : README.md 참조

"""
클래스 메소드의 사용법
# 함수가 클래스 안에 메소드로 정의
"""

class Person(object):

    """
    Advanced_OOP_4 코드보다 조금 더 세련된 코드
    """

    def __init__(self, year, month, day, sex):

        self.year  = year
        self.month = month
        self.day   = day
        self.sex   = sex

    def __str__(self):

        return '{}년 {}월 {}일생 {}'.format(self.year, self.month, self.day, self.sex)


    @classmethod
    def ssnConstructor(cls, ssn):

        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]

        else :
            year = '20' + front[:2]

        if (int(sex)%2) == 0 :
            sex = '여성'

        else :
            sex = '남성'

        month = front[2:4]
        day   = front[4:6] 

        return cls(year, month, day, sex)


ssn_1 = '900829-1000006'
ssn_2 = '951224-2000069'
ssn_3 = '201214-4000069'


Jun  = Person.ssnConstructor(ssn_1)
Jain = Person.ssnConstructor(ssn_2)
Rose = Person.ssnConstructor(ssn_3)


print(Jun)
print(Jain)
print(Rose)