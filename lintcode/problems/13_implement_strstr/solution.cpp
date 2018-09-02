class Solution {
public:
    /*
     * @param source: A source string
     * @param target: A target string
     * @return: An integer as index
     */
    int strStr(const char* source, const char* target) {
        if( target != NULL && target[0] == '\0' )
            return 0;
        if( target == NULL || source == NULL || source[0] == '\0' )
            return -1;
        
        buildKmp( target );
        for( int i = 0, j = 0; source[i] != '\0' && target[j] != '\0'; )
        {
            if( source[i] == target[j] )
            {
                ++i;++j;
                if( target[j] == '\0' )
                {
                    return i - j;
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
        return -1;
    }
    
    std::vector<int> kmp;
    
    int len( const char* target )
    {
        int length = 0;
        
        while( target[length] != '\0' )
            ++length;
        
        return length;
    }
    
    void buildKmp(const char * target)
    {
        kmp.assign( len(target), 0 );
        for( int j = 0, i = 1; target[i] != '\0'; )
        {
            if( target[i] == target[j] )
            {
                kmp[i] = j + 1;
                ++i;++j;
            }
            else if( j == 0 )
            {
                kmp[i] = 0;
                ++i;
            }
            else
            {
                j = kmp[j-1];
            }
        }
    }
};