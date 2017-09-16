class Solution {
public:

	//brutal force
    bool isPerfectSquare(int num) {
    	if( num <= 0 )
    		return false;

        int root = 1;
        do
        {
        	if( root*root == num )
        		return true;
        	++root;
        }while( root <= num/2 ) // little optimization

        return false;
    }

    

};