class Solution {
public:
    /*
     * @param source: source string to be scanned.
     * @param target: target string containing the sequence of characters to match
     * @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
     */
    int strStr(const char *source, const char *target) {
        if( target != NULL && target[0] == '\0' )
            return 0;
        if( target == NULL || source == NULL || source[0] == '\0' )
            return -1;
        
        buildKmp( target );
        for( int i = 0, j = 0; source[i] != '\0'; )
        {
            if( source[i] == target[j] )
            {
                ++i;++j;
                if( target[j] == '\0' )
                {
                    return i-j;
                }
            }
            else if( j == 0 )
            {
                ++i;
            }
            else
            {
                j = kmp[i-1];
            }
        }
        return -1;
    }
    
    std::vector<int> kmp;
    
    void buildKmp(const char * target)
    {
        for( int j = 0, i = 1; target[i] != '\0'; )
        {
            if( target[i] == target[j] )
            {
                kmp.push_back(j+1);
                ++i;++j;
            }
            else if( j == 0 )
            {
                kmp.push_back(0);
                ++i;
            }
            else
            {
                j = kmp[j-1];
            }
        }
    }
};