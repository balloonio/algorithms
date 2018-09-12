/*
class Solution {
public:
    int firstUniqChar(string s)
    {
        int map[255] = {0};
        for(int i=0;i<s.size();++i)
        {
            map[s[i]]+=1;
        }
        for(int i=0;i<s.size();++i)
        {
            if(map[s[i]]==1)
                return i;
        }
        return -1;
    }
};

 104 / 104 test cases passed.
 Status: Accepted
 Runtime: 58 ms
 Submitted: 1 hour, 52 minutes ago
 You are here!
 Your runtime beats 52.67% of cpp submissions.
*/

class Solution {
public:
    int firstUniqChar(string s)
    {
        // fix char size
        int map[256] = {0};
        for(int i=0;i<s.size();++i)
        {
            // IMPORTANT: pre-increment significantly improved speed
            ++map[s[i]];
        }
        for(int i=0;i<s.size();++i)
        {
            if(map[s[i]]==1)
                return i;
        }
        return -1;
    }
};

/*
 104 / 104 test cases passed.
 Status: Accepted
 Runtime: 42 ms
 You are here!
 Your runtime beats 92.83% of cpp submissions.
*/