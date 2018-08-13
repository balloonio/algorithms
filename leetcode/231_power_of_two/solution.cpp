class Solution {
public:
    bool isPowerOfTwo(int n) {
        if( n <= 0 )
            return false;
        int numOfOnBit = 0;
        for( int i = 0; i < sizeof(n)*8 ; ++i )
        {
            numOfOnBit += (n >> i) & 1;
        }
        return numOfOnBit == 1;
    }
};

/*
1108 / 1108 test cases passed.
Status: Accepted
Runtime: 3 ms
You are here!
Your runtime beats 33.45% of cpp submissions.
*/