from engine import GameEngine
import traceback

if __name__ == "__main__":
    try:
        game = GameEngine()
        game.run()
    except Exception as e:
        print("\n!!! 遊戲發生錯誤 !!!\n")
        traceback.print_exc()
        input("\n按 [Enter] 鍵退出...")