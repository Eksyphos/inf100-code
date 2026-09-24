def clip_grass(heights,max_height):
    c = 0
    for height in heights:
        if height>max_height:
            heights[c]=max_height
        c+=1

