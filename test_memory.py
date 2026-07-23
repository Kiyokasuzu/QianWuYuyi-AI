import json
from pathlib import Path


MEMORY_FILE = Path("data/memory.json")

USER_ID = "366648462"
QUERY = "事情"


def load_memory():
    if not MEMORY_FILE.exists():
        print("memory.json 不存在")
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def search_memory(data, user_id, query, limit=3):
    results = []

    for mem in reversed(data):
        if mem.get("user_id") != user_id:
            continue

        content = mem.get("content", "")

        if query in content or any(word in content for word in query.split()):
            results.append(mem)

            if len(results) >= limit:
                break

    return results


def main():
    data = load_memory()

    results = search_memory(
        data,
        USER_ID,
        QUERY
    )

    print(f"找到 {len(results)} 条相关记忆")

    for r in results:
        role = r.get("role", "unknown")
        content = r.get("content", "")

        print(f"  {role}: {content[:80]}...")


if __name__ == "__main__":
    main()
