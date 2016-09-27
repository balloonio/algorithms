class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if( s.length() != t.length())
            return false;
        
        int arr[26] = {0};
        
        for(int i = 0; i<s.length(); i++)
        {
            arr[s.at(i)-'a']++;
            arr[t.at(i)-'a']--;
        }
        
        for(int i = 0; i < 26; i++)
        {
            if( arr[i] != 0 )
                return false;
        }
        
        return true;
    }
};

/*
 Status: Accepted
 Runtime: 16 ms
 Submitted: 1 year ago
 You are here!
 Your runtime beats 55.56% of cpp submissions.
*/