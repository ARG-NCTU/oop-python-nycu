import numpy as np
import gymnasium as gym
from typing import TYPE_CHECKING, Optional
from custom_gymnasium.utils.base_lander import BASE_LANDER

class CustomLunarLander_v1(BASE_LANDER):
    def __init__(
        self,
        render_mode: Optional[str] = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        fuel: float = 150,):
        pass

        '''
        Task:
        - Implement a custom lunar lander environment where the lander has a fuel tank of size `fuel`.
        '''
        # =====================type your code here=====================
        super().__init__(render_mode, continuous, gravity, enable_wind, wind_power, turbulence_power)
        self.fuel = fuel  # Initialize the fuel tank
        self.initial_fuel = fuel  # Store the initial fuel for resetting
        
        # =============================================================

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,):
        pass
        '''
        Task:
        - Reset the fuel tank to its original size.
        '''
        # =====================type your code here=====================
        super().reset(seed=seed, options=options)
        self.fuel = self.initial_fuel  # Reset the fuel tank to its original size
        # =============================================================
        
    def step(self, action):
        pass
        '''
        Task:
        - The lander can only move if it has fuel left. If the fuel is exhausted, the lander can no longer move.
        
        Hint:
        - If the lander moves, the fuel tank should be decremented by 1.
        - If the lander doesn't move, the fuel tank should remain the same.
        '''
        # =====================type your code here=====================
        if self.fuel > 0 and action != 0:
            # 如果有燃料且執行移動動作
            # 計算燃料消耗
            # 這裡假設每次移動消耗 1 單位燃料
            # 這裡可以根據實際需求調整燃料消耗的計算方式
            # 例如，可以根據移動的距離或速度來計算燃料消耗
            # 執行動作並減少燃料
            self.fuel -= 1
            observation, reward, terminated, truncated, info = super().step(action)
        else:
            # 如果燃料耗盡，登陸器無法移動
            observation, reward, terminated, truncated, info = super().step(0)  # 假設 0 是 "無操作" 動作

        info = info or {}
        info['fuel'] = self.fuel  # 在 info 字典中包含剩餘燃料資訊
        return observation, reward, terminated, truncated, info
        # =============================================================
