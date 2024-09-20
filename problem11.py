Find All Pairs in a List that Sum to a Specific Value
Write a Python function to find all pairs in a list that sum to a specific value.
Input: [1, 2, 3, 4, 5], Sum=6
Output: [(1, 5), (2, 4)]

solution:
def pair_to_sum(input,sum):
    list_size=len(input)
    pair_list=[]
    for ii in range(0,list_size):
        jj=ii+1
        for jj in range(jj,list_size):
            if input[ii]+input[jj]==sum:
                pair_list.append((input[ii],input[jj]))
    return pair_list


input=[1,2,3,4,5,6]
sum=6
print(pair_to_sum(input,sum))
