# backtester.py

import subprocess
import os
from config import BACKTEST_COMMAND_TEMPLATE

def run_backtest(strategy_path: str) -> str:
    command = BACKTEST_COMMAND_TEMPLATE.format(strategy_file=strategy_path)
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Backtest timed out."
