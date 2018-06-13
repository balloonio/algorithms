
class LRUCache {
public:

    struct Node;

    LRUCache(int capacity) {
        capacity_ = capacity;
        size_ = 0;
        head_ = NULL;
        tail_ = NULL;
    }
    ~LRUCache()
    {
        unordered_map<int,Node*>::iterator it;
        for( it = keyToNode_.begin(); it != keyToNode_.end(); ++it )
        {
            delete (it->second);
            keyToNode_.erase( it->first );
        }
    }

    int capacity_;
    int size_;
    Node* head_;
    Node* tail_;
    unordered_map<int,Node*> keyToNode_;

    struct Node
    {
        Node( int k, int v )
        : prev( NULL )
        , next( NULL )
        , key(k)
        , value(v)
        {}

        Node* prev;
        Node* next;
        int key;
        int value;
    };

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
        if( np )
        {
            touchNode(np);
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

        Node* np = getNode(key);
        if( np )
        {
            // already in double link list, move to head, no addition needed, no removal needed
            touchNode(np);
        }
        else
        {
            // not in double link list, create node, insert in front, remove from tail if need
            np = new Node( key, value );
            insertNode( np );
            removeIfNeed();
        }
    }

    void insertNode( Node* nodeToInsert )
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
            delete (tail_->next);
            tail_->next = NULL;
        }
    }

    void touchNode( Node* nodeToTouch )
    {
        if( size_ == 1 )
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
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

