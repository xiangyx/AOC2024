def is_strictly_increasing_or_decreasing(report):
    diff = [y - x for x, y in zip(report[:-1], report[1:])]
    is_increasing = all(1 <= d and d <= 3 for d in diff)
    is_decreasing = all(-3 <= d and d <= -1 for d in diff)
    return is_increasing or is_decreasing

def is_report_safe(report):
    if is_strictly_increasing_or_decreasing(report):
        return True
    for i in range(len(report)):
        sub_report = report[:i] + report[i+1:]
        if is_strictly_increasing_or_decreasing(sub_report):
            return True
            
def main():
    Q1_safe_reports = 0
    Q2_safe_reports = 0
    with open("input/02.txt", "r") as reports:
        for report in reports:
            report = report.split()
            report = [int(level) for level in report]
            if is_strictly_increasing_or_decreasing(report):
                Q1_safe_reports += 1
            if is_report_safe(report):
                Q2_safe_reports += 1
    print(f"answer to Q1: {Q1_safe_reports}")
    print(f"answer to Q2: {Q2_safe_reports}")

if __name__ == '__main__':
    main()
    
