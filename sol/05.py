def get_data():
    with open("input/05.txt", "r") as f:
        rules = {}
        updates = []
        is_rules = True
        for line in f:
            if line == "\n":
                is_rules = False
                continue
            if is_rules:
                prev, curr = map(int, line.strip("\n").split("|"))
                if prev not in rules:
                    rules[prev] = [curr]
                else:
                    rules[prev].append(curr)
            if not is_rules:
                updates.append([int(x) for x in line.strip("\n").split(",")])
    return rules, updates

def is_valid_update(pages, rules):
    for i in range(len(pages)-1):
        if pages[i] not in rules or pages[i+1] not in rules[pages[i]]:
            return False
    return True

def solution_Q1(rules, updates):
    res = 0
    for pages in updates:
        if is_valid_update(pages, rules):
            res += pages[(len(pages)-1)//2]
    return res

def solution_Q2(rules, updates):
    res = 0
    for pages in updates:
        if not is_valid_update(pages, rules):
            for i in range(1, len(pages)):
                j = i
                while j > 0 and (pages[j - 1] not in rules or pages[j] not in rules[pages[j - 1]]):
                    pages[j], pages[j - 1] = pages[j - 1], pages[j]
                    j -= 1
            if is_valid_update(pages, rules):
                res += pages[(len(pages) - 1) // 2]
    return res
            
def main():
    ans_Q1 = solution_Q1(*get_data())
    ans_Q2 = solution_Q2(*get_data())
    print(f"answer to Q1: {ans_Q1}")
    print(f"answer to Q2: {ans_Q2}")
    
if __name__ == "__main__":
    main()

