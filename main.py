import sys
import time
sys.setrecursionlimit(100000)


def read_input_as_list(filename):
    return [int(line.strip()) for line in open(filename, 'r')]


def combinations(list, path, depth):
    count = 0
    if len(list) == 1:
        # print(path)
        return 1

    count += combinations(list[1:], path + f", a:{list[1]}", depth+1)
    if len(list) > 2 and list[0] + 3 >= list[2]:
        # print(f"list[0]+3:{list[0] + 3}\tlist[2]:{list[2]}\tlist{list}")
        count += combinations(list[2:], path + f", b:{list[2]}", depth+1)
    if len(list) > 3 and list[0] + 3 >= list[3]:
        count += combinations(list[3:], path + f", c:{list[3]}", depth+1)
    return count


# 1, 2, 3, 4
#    2, 3, 4
#       3, 4
# 1, 2,    4
# 1,    3, 4
#    2, 3, 4
#    2,    4


mysample = [0, 1, 2, 3, 4, 7]
samplea = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]  # 8
sampleb = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
           10, 3]  # 19208

#input = read_input_as_list("10.txt")
input = sampleb
input.sort()
diff = {1: 0, 2: 0, 3: 1}
diff[input[0]] = + 1

# Part 1
for i, plug in enumerate(input):
    if i + 1 < len(input):
        diff[input[i + 1] - plug] += 1
# print(diff[1] * diff[3])

# Part 2
input.insert(0, 0)
input.append(max(input) + 3)
start = time.time()
print(combinations(input, "0", 0))
end = time.time()
print(end - start)