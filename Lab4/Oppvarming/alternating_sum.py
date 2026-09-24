def alternate_sign_sum(nums):
    c = 0
    numsum = 0
    for num in nums:
        if c%2==0:
            numsum+=num
        else:
            numsum-=num
        c+=1
    return numsum
