"""
簡易計算機程式

這是一個命令列計算機工具，支援基本的四則運算（加、減、乘、除）。
使用方式：python main.py <數字1> <運算子> <數字2>
範例：python main.py 10 + 5
"""

import sys  # 匯入 sys 模組，用於存取命令列參數


def additionMethod(num1, num2):
    """
    加法函式

    參數：
        num1: 第一個數字（被加數）
        num2: 第二個數字（加數）

    回傳：
        兩數相加的結果
    """
    return num1 + num2


def subtractionMethod(num1, num2):
    """
    減法函式

    參數：
        num1: 第一個數字（被減數）
        num2: 第二個數字（減數）

    回傳：
        兩數相減的結果
    """
    return num1 - num2


def divisionMethod(num1, num2):
    """
    除法函式

    參數：
        num1: 第一個數字（被除數）
        num2: 第二個數字（除數）

    回傳：
        兩數相除的結果
    """
    return num1 / num2


def multiplicationMethod(num1, num2):
    """
    乘法函式

    參數：
        num1: 第一個數字（被乘數）
        num2: 第二個數字（乘數）

    回傳：
        兩數相乘的結果
    """
    return num1 * num2


# 程式進入點：當此檔案被直接執行時（而非被匯入時）
if __name__ == '__main__':

    # 檢查命令列參數是否足夠（程式名稱 + 3 個參數 = 至少 4 個）
    if len(sys.argv) < 4:
        print("Not enough arguments.")  # 參數不足，顯示錯誤訊息
        sys.exit(1)  # 以錯誤狀態碼 1 結束程式

    # 從命令列參數取得運算所需的數值和運算子
    num1 = sys.argv[1]      # 第一個參數：第一個數字
    operator = sys.argv[2]  # 第二個參數：運算子（+、-、*、/）
    num2 = sys.argv[3]      # 第三個參數：第二個數字

    # 根據運算子執行對應的運算
    if operator == '+':
        # 加法運算：將兩個字串轉換為整數後相加
        print(f"The sum of {num1} and {num2} is {additionMethod(int(num1), int(num2))}")
    elif operator == '-':
        # 減法運算：將兩個字串轉換為整數後相減
        print(f"The difference of {num1} and {num2} is {subtractionMethod(int(num1), int(num2))}")
    elif operator == '/':
        # 除法運算：將兩個字串轉換為整數後相除
        print(f"The division of {num1} by {num2} is {divisionMethod(int(num1), int(num2))}")
    elif operator == '*':
        # 乘法運算：將兩個字串轉換為整數後相乘
        print(f"The product of {num1} and {num2} is {multiplicationMethod(int(num1), int(num2))}")
    else:
        # 不支援的運算子，顯示錯誤訊息
        print("Unsupported operator.[" + operator + "]")
