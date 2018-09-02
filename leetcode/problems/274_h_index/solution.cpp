class Solution {
public:
    int hIndex(vector<int>& citations) {
        if( citations.empty() )
            return 0;
        
        int uncounted = 0;
        vector<int> bucket( citations.size()+1, 0 );
        for( int i = 0; i < citations.size(); ++i )
        {
            if( citations[i] <= citations.size() )
                ++bucket[ citations[i] ];
            else
                ++uncounted;
        }
        
        for( int i = 0; i < bucket.size(); ++i )
        {
            if( i != 0 )
                bucket[i] += bucket[i-1];
        }
        
        for( int i = bucket.size()-1; i >= 0; --i )
        {
            if( uncounted + bucket[ bucket.size()-1] - bucket[i-1] >= i )
                return i;
        }
        return 0;
    }
    
};