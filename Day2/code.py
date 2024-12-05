f = open('Day2/input.txt', 'r')

lines = f.readlines()

data = [line.split() for line in lines]


num_safe_1 = len(data)
num_safe_2 = len(data)

for report in data:

    increasing = (int(report[1]) - int(report[0])) > 0
    dampener = 1
    
    # check direction
    for i in range(1,len(report)):

        diff = int(report[i]) - int(report[i-1])

        if (diff == 0) or (diff < 0 and increasing) or (diff > 0 and not increasing) or abs(diff) > 3:

            num_safe_1 -= 1
            break
        
print(f'Part 1: {num_safe_1}')


num_safe_2 = len(data)

for report in data:

    increasing = (int(report[1]) - int(report[0])) > 0

    dampener = 1
    
    # check direction
    for i in range(1,len(report)):


        diff = int(report[i]) - int(report[i-1])

        if (diff == 0) or (diff < 0 and increasing) or (diff > 0 and not increasing) or abs(diff) > 3:
            if dampener:
                dampener = 0
                continue
            if not dampener:
                num_safe_2 -= 1
                break
        

print(f'Part 2: {num_safe_2}')







