import sys
def hello_world_en():
    print("Hello, World!")
def hello_world_zh():
    print("哈囉！世界！")
def additionMethod(num1, num2):
    return num1 + num2
if __name__ == '__main__':
    
    #check the arguments are enough
    if len(sys.argv) < 4:
        print("Not enough arguments.")
        sys.exit(1)
        
    num1 = sys.argv[1]
    operator = sys.argv[2]
    num2 = sys.argv[3]
    

    if operator == '+':
        print(f"The sum of {num1} and {num2} is {additionMethod(int(num1), int(num2))}")
    else:
        print("Unsupported operator.")
    