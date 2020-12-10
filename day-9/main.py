

def read_input_as_list(filename):
    return [int(line.strip()) for line in open(filename, 'r')]



if __name__ == '__main__':
    data = read_input_as_list(("9.txt"))
    preamble_length = 25

    # PART 1
    invalid_number = 0
    for i, number in enumerate(data):
        if i < preamble_length:
            continue
        found_combination = False
        for a in data[i - preamble_length:i]:
            for b in data[i - preamble_length:i]:
                #print(f"number: {number}\ta: {a}\tb: {b}")
                if a+b == number:
                    found_combination = True
                    break
            if found_combination:
                break
        if found_combination:
            continue
        else:
            print(f"Number {number} cannot be calculated with the preamble.")
            invalid_number = number
            break

    # PART 2
    print(invalid_number)
    found_it = False
    for i, a in enumerate(data):
        sum = a
        numbers = [a]
        for b in data[i+1:]:
            sum = sum + b
            numbers.append(b)
            if sum == invalid_number:
                min(numbers) + max(numbers)
                print(f"min: {min(numbers)}\tmax: {max(numbers)} is in sum: {min(numbers) + max(numbers)}")
                found_it = True
                break
            if sum > invalid_number:
                break
        if found_it:
            break