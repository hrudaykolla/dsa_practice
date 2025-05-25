#number the disks from 1 (smallest, topmost) to n (largest, bottom-most)

"""for 3 disks:
move disk 1: from pole_1 to ploe_3
move disk 2: from pole_1 to ploe_2
move disk 1: from pole_3 to ploe_2
move disk 3: from pole_1 to ploe_3
move disk 1: from pole_2 to ploe_1
move disk 2: from pole_2 to ploe_3
move disk 1: from pole_1 to ploe_3
"""

def TowerOfHanoi(n, from_rod, aux_rod, to_rod): 
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, to_rod, aux_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-1, aux_rod, from_rod, to_rod) 
  
  
# Driver code 
N = 4
  
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'B', 'C')