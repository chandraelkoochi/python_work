def max_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("{} is greater".format(num1))
    elif num2>num1 and num2>num3:
        print("{} is greater".format(num2))
    else:
        print("{} is greater".format(num3))

if __name__ == '__main__':
    max_num(10,20,15)