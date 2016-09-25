#include <algorithm>

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        if( nums1.empty() || nums2.empty() )
        {
            vector<int> blackVector;
            return blackVector;
        }
        
        int i1 = 0, i2 = 0;
        vector<int> result;
        sort( nums1.begin(), nums1.end() );
        sort( nums2.begin(), nums2.end() );
        
        while( i1<nums1.size() && i2<nums2.size() )
        {
            if( nums1[i1]==nums2[i2] && (result.empty() || result.back()!=nums1[i1]) )
            {
                result.push_back( nums1[i1] );
            }
            else if( nums1[i1] < nums2[i2] )
            {
                ++i1;
            }
            else
            {
                ++i2;
            }
        }
        return result;
    }
    
};

/*
 60 / 60 test cases passed.
 Status: Accepted
 Runtime: 9 ms
 You are here!
 Your runtime beats 62.87% of cpp submissions.
*/