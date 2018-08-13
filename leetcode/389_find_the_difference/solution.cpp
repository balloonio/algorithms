class Solution {
public:
    char findTheDifference(string s, string t)
    {
        if( s.size() == 0 )
            return t[0];
        int sAsciiSum = 0, tAsciiSum = 0, i = 0;
        for( ; i != s.size(); ++i )
        {
            sAsciiSum += s[i];
            tAsciiSum += t[i];
        }
        tAsciiSum += t[i];
        return (char)(tAsciiSum-sAsciiSum);
    }
};

/*
52 / 52 test cases passed.
Status: Accepted
Runtime: 3 ms
You are here!
Your runtime beats 62.13% of cpp submissions.
*/