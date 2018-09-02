#include<string>
#include<vector>
#include<queue>
#include<iostream>

using namespace std;

class Solution {
public:

    vector<int> kmp;
    deque<string> substrs;

    bool isMatch(string s, string p) {
        if( s.empty() && p.empty() )
            return true;
        else if( !s.empty() && p.empty() )
            return false;

        if( pickSubstrs(p) > s.length() )
            return false;

        if( !isHeadAndTailMatch(s) )
            return false;

        string substr = substrs.front();
        buildKmp( substr );
        cout << "before loop";

        // match all the substrings delimited by * in pattern one by one
        for( int i = 0, j = 0;  substrs.empty() || i < s.length(); )
        {
            if( s[i] == substr[j] || substr[j] == '?' )
            {
                if( j < substr.length() )
                {   
                    ++i; ++j;   
                }
                else if( !substrs.empty() )
                {   
                    // substr is a match in s, match next substr in substrs
                    substrs.pop_front();
                    substr = substrs.front();
                    buildKmp( substr );
                }
            }
            else if( j == 0 )
            {
                ++i;
            }
            else
            {
                j = kmp[j-1];
            }
        }
        if( substrs.empty() )
            return true;
        else
            return false;
    }

    bool isHeadAndTailMatch( string& s )
    {
        // try match the head and the tail with the first and the last substr
        // if it is a empty substr, it means  * at the begin or end, so it is a match regardless

        string head = substrs.front();
        if( !head.empty() && strCompare( head, s.substr(0,head.length())) )
            return false;

        string tail = substrs.back();
        if( !tail.empty() && strCompare(tail, s.substr(s.length()-tail.length(),tail.length())) )
            return false;

        substrs.pop_front();
        if( !substrs.empty() )
        {
            substrs.pop_back();
            s = s.substr( head.length(), s.length()-head.length()-tail.length());
        }
        else
        {
            s = s.substr( head.length(), s.length()-head.length());
        }

        return true;
    }

    // string compare ignore '?'
    bool strCompare( string a, string b )
    {
        if( a.length() != b.length() )
            return false;

        for( int i = 0; i < a.length(); ++i )
        {
            if( a[i] != b[i] && a[i] != '?' )
                return false;
        }
        return true;
    }

    int pickSubstrs( string p)
    {
        int nonStarChar = 0;
        string substr;
        for(int i = 0; i < p.length(); ++i )
        {
            if( p[i]=='*' )
            {
                substrs.push_back(substr);
                substr.clear();
            }
            else
            {
                nonStarChar++;
                substr.push_back(p[i]);
            }
        }
        substrs.push_back(substr);
        return nonStarChar;
    }

    void buildKmp( string p )
    {
        kmp.assign(p.length(),0);
        // loop through i to calculate the length of longest suffix that is prefix at p[i]
        for( int i = 1, j = 0, k = 0; i < p.length() && j < p.length(); ++k)
        {
            if( p[i] == p[j] )
                kmp[i++] = ++j;
            else if( j == 0 )
                kmp[i++] = 0;
            else
                j = kmp[j-1];
        }
    }

    void printKmp()
    {
        for( int i = 0; i < kmp.size(); ++i )
        {
            cout << kmp[i] << ",";
        }
    }    
};

int main()
{
    Solution s;
    cout << "\n is match" << s.isMatch("aa","a") <<"\n";
    cout << s.isMatch("aa","*");
    cout << s.isMatch("cb","?a");
    cout << s.isMatch("adceb","*a*b");
    cout << s.isMatch("acdcb","a*c?b");
    return 0;
}