class LRUCache {
public:
    LRUCache(int capacity) {
        capacity_ = capacity;    
        head_ = NULL;
        tail_ = NULL;
    }

    int capacity_;
    int size_;
    Node* head_;
    Node* tail_;
    unordered_map<int,int> keyToNode_;

    struct Node
    {
        Node* prev;
        Node* next;
        int value;
    }

    Node* getNode( int key )
    {
        unordered_map<int,Node*>::iterator it;
        if( (it = keyToNode_.find(key)) != keyToNode_.end() )
        {
            return (it->second);
        }
        else
        {
            return NULL;
        }
    }
    
    int get(int key) {
        Node* np = getNode(key);
        if( np!= NULL )
        {
            // update frequency
            
            return np->value;
        }
        else
        {
            return -1;
        }
    }
    
    void put(int key, int value) {
        Node* np = getNode(key);
        if( np != NULL )
        {
            //already in double link list, move to head
            Node* np= (it->second);
            Node* temp = np->next;
            np->next = np->prev;
            np->prev = temp;

            head_ = 
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */