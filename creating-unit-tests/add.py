def add(x, y):
    return x + y

def test_add():
    assert add(1, 1) == 2
    print("There are no issues with the " + add.__name__ + " function")
    
def main(): 
    test_add()

if __name__=="__main__": 
    main() 