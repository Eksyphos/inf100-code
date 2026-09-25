def find_treasure(grid,target_sum):
    bredde = len(grid[0])
    høyde = len(grid)
    koordinater = []
    for row in range(høyde):
        
        for collumn in range(bredde):
            result = row+collumn+grid[row][collumn]
            if result==target_sum:
                newlist = [row,collumn]
                koordinater.append(newlist)
    return koordinater