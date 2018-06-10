class Solution {
public:
    string minWindow(string s, string t) {
        int head = 0, tail = 0, countUnmetCharInT = t.length() ;
        string result;
        unordered_map<char,int> map;
        
        buildCountMap( map, t );
        
        while( tail < s.length() )
        {
            if( map.find( s[tail] ) != map.end() )
            {
                if( map[s[tail]] > 0 )
                {
                    // a char we need in t and not an extra
                    countUnmetCharInT--;
                }
                
                map[s[tail]]--; // decrease numbers of this char still needed
                
                if( countUnmetCharInT == 0 ) // all character are met
                {
                    shrinkHead( head, s, map);
                    string replaceCandidate = s.substr( head, tail-head+1); // +1 to be inclusive on tail
                    if( result.empty() || result.length() > replaceCandidate.length())
                        result=replaceCandidate;
                }
            }
            ++tail;
        }
        return result;
    }
    
    void buildCountMap( unordered_map<char,int>& map, string& t )
    {
        for( int i = 0; i < t.length(); ++i )
        {
            ++map[t[i]];
        }
    }
    
    void shrinkHead( int& head, string& s, unordered_map<char,int>& map)
    {
        while(true)
        {
            if( map.find( s[head]) != map.end() && map[s[head]] == 0  )
            {
                break;
            }
            else if( map.find( s[head]) != map.end() && map[s[head]] < 0 )
            {
                map[s[head]]++;
            }
            head++;
        }
    }
};
