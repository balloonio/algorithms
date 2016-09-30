class Solution {
public:
    std::map<int,int> knowledge;
    
    int climbStairs(int n)
    {
        if( n <= 2)
            return n;
        
        std::map<int,int>::iterator it;
        if( (it = knowledge.find(n)) != knowledge.end() )
            return it->second;
        int path1 = climbStairs(n-1);
        int path2 = climbStairs(n-2);
        knowledge.insert( std::pair<int,int>(n-1,path1) );
        knowledge.insert( std::pair<int,int>(n-2,path2) );
        
        return path1+path2;
    }
};

/*
 45 / 45 test cases passed.
 Status: Accepted
 Runtime: 0 ms
 You are here!
 Your runtime beats 6.70% of cpp submissions.
*/
