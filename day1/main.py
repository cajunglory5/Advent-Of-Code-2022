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
    elves.sort(reverse=True)
    print(elves)
    print(elves[0]+elves[1]+elves[2])

if __name__ == "__main__":
    main()