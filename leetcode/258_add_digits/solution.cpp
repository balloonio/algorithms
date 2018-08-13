class Solution {
public:
    int addDigits(int num)
    {
        if( num < 0 )
            num *= -1;
        return recDigitize( num );
    }
    
    int recDigitize( int num)
    {
        if( num/10 == 0 )
            return num;
        
        int temp = 0;
        while( num !=0 )
        {
            temp += num%10;
            num /=10;
        }
        return recDigitize( temp );
    }
};

/*
 Status: Accepted
 Runtime: 8 ms
 You are here!
 Your runtime beats 15.34% of cpp submissions.
*/