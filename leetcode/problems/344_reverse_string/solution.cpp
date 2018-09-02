class Solution {
public:
    string reverseString(string s)
    {
        if( s.size() == 0 )
            return s;
        string result;
        for( int i = s.size()-1; i >= 0; --i )
        {
            result += s[i];
        }
        return result;
    }
};

/*
476 / 476 test cases passed.
Runtime: 9 ms
You are here!
Your runtime beats 42.79% of cpp submissions.
*/