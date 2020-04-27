def centuryFromYear(year):
    '''1 ~ 100 => 1
    101 ~ 200 => 2'''
    import math
    print(year)
    return math.ceil(year/100)

#Best Solution
def centuryFromYear(year):
    return (year + 99) // 100
    
#어떻게 저런 생각을 하지?ㅠㅠ
