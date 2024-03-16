def subtract(x, y):
    return x - y

def test_subtract():
    assert subtract(2, 2) == 0
    print("There are no issues with the " + subtract.__name__ + " function")

def main(): 
    test_subtract()

if __name__=="__main__": 
    main() 