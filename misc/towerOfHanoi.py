#number the disks from 1 (smallest, topmost) to n (largest, bottom-most)
"""
Recursive idea:
To move n disks from rod A to rod C:

step: 1 Move n-1 disks from A → B using C as auxiliary
step: 2 Move the nth (largest) disk from A → C
step: 3 Move the n-1 disks from B → C using A as auxiliary
"""

"""
for 3 disks:
    move disk 1: from pole_1 to pole_3
    move disk 2: from pole_1 to pole_2
    move disk 1: from pole_3 to pole_2
    move disk 3: from pole_1 to pole_3
    move disk 1: from pole_2 to pole_1
    move disk 2: from pole_2 to pole_3
    move disk 1: from pole_1 to pole_3
"""

def TowerOfHanoi(n, source, target, auxiliary, depth=0):
    indent = "  " * depth  # Visualize recursion depth

    if n == 1:
        print(f"{indent}Move disk 1 from {source} to {target}")
        return

    #print(f"{indent}Move top {n-1} disks from {source} to {auxiliary} (using {target} as auxiliary)")
    TowerOfHanoi(n - 1, source, auxiliary, target, depth + 1) # step -1

    print(f"{indent}Move disk {n} from {source} to {target}") # step -2

    #print(f"{indent}Move top {n-1} disks from {auxiliary} to {target} (using {source} as auxiliary)")
    TowerOfHanoi(n - 1, auxiliary, target, source, depth + 1) # step -3

if __name__ == "__main__": 
    N = 3
    
    TowerOfHanoi(N, 'A', 'C', 'B')