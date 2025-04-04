# run_pipeline.py

import os
import uuid
from generator import generate_strategy
from validator import is_valid_python
from backtester import run_backtest
from config import STRATEGY_FOLDER, RESULTS_FOLDER, LOG_FOLDER

os.makedirs(STRATEGY_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

def run():

    print("[🚀] 正在调用 AI 生成策略")

    strategy_code = generate_strategy()
    if not is_valid_python(strategy_code):
        print("[❌] 生成策略语法错误")
        return

    strategy_id = str(uuid.uuid4())[:8]
    strategy_path = os.path.join(STRATEGY_FOLDER, f"strategy_{strategy_id}.py")

    with open(strategy_path, "w", encoding="utf-8") as f:
        f.write(strategy_code)

    print(f"[✅] stragegy is complete：{strategy_path}")
    print("[⏳] Start backtesting...")

    result = run_backtest(strategy_path)

    result_path = os.path.join(RESULTS_FOLDER, f"{strategy_id}_result.txt")
    with open(result_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"[📈] 回测完成，结果保存于：{result_path}")

if __name__ == "__main__":
    run()
