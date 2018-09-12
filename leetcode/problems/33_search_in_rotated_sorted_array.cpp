/* Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
 */

class Solution {
public:
    
    int search(vector<int>& nums, int target) {
        
        if( nums.size() == 0 )
            return -1;
        
        return binarySearchPivot( nums,0,nums.size()-1,target );
    }
    
    int binarySearchPivot( vector<int>& nums, int start, int end, int target)
    {   
        int mid = (start + end) / 2;
        
        if( nums[mid] == target )
            return mid;
        else if( end == start )
            return -1;
        
        bool leftPartPivot = hasPivot( nums, start, mid );
        if( leftPartPivot )
        {
            if( target > nums[end] || target < nums[mid+1] )
                return binarySearchPivot(nums,start,mid,target);
            else
                return binarySearch(nums, mid+1, end,target );
        }
        else
        {
            if( target > nums[mid] || target < nums[start] )
                return binarySearchPivot(nums,mid+1,end,target);
            else
                return binarySearch(nums, start, mid,target );          
        }
    }
    
    int binarySearch( vector<int>& nums, int start, int end, int target )
    {
        int mid = (start + end) / 2;
        if( target == nums[mid] )
            return mid;
        else if( end == start )
            return -1;
        else if( target < nums[mid] )
            return binarySearch( nums, start, mid, target );
        else
            return binarySearch( nums, mid+1, end, target );
    }
    
    bool hasPivot(  vector<int>& nums, int start, int end )
    {
        if( nums[end] < nums[start] )
            return true;
        else
            return false;
    }
};