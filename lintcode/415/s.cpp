class Solution {
public:
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    bool isPalindrome(string &s) {
        // write your code here
            if( s.empty() )
            return true;

        for( int i = 0, j = s.length()-1; i < j; )
        {
            if( !isAlphNum( s[i] ) )
                ++i;
            if( !isAlphNum( s[j] ) )
                --j;
            if( isAlphNum( s[i] ) && isAlphNum( s[j] ) )
            {
                if( ignoreCaseCompare( s[i], s[j]) )
                    {   ++i;--j;    }
                else
                    {   return false;   }
            }
        }
        return true;
    }

    bool isAlphNum( char c )
    {
        if( c >= 'a' && c <= 'z' )
            return true;
        if( c >= 'A' && c <= 'Z' )
            return true;
        if( c >= '0' && c <= '9' )
            return true;
        return false;
    }

    bool ignoreCaseCompare( char a, char b )
    {
        if( a >= 'A' && a <= 'Z' )
            a+= 'a' - 'A';
        if( b >= 'A' && b <= 'Z' )
            b+= 'a' - 'A';
        return a == b;
    }
};