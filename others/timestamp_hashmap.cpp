/*
带expiration的hashmap
http://www.1point3acres.com/bbs/thread-402936-1-1.html
https://www.careercup.com/question?id=5689672300756992
Add a third dimension of time to a hashmap , so ur hashmap will look something 
like this - HashMap&lt;K, t, V&gt; where t is a float value. Implement the get 
and put methods to this map. The get method should be something like - map.get(K,t) 
which should give us the value. If t does not exists then map should return the 
closest t' such that t' is smaller than t. For example, if map contains (K,1,V1) 
and (K,2,V2) and the user does a get(k,1.5) then the output should be v1 as 1 is 
the next smallest number to 1.5
*/
typedef int Key;
typedef int Time;
typedef int Value;

class TimeHash
{
private:
    std::unordered_map<Key, std::map<Time, Value>> key2timeval_;
    typedef std::unordered_map<Key, std::map<Time, Value>>::iterator KIT;
    typedef std::map<Time, Value>::iterator TVIT;

public:
    Value get(Key k, Time t);
    bool put(Key k, Time t, Value v);
};

Value TimeHash::get(Key k, Time t)
{
    KIT iter = key2timeval_.find(k);
    if( iter == key2timeval_.end() )
    {
        // Key not in map
        return -1;
    }
    std::map<Time, Value>& timeval = iter->second;
    TVIT iter2 = timeval.find(t);
    if( iter2 != timeval.end() )
    {
        // timestamp exist
        return iter2->second;
    }
    // timestamp not exist, find the latest time before the time
    iter2 = timeval.lower_bound(t); // first item key >= k
    // what if no value has timestamp earlier than t?? what if timeval empty?? TBD
    if( iter2 != timeval.begin() )
    {
        --iter2;
    }
    return iter2->second;
}

bool TimeHash::put(Key k, Time t, Value v)
{
    KIT iter = key2timeval_.find(k);
    if( iter == key2timeval_.end() )
    {
        // Key not in map, create blank map for it
        key2timeval_[key] = std::map<Time, Value>();
    }
    std::map<Time, Value>& timeval = key2timeval_[key];
    timeval[t] = v;
}