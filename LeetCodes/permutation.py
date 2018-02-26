"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Source: https://leetcode.com/problems/permutations/#/description
"""
#DO NOT CHANGE THIS CLASS
class Solution(object):
	#YOUR CODE GOES HERE
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



# =============================================================================
# def per(nums):
#     fac = len(nums)
#     print ('fac = {}'.format(fac))
#     if fac == 0:
#         return
#     temp = []
#     for i in nums:
#         print ('i = {}'.format(i))
# #        print ('i = {}'.format(nums))
# #        if len([item for item in nums if item not in [i]])!=0:
#         print ('item = {}'.format([item for item in nums if item not in [i]]))
#         thing = [item for item in nums if item not in [i]]
#         if len(thing)!=0:
#             s = per([item for item in nums if item not in [i]])
#             print ('s = {}'.format(s))
#             temp = temp + [s] + [i]
#             print ('temp = {}'.format(temp))
# #        print ('len(s) = {}'.format(len(s)))
#     #        if s != None:
#     #        for j in len(s):
#     #           if s[j] != None:
#     temp = temp + [i]
#     print ('temp = {}'.format(temp))
#         #temp = temp + [i]
#     return temp
# =============================================================================

def pem(nums):
    #base case:
    if not nums:
        return [[]]
    t=[]
    for i in nums:
#        print ('i = {}'.format(nums))
        arr = [item for item in nums if item != i]
#        print ('arr = {}'.format(arr))
        s = pem(arr)
#        print ('s = {}'.format(s))
#        t = []
#        print ('len(arr) = {}'.format(len(arr)))
#        if len(arr)!=0:
        for x in s:
            x.insert(0,i)# + s[j]])
        t.extend(s)
    return t #list of list
    
def per(nums):
    fac = len(nums)
    if fac > 0:
#        return
        temp = []
    #    print ('i = {}'.format(nums))
        for i in nums:
#            if len([item for item in nums if item not in [i]])!=0:
            s = per([item for item in nums if item not in [i]])
            print ('s = {}'.format(s))
    #        print ('len(s) = {}'.format(len(s)))
    #        if s != None:
    #        for j in len(s):
    #           if s[j] != None:
            temp = temp + [s] + [i]
    #            print ('i = {}'.format(i))
    #            print ('item = {}'.format([item for item in nums if item not in [i]]))
    #            print ('temp = {}'.format(temp))
                #temp = temp + [i]
        return temp

#test case
def main():
    arr = [1,2,3]
#    print (per(arr))
    print (pem(arr))
if __name__ == "__main__":
    main()