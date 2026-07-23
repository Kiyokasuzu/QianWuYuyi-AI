import json
from pathlib import Path


def test_memory_search():

    path = Path("data/memory.json")

    if not path.exists():
        return

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    query = "事情"

    results = []

    for mem in reversed(data):
        content = mem.get("content", "")

        if query in content:
            results.append(mem)

        if len(results) >= 3:
            break

    assert isinstance(results, list)

    print(f"找到 {len(results)} 条相关记忆")
