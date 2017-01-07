class Solution {
public:

    // * modifying the vector is a lot faster than using a set
    // * improve to use O(1) space?
    // * dfs bfs?

    //std::set< std::pair<int,int> > traversedPoints;

    int countBattleships(vector<vector<char>>& board) {
        int numberOfShip = 0;
        for( int i = 0; i < board.size(); ++i )
        {
            for( int j = 0; j <board[i].size(); ++j )
            {
                //if we already traversed this point, skip
                //if( traversedPoints.find( std::pair<int,int>(i,j)) != traversedPoints.end() )
                if( board[i][j] == 'Y' )
                    continue;

                //otherwise, if it is water, add to traversed and skip
                if( board[i][j] == '.' )
                {
                    //traversedPoints.insert( std::pair<int,int>(i,j) );
                    board[i][j] = 'Y';
                    continue;
                }
                //otherwise, that is, it is part of a ship; traverse all the part of the ship
                else
                {
                    ++numberOfShip;

                    for( int m = 1; i+m < board.size() && board[i+m][j]=='X'; ++m )
                    {
                        //traversedPoints.insert( std::pair<int,int>(i+m,j) );
                        board[i+m][j] = 'Y';
                    }

                    for( int n = 1; j+n < board[i].size() && board[i][j+n]=='X'; ++n )
                    {
                        //traversedPoints.insert( std::pair<int,int>(i,j+n) );
                        board[i][j+n] = 'Y';
                    }

                }

            }
        }

        return numberOfShip;
    }
};
