"""
Merge two sorted lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Source: https://leetcode.com/problems/merge-two-sorted-lists/#/description
"""


def merge_two_list_helper(list1, list2):
	#NOTE: YOU CAN NOT USE ANY SORTING LIBRARIES
	#YOUR CODE GOES HERE
    """
    Input: Two sorted lists: list1 and list2
    Output: One merged sorted list
	
    have two index, one each that comb through each list
    Have a while loop that runs and
    build a new list that takes the smallest value between the item popping out of each list everytime
    wrap the code up with adding whichever list still has items in it to the merged string
    """
    merged_list=[]
#    len_total = len(list1) + len(list2)
    index_1=0
    index_2=0
    while index_1<len(list1) and index_2<len(list2):
        if list1[index_1] < list2[index_2]:
            merged_list = merged_list + [list1[index_1]]
            index_1 += 1
        else:
            merged_list = merged_list + [list2[index_2]]
            index_2 += 1
    if index_1 < len(list1):
        merged_list = merged_list + list1[index_1:]
    elif index_2 < len(list2):
        merged_list = merged_list + list2[index_2:]
    
    return merged_list


#DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1,list2):
	return merge_two_list_helper(list1, list2)


#test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print ("merging [1,3,5] and [2,4,6]......")
    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))
    
    list1 = [1,2,3,5,7]
    list2 = [2,4,6,7,8,9]
    print ("merging {} and {}......".format(list1,list2))
#    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))

if __name__ == "__main__":
    main()
