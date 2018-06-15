class LFUCache {
public:
    struct Data;
    LFUCache(int capacity) {
        this->capacity = capacity;
        size = 0;
    }

    int capacity;
    int size;
    typedef list<Data>::iterator DI; // data iterator
    typedef unordered_map<int,DI>::iterator KI; // key iterator
    list<Data> dataStore;
    unordered_map<int,DI> keyToData;
    unordered_map<int,DI> freqToFirstData;

    struct Data {
        int key;
        int value;
        int freq;

        Data( int k, int v, int f )
        : key(k)
        , value(v)
        , freq(f)
        {}
    };
    
    int get(int key) 
    {
        if( size <= 0 )
            return -1;

        DI data;
        KI iter = keyToData.find(key);
        if( iter != keyToData.end() )
        {
            // found data, update data store list position, update frequency map
            data = iter->second;
            updateFrequency( data );
            printDataStore();
            return data->value;
        }
        else
        {
            printDataStore();
            return -1;
        }
    }

    void put(int key, int value) {
        if( capacity <= 0 )
            return;

        DI data;
        KI iter = keyToData.find(key);
        if( iter != keyToData.end() )
        {
            // update data store list position, update frequency map
            data = iter->second;
            data->value = value;
            updateFrequency(data);
        }
        else
        {
            // evict the last data in list if need, push the new data to the end
            evictIfNeed();
            insertNewData(key,value);
        }
        printDataStore();
    }

    void updateFrequency( DI data )
    {
        // remove from current frequency bucket if it is the frontmost element
        KI iter = freqToFirstData.find(data->freq);
        if( iter != freqToFirstData.end() && iter->second == data )
        {
            DI next = data;
            ++next;
            if( next != dataStore.end() && next->freq == data->freq )
                freqToFirstData[data->freq] = next;
            else
                freqToFirstData.erase(data->freq);
        }
        data->freq ++;
        // insert to the correct position
        iter = freqToFirstData.find(data->freq);
        if( iter != freqToFirstData.end() )
        {
            // if there is data with the same frequency, insert at the front of them
            dataStore.splice( iter->second, dataStore, data );
        }
        else if( (iter=freqToFirstData.find(data->freq-1)) != freqToFirstData.end() )
        {
            // otherwise, insert at the front of the frontmost data with frequency 1 less than self if any
            dataStore.splice( iter->second, dataStore, data );
        }
        freqToFirstData[data->freq] = data;
    }

    void insertNewData( int key, int value)
    {
        // find the frontmost data from frequency map
        DI data;
        KI iter = freqToFirstData.find(1);
        if( iter != freqToFirstData.end() )
        {
            // create new data, insert it at the front of the frontmost node with same frequency
            data = dataStore.insert( iter->second, Data(key,value,1) );
        }
        else
        {
            dataStore.push_back(Data(key,value,1));
            data = dataStore.end();
            --data;
        }

        // update frequency map
        freqToFirstData[1] = data;
        keyToData[key] = data;
        ++size;
    }

    void evictIfNeed()
    {
        if(size < capacity)
            return;

        DI data = dataStore.end();
        --data;
        keyToData.erase( data ->key );

        KI iter = freqToFirstData.find( data->freq );
        if( iter != freqToFirstData.end() && iter->second == data )
        {
            // data in frequency map and data is the frontmost data in list among data with same frequency
            freqToFirstData.erase( data->freq );
        }
        dataStore.pop_back();
        --size;
    }

    void printDataStore()
    {
        cout << "\nPrinting dataStore: from head to tail";
        for( list<Data>::iterator data = dataStore.begin(); data != dataStore.end(); ++data )
        {
            cout << "(k:" << data->key << ", v:" << data->value << ", f:" << data->freq << ")->";
        }
        cout << "\nfrom tail to head";
        for( list<Data>::reverse_iterator data = dataStore.rbegin(); data != dataStore.rend(); ++data )
        {
            cout << "(k:" << data->key << ", v:" << data->value << ", f:" << data->freq << ")->";
        }
        cout << "\nPrinting frequency map";
        for( KI it = freqToFirstData.begin(); it != freqToFirstData.end(); ++it )
        {
            cout << "key:" << it->first << "->(k:" << it->second->key << ", v:" << it->second->value << ", f:" << it->second->freq << "), ";
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

/* int main()
{
    LFUCache lfu(2);
    lfu.put(1,1);
    lfu.put(2,2);
    lfu.get(1);
    lfu.put(3,3);
    lfu.get(2);
    lfu.get(3);
    lfu.put(4,4);
    lfu.get(1);
    lfu.get(3);
    lfu.get(4);
}

Printing dataStore: from head to tail(k:1, v:1, f:1)->
from tail to head(k:1, v:1, f:1)->
Printing frequency mapkey:1->(k:1, v:1, f:1), 
Printing dataStore: from head to tail(k:2, v:2, f:1)->(k:1, v:1, f:1)->
from tail to head(k:1, v:1, f:1)->(k:2, v:2, f:1)->
Printing frequency mapkey:1->(k:2, v:2, f:1), 
Printing dataStore: from head to tail(k:2, v:2, f:1)->(k:1, v:1, f:2)->
from tail to head(k:1, v:1, f:2)->(k:2, v:2, f:1)->
Printing frequency mapkey:2->(k:1, v:1, f:2), key:1->(k:2, v:2, f:1), 
Printing dataStore: from head to tail(k:3, v:3, f:1)->(k:2, v:2, f:1)->
from tail to head(k:2, v:2, f:1)->(k:3, v:3, f:1)->
Printing frequency mapkey:1->(k:3, v:3, f:1), 
Printing dataStore: from head to tail(k:3, v:3, f:1)->(k:2, v:2, f:2)->
from tail to head(k:2, v:2, f:2)->(k:3, v:3, f:1)->
Printing frequency mapkey:2->(k:2, v:2, f:2), key:1->(k:3, v:3, f:1), 
Printing dataStore: from head to tail(k:3, v:3, f:2)->(k:3, v:3, f:2)->(k:2, v:2, f:2)->
from tail to head(k:2, v:2, f:2)->(k:3, v:3, f:2)->(k:3, v:3, f:2)->
Printing frequency mapkey:2->(k:3, v:3, f:2), 
Printing dataStore: from head to tail(k:3, v:3, f:2)->(k:3, v:3, f:2)->(k:4, v:4, f:1)->
from tail to head(k:4, v:4, f:1)->(k:3, v:3, f:2)->(k:3, v:3, f:2)->
Printing frequency mapkey:1->(k:4, v:4, f:1), key:2->(k:3, v:3, f:2), 
Printing dataStore: from head to tail(k:3, v:3, f:2)->(k:3, v:3, f:2)->(k:4, v:4, f:1)->
from tail to head(k:4, v:4, f:1)->(k:3, v:3, f:2)->(k:3, v:3, f:2)->
Printing frequency mapkey:1->(k:4, v:4, f:1), key:2->(k:3, v:3, f:2), 
Printing dataStore: from head to tail(k:3, v:3, f:3)->(k:3, v:3, f:2)->(k:4, v:4, f:1)->
from tail to head(k:4, v:4, f:1)->(k:3, v:3, f:2)->(k:3, v:3, f:3)->
Printing frequency mapkey:3->(k:3, v:3, f:3), key:1->(k:4, v:4, f:1), key:2->(k:3, v:3, f:2), 
Printing dataStore: from head to tail(k:3, v:3, f:3)->(k:4, v:4, f:2)->(k:3, v:3, f:2)->(k:4, v:4, f:2)->
from tail to head(k:4, v:4, f:2)->(k:3, v:3, f:2)->(k:4, v:4, f:2)->(k:3, v:3, f:3)->
Printing frequency mapkey:3->(k:3, v:3, f:3), key:2->(k:4, v:4, f:2),  */