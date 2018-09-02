class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {

        if( arr.empty() )
            return arr;

        int closestIndex = -1;
        for( closestIndex = 0; closestIndex < arr.size(); ++closestIndex )
        {
            if( arr[closestIndex] >= x )
                break;
        }
        if( closestIndex == arr.size() )
        {
            // if no element greater than x, return the last element
            --closestIndex;
        }
        else if( closestIndex - 1 >= 0)
        {
            closestIndex = x-arr[closestIndex-1]<=arr[closestIndex]-x ? closestIndex-1 : closestIndex;
        }

        int low = closestIndex, high = closestIndex;
        while( high-low+1 < k )
        {
            if( low - 1 < 0 )
            {
                low = 0;
                break;
            }
            else if( high + 1 >= arr.size() )
            {
                --low;
            }
            else if( x-arr[low-1] <= arr[high+1]-x )
            {
                --low;
            }
            else
            {
                ++high;
            }
        }
        
        return vector<int>( arr.begin()+low, arr.begin()+low+k);
    }
};