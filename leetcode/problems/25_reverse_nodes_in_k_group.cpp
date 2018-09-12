/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if( k == 0 || head == NULL )
            return head;
        
        int length = len( head );
        if( length >= k )
        {
            // need to reverse first k
            ListNode* oldHead = head;
            ListNode* firstNodeAfterK = getFirstNodeAfterK( head, k );
            head = reverseKNodes( head, k );
            oldHead->next = reverseKGroup( firstNodeAfterK, k );
        }
        
        return head;
    }
    
    int len( ListNode* head )
    {
        int index = 0;
        while( head != NULL )
        {
            head = head->next;
            ++index;
        }
        return index;
    }
    
    ListNode* reverseKNodes( ListNode* head, int k )
    {
        int reverted = 0;
        ListNode* prev = NULL;
        while( reverted != k )
        {
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
            ++reverted;
        }
        return prev;
    }
    
    ListNode* getFirstNodeAfterK( ListNode* head, int k )
    {
        ListNode* node = NULL;
        int index = 0;
        
        while( head != NULL )
        {
            head = head->next;
            ++index;
            
            if( index == k )
                return head;
        }
        
        return NULL;
    }
};