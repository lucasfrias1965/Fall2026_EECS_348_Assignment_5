from random import sample
import os, datetime, re, subprocess, time


SOLVABLE_BOARD = """\
5 3 9 8 2 4 1 7 6
1 8 6 5 7 9 2 4 3
4 7 2 1 3 6 8 9 5
9 2 4 3 8 7 5 6 1
3 1 8 6 9 5 4 2 7
6 5 7 4 1 2 3 8 9
7 4 5 2 6 1 9 3 8
8 9 1 7 4 3 6 5 2
2 6 3 9 5 8 7 1 4
"""

#splits thie input into how i need it
solv_board_formatted = re.split(r'[ \n\s]+', SOLVABLE_BOARD)[:-1]
print(solv_board_formatted)
input()

for i in range(0, 82):
    #build string and write it to file
    f = open("puzzle5.txt", "w")
    solv_board_formatted = re.split(r'[ \n\s]+', SOLVABLE_BOARD)[:-1]

    start = time.perf_counter()


# Source - https://stackoverflow.com/a/5597017
# Posted by user355252, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-24, License - CC BY-SA 3.0

    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['./a.out'], stdout=devnull, stderr=subprocess.STDOUT)


    for rs in sample(range(81), i):
        solv_board_formatted[rs] = "_"
    f.write("".join(solv_board_formatted))

    elapsed = time.perf_counter() - start

    print(f"diff is {elapsed}")
    open("results.txt", "a").write(f"M = {i} -> {elapsed}\n")
