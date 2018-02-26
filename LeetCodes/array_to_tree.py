"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
    	#YOUR CODE GOES HERE
    	##
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """
        Input: a list of values
        Output: a tree
        
        always dividing by 2 and start with the middle node as parent
        then in the left and right segments, use the middle node for each segments as children
        """
        if len(nums)==0:
            return
        else:
            #recursive, handing one to left then to right      
            #break when nums is empty
            div = int(len(nums)/2)
            parent = nums[div]
            left = nums[:div]
            right = nums[div+1:]
            t = TreeNode(parent)
            t.left = self.sortedArrayToBST(left)
            t.right = self.sortedArrayToBST(right)
            return t

        
#test cases
def main():
    nums = [1,2,3,4,5,6,7]
    s = Solution()
    t = s.sortedArrayToBST(nums)
    print ("Test Case 1:")
    print ("Your array is {}".format(nums))
    print ("Your result is {}, {}, {}, {}, {}, {}, {}".format(t.val, t.left.val, t.right.val, t.left.left.val, t.left.right.val, t.right.left.val, t.right.right.val))
    print ("{}".format(t.val))
    print ("{}".format(t.left.val))
    print ("{}".format(t.right.val))
    print ("{}".format(t.left.left.val))
    print ("{}".format(t.left.right.val))
    print ("{}".format(t.right.left.val))
    print ("{}".format(t.right.right.val))

    nums = [-10,-2,2,4,8,16]
    s = Solution()
    t = s.sortedArrayToBST(nums)
    print ("Test Case 2:")
    print ("Your array is {}".format(nums))
    print ("Your result is {}, {}, {}, {}, {}, {}".format(t.val, t.left.val, t.right.val, t.left.left.val, t.left.right.val, t.right.left.val))
    print ("{}".format(t.val))
    print ("{}".format(t.left.val))
    print ("{}".format(t.right.val))
    print ("{}".format(t.left.left.val))
    print ("{}".format(t.left.right.val))
    print ("{}".format(t.right.left.val))
#    print ("{}".format(t.right.right.val))
    
    nums = [-10,2,4,8,16]
    s = Solution()
    t = s.sortedArrayToBST(nums)
    print ("Test Case 3:")
    print ("Your array is {}".format(nums))
    print ("Your result is {}, {}, {}, {}, {}".format(t.val, t.left.val, t.right.val, t.left.left.val, t.right.left.val))
    print ("{}".format(t.val))
    print ("{}".format(t.left.val))
    print ("{}".format(t.right.val))
    print ("{}".format(t.left.left.val))
#    print ("{}".format(t.left.right.val))
    print ("{}".format(t.right.left.val))
#    print ("{}".format(t.right.right.val))
    
    nums = [-10]
    s = Solution()
    t = s.sortedArrayToBST(nums)
    print ("Test Case 4:")
    print ("Your array is {}".format(nums))
#    print ("Your result is {}, {}, {}, {}, {}, {}, {}".format(t.val, t.left.val, t.right.val, t.left.left.val, t.left.right.val, t.right.left.val, t.right.right.val))
    print ("{}".format(t.val))
# =============================================================================
#     print ("{}".format(t.left.val))
#     print ("{}".format(t.right.val))
#     print ("{}".format(t.left.left.val))
#     print ("{}".format(t.left.right.val))
#     print ("{}".format(t.right.left.val))
#     print ("{}".format(t.right.right.val))
# =============================================================================

if __name__ == "__main__":
    main()