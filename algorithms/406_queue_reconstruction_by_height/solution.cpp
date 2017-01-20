class Solution {
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        
        vector< pair<int,int> > queue;
        // Sort the list based on people's height, from tall to short, front of the queue to back
        std::sort( people.begin(), people.end(), TallerOrFronter() );
        
        // Insert the person into the queue at the index = k
        for( vector<pair<int, int>>::iterator i = people.begin(); i != people.end(); ++i )
        {
            // If the entire current queue is in the front of the new guy, add to the end
            if( queue.size() == people[i-people.begin()].second )
                queue.push_back( people[i-people.begin()] );
            // Else, insert to index = k
            else
                queue.insert( queue.begin()+people[i-people.begin()].second, people[i-people.begin()] );
        }
        
        return queue;
    }
    
    struct TallerOrFronter
    {
        bool operator()( const pair<int,int>& p1, const pair<int,int>& p2 )
        {
            if( p1.first == p2.first )
                return p1.second < p2.second;
            else
                return p1.first > p2.first;
        }
    };
    
};
