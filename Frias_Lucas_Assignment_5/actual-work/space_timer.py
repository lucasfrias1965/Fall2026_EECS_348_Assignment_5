from random import sample import os, re 


SOLVABLE_BOARD = """\ 5 3 9 8 2 4 1 7 6 1 8 6 5 7 9 2 4 3 4 7 2 1 3 6 8 9 5 9 2 4 3 8 7 5 6 1 3 1 8 6 9 5 4 2 7 6 5 7 4 1 2 3 8 9 7 4 5 2 6 1 9 3 8 8 9 1 7 4 3 6 5 2 2 6 3 9 5 8 7 1 4 """ 


RESULTS_FILE = "space_results.txt" # truncate/create the results file fresh for this run 

open(RESULTS_FILE, "w").close() 

for i in range(0, 82):     # start from a fresh copy of the solved board each iteration     
    board = re.split(r'[ \n\s]+', SOLVABLE_BOARD)[:-1]     
    for rs in sample(range(81), i):         
        board[rs] = "_"     
        with open("puzzle5.txt", "w") as f:        
            f.write("".join(board))     
            with open(os.devnull, "wb") as devnull:         
                pid = os.fork()         
                if pid == 0:             
                    os.dup2(devnull.fileno(), 1)  # stdout                          os.dup2(devnull.fileno(), 2)  # stderr                          os.execv("./a.out", ["./a.out"])             os._exit(127)  # only reached if execv fails         _, status, rusage = os.wait4(pid, 0)     if os.WIFEXITED(status) and os.WEXITSTATUS(status) != 0:         print(f"WARNING: a.out exited with status {os.WEXITSTATUS(status)} at M={i}")     # ru_maxrss is in kilobytes on Linux     max_rss_kb = rusage.ru_maxrss     print(f"M = {i} -> {max_rss_kb} KB")     with open(RESULTS_FILE, "a") as rf:         rf.write(f"M = {i} -> {max_rss_kb} KB\n") 
