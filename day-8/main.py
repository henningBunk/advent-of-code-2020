import re


def read_input_as_list(filename):
    return [line.strip() for line in open(filename, 'r')]


def value(instruction):
    return int(re.search("([+-]\d+)", instruction)[0])


def run_bootcode(code):
    accumulator = 0
    pointer = 0
    while True:
        #print(pointer)
        if pointer >= len(code):
            break
        if code[pointer][:3] == "nop":
            pointer += 1
            continue
        if code[pointer][:3] == "acc":
            accumulator = accumulator + value(code[pointer])
            code[pointer] = "end"
            pointer += 1
            continue
        if code[pointer][:3] == "jmp":
            pointer = pointer + value(code[pointer])
            continue
        if code[pointer][:3] == "end":
            break
    return accumulator


def find_corruption(code):
    ## run the bootcode backwards and mark every position with "win"
    last_line = len(code)
    code.insert(0, 0)
    stack = [last_line]
    while len(stack) != 0:
        current_line = stack.pop()
        #print(f"{current_line}")
        # Add lines above onto the stack if they aren't jumps
        previous_line = current_line - 1
        if code[previous_line][:3] == "nop":
            stack.append(previous_line)
        if code[previous_line][:3] == "acc":
            stack.append(previous_line)
        # Find Jumps which could reach the current line
        for other_line, line in enumerate(code[1:], 1):
            if code[other_line][:3] == "jmp":
                if current_line == other_line + value(line):
                    stack.append(other_line)
        code[current_line] = "win"

    return manipulate_and_run_bootcode(code[1:])


def manipulate_and_run_bootcode(code):
    ## run the manipulated bootcode and try if a jmp==nop or vice versa would hit a "win"
    pointer = 0
    while True:
        #print(pointer)
        if pointer > len(code):
            break
        if code[pointer][:3] == "nop":
            would_jump_to = pointer + value(code[pointer])
            if code[would_jump_to] == "win":
                print(f"Changing {code[pointer]} to a jump would hit a 'win' line")
                pointer = pointer + value(code[pointer])
                break
            pointer += 1
            continue
        if code[pointer][:3] == "acc":
            pointer += 1
            continue
        if code[pointer][:3] == "jmp":
            would_continue_to = pointer + 1
            if code[would_continue_to] == "win":
                print(f"Changing {code[pointer]} to a nop would hit a 'win' line")
                pointer = pointer + 1
                break
            pointer = pointer + value(code[pointer])
            continue
    return pointer


if __name__ == '__main__':

    bootcode = read_input_as_list("8.txt")
    accumulated = run_bootcode(bootcode)
    print(f"The boot code accumulates until {accumulated} than it enters a loop.\n")

    bootcode = read_input_as_list("8.txt")
    corruption = find_corruption(bootcode)
    print(f"Corruption in your bootcode found at line: '{corruption}'\n")

    # Bootcode is corrupt at line 426 "jmp -279" should be "nop -279"
    print(f"Repairing bootcode")
    bootcode = read_input_as_list("8.txt")
    bootcode[corruption - 1] = "nop -279"
    accumulated = run_bootcode(bootcode)
    print(f"The boot code accumulates until {accumulated} than it ends successfully.")
