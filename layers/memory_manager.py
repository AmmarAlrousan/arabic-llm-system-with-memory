import json
from datetime import datetime

def load_memory():
    try:
        with open("memory.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"long_term": {}, "short_term": []}

def save_memory(memory):
    with open("memory.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def update_short_memory(memory, user, assistant):
    memory["short_term"].append({
        "time": str(datetime.now()),
        "user": user,
        "assistant": assistant
    })
    memory["short_term"] = memory["short_term"][-8:]  # آخر 8 رسائل
    save_memory(memory)

def update_long_memory(memory, user, assistant):
    memory["long_term"][user] = assistant
    save_memory(memory)