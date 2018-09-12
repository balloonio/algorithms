class Solution {
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        int mapRansom[256] = {0};
        int mapMagazine[256] = {0};
        for( int i = 0; i < ransomNote.size() || i < magazine.size(); ++i )
        {
            if( i < ransomNote.size() )
            ++mapRansom[ ransomNote[i] ];
            if( i < magazine.size() )
            ++mapMagazine[ magazine[i] ];
        }
        for( int i = 0; i < 256; ++i )
        {
            if( mapRansom[i] > mapMagazine[i] )
            return false;
        }
        return true;
    }
};

/*
 126 / 126 test cases passed.
 Status: Accepted
 Runtime: 26 ms
 Submitted: 0 minutes ago
 You are here!
 Your runtime beats 63.80% of cpp submissions.
*/
