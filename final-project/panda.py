import pandas as pd
import json
import matplotlib.pyplot as plt

# 讀取JSON文件的每一行，將其轉換為字典列表
data = []
with open('./oop-python-nycu/final-project/player_data.json', 'r') as f:
    for line in f:
        data.append(json.loads(line))

# 將數據轉換為DataFrame
df = pd.DataFrame(data)

# 顯示數據框架的前幾行
print(df.head())

# 繪製圖表
# 例如：繪製每個玩家的跳躍次數對比
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['player1_jump_count'], label='Player 1 Jump Count')
plt.plot(df.index, df['player2_jump_count'], label='Player 2 Jump Count')
plt.xlabel('Game Index')
plt.ylabel('Jump Count')
plt.title('Player Jump Counts Over Games')
plt.legend()
plt.show()

# 繪製每個玩家的射擊次數對比
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['player1_shoot_count'], label='Player 1 Shoot Count')
plt.plot(df.index, df['player2_shoot_count'], label='Player 2 Shoot Count')
plt.xlabel('Game Index')
plt.ylabel('Shoot Count')
plt.title('Player Shoot Counts Over Games')
plt.legend()
plt.show()

# 你可以根據需要繪製更多的圖表，比如炸彈使用次數、死亡次數等
