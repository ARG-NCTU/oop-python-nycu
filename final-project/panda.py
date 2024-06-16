import pandas as pd
import matplotlib.pyplot as plt
import json

# 讀取 JSON 檔案到 Python 字典
with open('./oop-python-nycu/final-project/player_data.json', 'r') as f:
    data = json.load(f)

# 將字典轉換成 Pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# 計算統計量
means = df.mean()
std_devs = df.std()
std_errs = df.sem()

# 視覺化呈現

# 製作平均值的柱狀圖
means.plot(kind='bar', yerr=std_errs, capsize=5)
plt.title('Average Statistics')
plt.ylabel('Mean Value')
plt.xticks(rotation=0)
plt.show()

# 製作標準差的柱狀圖
std_devs.plot(kind='bar')
plt.title('Standard Deviation')
plt.ylabel('Standard Deviation Value')
plt.xticks(rotation=0)
plt.show()