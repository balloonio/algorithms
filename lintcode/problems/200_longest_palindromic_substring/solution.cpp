class Solution {
public:
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    string str;
    vector<int> m; //M's algo

    string longestPalindrome(string &s) {

        // If s is empty or has only 1 character, pld is itself
        if( s.size() <= 1 )
            return s;

        modifyAndStoreS(s);
        m.assign( str.size(),1); // every char is at least pld with length 1

        int c = 0, r = 0; //explored pld center index, right boundary index

        // handle through all from index 1 until center reached last item
        // no need to start from index 0 because its longest pld possible is 1
        for( int i = 1; i < str.length(); )
        {
            // calculate currently the pld length at index i
            // if i is smaller than r, means we can copy the pld length from mirror part
            // i's pld is at least MIN( the pld length of mirror part, double distance from i to right boundary inclusive )
            if( i < r )
            {
                int mi = getMirrorIndex(i,c);
                int lenCutByR = 2*(r-i)+1;
                m[i] = min( m[mi], lenCutByR );
            }

            // If i's pld is not reaching r, then we are sure it is the pld's final length, no need to explore beyond r
            if( i + m[i]/2 < r )
            {
                ++i;
            }
            else
            {
                c = i; // since i's pld is reaching r boundary, update center to i
                ++i;
                r = c > r ? c : r ; // if c is ahead of r, update r; this happens when previous pld was 1 char, r==c before c=i

                // r-c+1 is the distance from c to the first item after r, that is the distance we need to start explore
                for( int j = r-c+1; c-j >= 0 && c+j < str.size() && str[c-j] == str[c+j]; ++j )
                {
                    m[c]+=2;
                    r = c + j;
                }
            }
        }

        int start = 0, len = 0;
        getResultFromM( start, len );
        return s.substr( start, len );
    }

    // Add special character between each character so that even size pld can be handled same way
    // s size wont be empty or one here
    // "abcbb" -> "a#b#c#b#b"
    void modifyAndStoreS(string& s)
    {
        stringstream ss;
        ss << s[0];
        for( int i = 1; i < s.size(); ++i )
        {
            ss << '#' << s[i];
        }
        str = ss.str();
    }

    int min( int x, int y )
    {
        return x<y ? x : y;
    }

    // assuming i is greater than c
    int getMirrorIndex( int i, int c )
    {
        return c- (i-c);
    }

    void getResultFromM( int& startIndex, int& realLenMax )
    {
        int center = 0;
        for( int i = 0; i < m.size(); ++i )
        {
            // remove number of specail charactor to get real length
            int r = i + m[i]/2;
            int realLen = m[i] - m[i]/2 - r%2;
            if( realLen > realLenMax )
            {
                realLenMax = realLen;
                center = i;
            }
        }

        startIndex = center - m[center]/2;
        startIndex = (startIndex + 1)/2;
    }
};