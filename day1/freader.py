from typing import List

def read_file(filename: str) -> str:
    f = open(filename, "r")
    return f.read()

def read_file_line_split(filename: str) -> List[str]:
    dat = read_file(filename)
    return dat.splitlines()
