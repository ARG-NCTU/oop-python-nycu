import pandas as pd
import json
import matplotlib.pyplot as plt

# 读取JSON文件并将其转换为字典列表
with open('./oop-python-nycu/final-project/player_data.json', 'r') as f:
    data = json.load(f)

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 显示数据框架的前几行
print(df.head())

# 绘制图表
# 例如：绘制每个玩家的跳跃次数对比
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['player1_jump_count'], label='Player 1 Jump Count')
plt.plot(df.index, df['player2_jump_count'], label='Player 2 Jump Count')
plt.xlabel('Game Index')
plt.ylabel('Jump Count')
plt.title('Player Jump Counts Over Games')
plt.legend()
plt.show()

# 绘制每个玩家的射击次数对比
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['player1_shoot_count'], label='Player 1 Shoot Count')
plt.plot(df.index, df['player2_shoot_count'], label='Player 2 Shoot Count')
plt.xlabel('Game Index')
plt.ylabel('Shoot Count')
plt.title('Player Shoot Counts Over Games')
plt.legend()
plt.show()

# 你可以根据需要绘制更多的图表，比如炸弹使用次数、死亡次数等

