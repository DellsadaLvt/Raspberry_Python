friends= [ "Mike", "John", "Keny" ]
number= 9


def add_cal( a, b):
    try:
        int(a);
        int(b);
    except:
        print("invalid input")
        return -1
    return (a + b)
    
