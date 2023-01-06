# Basic Python starter
import freader

INPUT_FILE = "input.txt"

def main():
    dat = freader.read_file_line_split(INPUT_FILE)
    a = 0
    elves = []
    for calorie in dat:
        # print(calorie)
        if calorie != "":
            x = int(calorie)
            a = x + a
        else:
            elves.append(a) 
            print(a)
            a = 0
    print(elves)
    print(max(elves))

if __name__ == "__main__":
    main()