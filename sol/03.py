import re

def Q1_sum_product(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)
    
    res = 0
    for match in matches:
        x, y = map(int, match)
        res += x * y
    return res

def Q2_sum_product(text):
    pattern = r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don\'t\(\))"
    matches = re.findall(pattern, text)

    res = 0
    skip = False
    for match in matches:
        pair, do, dont = match
        if do == "do()":
            skip = False
        elif dont == "don't()":
            skip = True
            continue
        elif not skip:
            x, y = map(int, pair.split(","))
            res += x * y
    return res

def main():
    Q1_res = 0
    Q2_res = 0
    with open("input/03.txt", "r") as file:
        instruction = file.read()
        Q1_res += Q1_sum_product(instruction)
        Q2_res += Q2_sum_product(instruction)
    print(f"answer to Q1: {Q1_res}")
    print(f"answer to Q2: {Q2_res}")

if __name__ == '__main__':
    main()