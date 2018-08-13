
class LRUCache {
public:

    struct Node;
    typedef shared_ptr<Node> NP;

    LRUCache(int capacity) {
        cout << "capacity" << capacity;
        capacity_ = capacity;
        size_ = 0;
        head_ = NULL;
        tail_ = NULL;
    }
    ~LRUCache()
    {}

    int capacity_;
    int size_;
    NP head_;
    NP tail_;
    unordered_map<int,NP> keyToNode_;

    struct Node
    {
        Node( int k, int v )
        : prev( NULL )
        , next( NULL )
        , key(k)
        , value(v)
        {}

        NP prev;
        NP next;
        int key;
        int value;
    };

    NP getNode( int key )
    {
        unordered_map<int,NP>::iterator it;
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
        NP np = getNode(key);
        if( np )
        {
            touchNode(np);
            printList();
            return np->value;
        }
        else
        {
            return -1;
        }
    }

    void put(int key, int value) {

        if( capacity_ <= 0 )
            return;

        NP np = getNode(key);
        if( np )
        {
            // already in double link list, update value, move to head, no addition needed, no removal needed
            np->value=value;
            touchNode(np);
        }
        else
        {
            // not in double link list, create node, insert in front, remove from tail if need
            np = make_shared<Node>( key, value );
            insertNode( np );
            removeIfNeed();
        }
        printList();
    }

    void insertNode( NP nodeToInsert )
    {
        if( !size_ )
            tail_ = nodeToInsert;
        if( head_ )
            head_->prev = nodeToInsert;

        nodeToInsert->prev = NULL;
        nodeToInsert->next = head_;
        head_ = nodeToInsert;

        keyToNode_[ nodeToInsert->key ] = nodeToInsert;
        ++size_;
        return;
    }

    void removeIfNeed()
    {
        if( size_ > capacity_ )
        {
            keyToNode_.erase( tail_->key );
            tail_ = tail_->prev;
            
            // tail should never be null here
            tail_->next = NULL;
        }
    }

    void touchNode( NP nodeToTouch )
    {
        if( size_ == 1 || nodeToTouch == head_)
            return;

        // if node is not head
        if( nodeToTouch->prev != NULL )
        {
            nodeToTouch->prev->next = nodeToTouch->next;
        }

        // if node is not tail
        if( nodeToTouch->next != NULL )
        {
            nodeToTouch->next->prev = nodeToTouch->prev;
        }

        if( nodeToTouch == tail_ )
        {
            tail_ = nodeToTouch->prev;
        }

        if( nodeToTouch != head_ )
        {
            // head should never be null here
            head_->prev = nodeToTouch;
            nodeToTouch->next = head_;
            nodeToTouch->prev = NULL;
            head_ = nodeToTouch;
        }
    }

    void printList()
    {
        cout << "\nHead->Tail:\n";
        NP np = head_;
        while( np )
        {
            cout << np->key << "->";
            np = np->next;
        }
        cout << "\nTail->Head:\n";
        np = tail_;
        while( np )
        {
            cout << np->key << "->";
            np = np->prev;
        }
    }
};