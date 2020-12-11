import sys
import time
sys.setrecursionlimit(100000)


def read_input_as_list(filename):
    return [int(line.strip()) for line in open(filename, 'r')]


samplea = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]  # 8
sampleb = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34,
           10, 3]  # 19208

input = read_input_as_list("10.txt")
#input = sampleb

# Prepare the data by sorting and adding the wall plug (0) and the device (max +3) to the list
input.sort()
input.insert(0, 0)
input.append(max(input) + 3)

# Part 1
diff = {1: 0, 2: 0, 3: 0}
for i, plug in enumerate(input):
    if i + 1 < len(input):
        diff[input[i + 1] - plug] += 1
print(f"These are the occurences of steps between chargers: {diff}")
print(f"The result for question one is: {diff[1] * diff[3]}\n")


# Part 2, done by recursion with memoization
def memoize(f):
    memo = {}

    def helper(x):
        hash = sum(x)
        if hash not in memo:
            memo[hash] = f(x)
        return memo[hash]

    return helper


def count_combinations(list):
    count = 0
    if len(list) == 1:
        return 1

    count += count_combinations(list[1:])
    if len(list) > 2 and list[0] + 3 >= list[2]:
        count += count_combinations(list[2:])
    if len(list) > 3 and list[0] + 3 >= list[3]:
        count += count_combinations(list[3:])
    return count


start = time.time()

count_combinations = memoize(count_combinations)
combinations = count_combinations(input)

end = time.time()
print(f"There are {combinations} different combinations how you can connect your device to the wall plug.")
print(f"Calculation took {(end - start) * 1000:02f} ms")
