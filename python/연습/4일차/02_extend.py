a = ['apple']
a.extend(['banana', 'mongo']) # 반드시 리스트로 묶어 줘야 한다. 
print(a)
a.extend('banana')
print(a)

"""
['apple', 'banana', 'mongo']
['apple', 'banana', 'mongo', 'b', 'a', 'n', 'a', 'n', 'a']
"""
