class NumMatrix {
public:
    NumMatrix(vector<vector<int>> matrix) {
        
        if( matrix.empty())
            return;
        
        int length = matrix.size();
        int width = matrix[0].size();
        
        vector<int> blank;
        blank.assign( width, 0 );
        m.assign( length, blank);
        
        for( int i = 0; i < length; ++i )
        {
            for( int j = 0; j < width; ++j )
                m[i][j] = matrix[i][j] + ((i==0)?0:m[i-1][j]) + ((j==0)?0:m[i][j-1]) - ((i==0||j==0)?0:m[i-1][j-1]);
        }
    }
    vector<vector<int>> m;
        
    int sumRegion(int row1, int col1, int row2, int col2) {
        if( m.empty() || m[0].empty() )
            return 0;
        
        return m[row2][col2] - ((row1==0)?0:m[row1-1][col2]) - ((col1==0)?0:m[row2][col1-1]) + ((row1==0||col1==0)?0:m[row1-1][col1-1]);
    }
    
    void printM()
    {
        for( int i = 0; i < m.size(); ++i )
        {
            for( int j = 0; j < m[0].size(); ++j)
                cout << " " << m[i][j] << " ";
            cout << "\n";
        }
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */