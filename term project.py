from chem_reaction import chem_reactions

def function1():
    substance = input("請輸入要查詢的純物質（例如 CO2）：").strip()

    if substance not in chem_reactions:
        print("查無此純物質。")
        return

    reactions = chem_reactions[substance]

    print(f"\n{substance} 的相關反應：")
    for idx, data in reactions.items():
        print(f"{idx}. {data['equation']}")

    try:
        choice = int(input("\n請輸入要查看的反應編號："))
    except ValueError:
        print("請輸入有效的整數編號。")
        return

    if choice not in reactions:
        print("此編號不存在。")
        return

    selected = reactions[choice]
    print("\n反應資訊：")
    print(f"反應式：{selected['equation']}")
    print(f"反應性質：{selected['property']}")
    print(f"反應條件：{selected.get('conditions', '無')}")
    print(f"是否可逆：{'是' if selected.get('reversible') else '否'}")

def parse_equation(equation):
    equation = equation.replace(" ", "")
    
    reversible = "⇌" in equation
    equation = equation.replace("⇌", "→")
    
    if "→" not in equation:
        raise ValueError(f"反應式格式錯誤，缺少 '→': {equation}")
    
    left, right = equation.split("→")
    reactants = set(r.lstrip("0123456789") for r in left.split("+"))
    products = set(p.lstrip("0123456789") for p in right.split("+"))
    
    return reactants, products, reversible

def build_reaction_graph(chem_reactions):
    graph = {}

    for _, reactions in chem_reactions.items():
        for data in reactions.values():
            eq = data["equation"]
            prop = data.get("property", "未知")

            # 這裡修正 conditions 和 reversible
            conditions = data.get("conditions", "無")            # ← 修正這行
            reversible_flag = data.get("reversible", False)      # ← 修正這行
            reactants, products, reversible_eq = parse_equation(eq)
            reversible = reversible_flag or reversible_eq        # ← 修正這行

            # 將資料放入 graph
            for r in reactants:
                graph.setdefault(r, [])
                for p in products:
                    graph[r].append({
                        "to": p,
                        "equation": eq,
                        "property": prop,
                        "conditions": conditions,       # ← 加入到 edge
                        "reversible": reversible        # ← 加入到 edge
                    })

            # 若反應可逆，自動加反向
            if reversible:
                for p in products:
                    graph.setdefault(p, [])
                    for r in reactants:
                        graph[p].append({
                            "to": r,
                            "equation": eq,
                            "property": prop,
                            "conditions": conditions,   # ← 加入到 edge
                            "reversible": reversible    # ← 加入到 edge
                        })

    return graph

from collections import deque

def find_reaction_path(graph, start, target):
    queue = deque()
    queue.append((start, []))
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == target:
            return path
        if current in visited:
            continue
        visited.add(current)
        for edge in graph.get(current, []):
            next_node = edge["to"]
            queue.append((
                next_node,
                path + [(current, next_node, edge)]
            ))
    return None

def function2(start, target, chem_reactions_extended):
    graph = build_reaction_graph(chem_reactions_extended)
    path = find_reaction_path(graph, start, target)

    if path is None:
        print(f"找不到從 {start} 轉換到 {target} 的反應路徑。")
        return

    print(f"找到從 {start} 到 {target} 的反應路徑：\n")
    for i, (frm, to, edge) in enumerate(path, 1):
        print(f"Step {i}: {frm} → {to}")
        print(f"  反應式：{edge['equation']}")
        print(f"  性質：{edge['property']}")
        print(f"  條件：{edge.get('conditions', '無')}")
        print(f"  可逆性：{'是' if edge.get('reversible') else '否'}\n")

def main():
    while True:
        print("\n請選擇功能：") 
        print("1. 查詢化合物反應 (function1)") 
        print("2. From A to B (function2)") 
        print("3. 離開程式")
        choice = input("輸入 1、2 或 3: ").strip() 

        if choice == "1": 
            function1() 

        elif choice == "2": 
            start = input("請輸入起始化合物 A：").strip()
            target = input("請輸入目標化合物 B：").strip()
            function2(start, target, chem_reactions)

        elif choice == "3":
            print("程式已結束")
            break

        else: 
            print("輸入錯誤，請輸入 1、2 或 3")

if __name__ == "__main__":
    main()