class Solution {

    unordered_map<int,int> map;
    vector<string> findAll( n )
    {
        defineFlipMap();

        vector<string> result;

        for( int i = 0; i < n )
    }

    void defineFlipMap()
    {
        map[0]=0;
        map[1]=1;
        map[6]=9;
        map[8]=8;
        map[9]=6;
    }
}