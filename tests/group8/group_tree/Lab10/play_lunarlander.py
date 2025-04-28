import sys, time
import os

import pygame
import gymnasium as gym
from gymnasium.utils.play import play, display_arr, PlayPlot
import numpy as np
import add_path
import warnings
warnings.filterwarnings("ignore")

env = gym.make('custom_gymnasium.envs:CustomLunarLander-v1', gravity= -5.0, fuel=150, turbulence_power = 1, render_mode="rgb_array")
env.reset()
env.render()
def callback(obs_t, obs_tp1, action, rew, terminated, truncated, info):
    # 顯示燃料值
    fuel = info.get('fuel', '未知')  # 從 info 字典中提取燃料值
    print(f"燃料剩餘量: {fuel}")
    if terminated :
    	print("\x1b[6;30;42mSuccess!!\x1b[0m") if rew==100 else print("Crashed!!")   
    return [rew]
plotter = PlayPlot(callback, 150, ["reward"])
play(env,callback = plotter.callback
                        ,keys_to_action={
                          "w": 2,
                          "a": 1,
                          "d": 3,
                          }, noop=0)

