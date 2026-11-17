import json

FACTOR = 1  # 倍率（設定）

with open("input.json") as f:
    values = json.load(f)
answer = sum(values) / len(values)
print(answer * FACTOR)
