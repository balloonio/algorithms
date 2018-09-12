class Solution {
public:
    /**
     * @param nums: A list of integers
     * @param k: An integer
     * @return: The median of the element inside the window at each moving
     */
    vector<int> medianSlidingWindow(vector<int> &nums, int k) {
        // write your code here
        if ( nums.empty() or k == 1 )
        {
            return nums;
        }

        int n = nums.size();
        int n_result = n - k + 1;
        vector<int> result;
        result.reserve( n_result );

        std::multiset<int> left;
        std::multiset<int> right;

        // initialize left and right
        for( int i = 0; i < k; ++i )
        {
            if( left.size() <= right.size() )
            {
                left.insert( nums[i] );
            }
            else
            {
                right.insert( nums[i] );
            }

            if( left.empty() or right.empty() )
            {
                continue;
            }

            // max of left > min of right, then swap
            if( *left.rbegin() > *right.begin() )
            {
                int small = *right.begin();
                int big = *left.rbegin();

                auto itr = left.find(big);
                left.erase(itr);
                left.insert(small);

                itr = right.find(small);
                right.erase(itr);
                right.insert(big);
            }
        }

        for( int i = 0; i < n_result; ++i )
        {
            // take min from right
            int median = *left.rbegin();
            result.push_back( median );

            // cout << left.size() << " " << right.size() ;

            // remove nums[i] right or left
            if( nums[i] <= *left.rbegin() )
            {
                auto itr = left.find(nums[i]);
                left.erase(itr);
            }
            else
            {
                auto itr = right.find(nums[i]);
                right.erase(itr);
            }

            // insert nums[i+k] if there is
            if( i+k == n )
            {
                break;
            }

            if( left.size() <= right.size() )
            {
                left.insert( nums[i+k] );
            }
            else
            {
                right.insert( nums[i+k] );
            }

            if( left.empty() or right.empty() )
            {
                continue;
            }

            // max of left > min of right, then swap
            if( *left.rbegin() > *right.begin() )
            {
                int small = *right.begin();
                int big = *left.rbegin();

                auto itr = left.find(big);
                left.erase(itr);
                left.insert(small);

                itr = right.find(small);
                right.erase(itr);
                right.insert(big);
            }
        }

        return result;
    }

};
