# app.py
# This is a test commit
# This is 2nd commit by Jasper
# This is 3rd commit by Japper
# 4th commit
# This is 5th commit by Jasper
# This is 6th commit by Jasper - Enabled GitHub Actions 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
    
def test_sub():
    assert sub(3,1) ==2
    assert sub (1,1)==0
    
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
