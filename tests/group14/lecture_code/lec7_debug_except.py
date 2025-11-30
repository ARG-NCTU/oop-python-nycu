import math
########################################
### EXAMPLE: Buggy code to reverse a list
### Try to debug it! (fixes needed are explained below)
########################################
##def rev_list_buggy(L):
##    """
##    input: L, a list
##    Modifies L such that its elements are in reverse order
##    returns: nothing
##    """
##    for i in range(len(L)):
##        j = len(L) - i
##        L[i] = temp
##        L[i] = L[j]
##        L[j] = L[i]
#
## FIXES: --------------------------
## temp unknown
## list index out of range -> sub 1 to j
## get same list back -> iterate only over half
## --------------------------
def rev_list(L): #use new version
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        
L = [1,2,3,4]
rev_list(L)
print(L)
#
#
########################################
### EXAMPLE: Buggy code to get a list of primes
### Try to debug it! (fixes needed are explained below)
########################################
##def primes_list_buggy(n):
##    """
##    input: n an integer > 1
##    returns: list of all the primes up to and including n
##    """
##    # initialize primes list
##    if i == 2:
##        primes.append(2)
##    # go through each elem of primes list
##    for i in range(len(primes)):
##        # go through each of 2...n
##        for j in range(len(n)):
##            # check if not divisible by elem of list
##            if i%j != 0:
##                primes.append(i)
#
#
## FIXES: --------------------------
## = invalid syntax, variable i unknown, variable primes unknown
## can't apply 'len' to an int
## division by zero -> iterate through elems not indices
##                  -> iterate from 2 not 0
## forgot to return 
## primes is empty list for n > 2
## n = 3 goes through loop once -> range to n+1 not n
## infinite loop -> append j not i
##               -> list is getting modified as iterating over it!
##               -> switch loops around
## n = 4 adds 4 -> need way to stop going once found a divisible num
##              -> use a flag
## --------------------------
def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """

    if n < 2:
        return []

    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        import math

        # ==================================================
        # lec7_debug_except.py
        # 已加入中文註解，說明各範例用途與重要行為（不改動既有邏輯）
        # 主要示範內容：
        # - 反轉列表的正確作法
        # - 產生質數列表（簡單版）
        # - 例外處理（try/except）與自訂例外
        # - 在清單與平均數計算中的例外處理示範
        # ==================================================

        ########################################
        ### 範例：將列表就地反轉（reverse）
        ### 原本檔案中有一個錯誤版本註解，這裡使用修正後的 `rev_list`
        ########################################
        def rev_list(L):
            """
            將列表 L 就地反轉（in-place）。
            - 輸入：L，一個可變的序列（list）
            - 輸出：無（修改傳入的列表）

            實作重點：只需迭代到一半（len(L)//2），並在對稱位置互換元素。
            """
            for i in range(len(L)//2):
                # 計算對稱索引 j
                j = len(L) - i - 1
                # 交換 L[i] 與 L[j]
                temp = L[i]
                L[i] = L[j]
                L[j] = temp

        # 小測試：就地反轉
        L = [1, 2, 3, 4]
        rev_list(L)
        print(L)  # 預期輸出: [4, 3, 2, 1]


        ########################################
        ### 範例：取得質數列表（簡單 Sieve-like 概念，但此處為簡單判別法）
        ### `primes_list(n)` 回傳 <= n 的所有質數
        ########################################
        def primes_list(n):
            """
            輸入: n 整數 (> = 2)
            輸出: 回傳一個包含從 2 到 n 的質數的列表

            注意：此版本使用簡單的試除法，對於小 n 足夠。如果要大量計算可以改用篩法 (Sieve)。
            """

            if n < 2:
                return []

            # 初始化已知的質數列表
            primes = [2]
            # 從 3 開始，逐一檢查到 n（含）
            for j in range(3, n + 1):
                is_div = False
                # 若 j 能被已知的某個質數整除，則不是質數
                for p in primes:
                    if j % p == 0:
                        is_div = True
                        # 一旦發現可整除就可停止檢查（小優化）
                        break
                if not is_div:
                    primes.append(j)
            return primes

        print(primes_list(2))   # [2]
        print(primes_list(15))  # [2, 3, 5, 7, 11, 13]


        ######################################
        # 範例：輸入和例外處理（try/except 基本用法）
        ######################################
        # 下方範例示範如何處理使用者輸入的錯誤：無論輸入非數字或除以零，都能捕捉並給出友善訊息。

        try:
            a = int(input("Tell me one number: "))
            b = int(input("Tell me another number: "))
            print("a/b = ", a / b)
        except:
            # 未指定例外類別，會捕捉任何例外
            # 在實務上通常應該更明確地列出要捕捉的例外類型
            print("Bug in user input.")


        try:
            a = int(input("Tell me one number: "))
            b = int(input("Tell me another number: "))
            print("a/b = ", a / b)
            print("a+b = ", a + b)
        except ValueError:
            # 無法將輸入轉為數字
            print("Could not convert to a number.")
        except ZeroDivisionError:
            # 除以零
            print("Can't divide by zero")
        except:
            # 捕捉其他未預期錯誤
            print("Something went very wrong.")



        ######################################
        # 範例：自行拋出例外（防禦式檢查）
        ######################################
        def get_ratios(L1, L2):
            """
            假設 L1 和 L2 是等長的數字列表，回傳一個新列表，其元素為 L1[i]/L2[i]

            行為說明：
            - 若傳入兩個長度不同的列表，立即拋出 ValueError，讓呼叫端知道使用方式錯誤。
            - 若分母為 0，將對應位置放入 float('nan')，並繼續處理其他索引。
            - 若引發 TypeError（例如把字串當作數字來除），則將其轉為 ValueError，並中止函式。
            """

            # 防禦性檢查：兩個列表長度必須相等
            if len(L1) != len(L2):
                raise ValueError('get_ratios called with lists of different lengths')

            ratios = []
            for index in range(len(L1)):
                try:
                    # 主要操作：計算商並加入 results
                    ratios.append(L1[index] / L2[index])

                except ZeroDivisionError:
                    # 對於除以零，將結果記為 NaN（Not a Number），並繼續
                    ratios.append(float('nan'))

                except TypeError:
                    # 型別錯誤代表參數型別不對，轉為 ValueError 並中止
                    raise ValueError('get_ratios called with bad argument type')

                else:
                    # 如果沒有例外發生，可在此做些紀錄或訊息
                    print(f"Index {index}: success")

                finally:
                    # 無論是否發生例外，此區塊都會執行
                    print(f"Index {index}: finished processing.")

            return ratios

        print(get_ratios([1, 4], [2, 4]))


        #######################################
        ## 範例：在 list 結構中處理例外與平均值計算
        #######################################
        def get_stats(class_list):
            """
            輸入：class_list 為一個學生資訊列表，每個元素類似：[[first, last], [grade1, grade2, ...]]
            輸出：回傳 new_stats 列表，每個項目包含姓名、原始成績列表、以及該學生的平均分數。
            """
            new_stats = []
            for person in class_list:
                # person[0] = name-list，如 ['peter', 'parker']
                # person[1] = grades-list，如 [80.0, 70.0]
                new_stats.append([person[0], person[1], avg(person[1])])
            return new_stats

        # avg() 版本：處理空的 grade list 時會捕捉 ZeroDivisionError
        def avg(grades):
            try:
                return sum(grades) / len(grades)
            except ZeroDivisionError:
                # 當 grades 為空時，回傳 0.0 並印出警告
                print('warning: no grades data')
                return 0.0


        test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
                       [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
                       [['captain', 'america'], [80.0, 70.0, 96.0]],
                       [['deadpool'], []]]

        print(get_stats(test_grades))
