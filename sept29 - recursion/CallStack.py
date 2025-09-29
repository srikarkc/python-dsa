def funcThree():
    print('3')

def funcTwo():
    funcThree()
    print('2')

def funcOne():
    funcTwo
    print('1')

funcOne