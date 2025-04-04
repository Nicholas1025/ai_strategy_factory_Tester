# config.py

OPENAI_API_KEY = " "  # <- Your API Key
MODEL_NAME = "gpt-3.5-turbo"   

STRATEGY_FOLDER = "strategy_output"
RESULTS_FOLDER = "results"
LOG_FOLDER = "logs"
PROMPT_FOLDER = "prompts"

BACKTEST_COMMAND_TEMPLATE = "python3 prosperity3bt/main.py {strategy_file}"  # 改成你的 backtester 命令
