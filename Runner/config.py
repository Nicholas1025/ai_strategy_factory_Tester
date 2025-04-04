# config.py

OPENAI_API_KEY = "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"  # <- 填你自己的 API Key
MODEL_NAME = "gpt-3.5-turbo"  # 或 gpt-3.5-turbo 可改

STRATEGY_FOLDER = "strategy_output"
RESULTS_FOLDER = "results"
LOG_FOLDER = "logs"
PROMPT_FOLDER = "prompts"

BACKTEST_COMMAND_TEMPLATE = "python3 prosperity3bt/main.py {strategy_file}"  # 改成你的 backtester 命令
