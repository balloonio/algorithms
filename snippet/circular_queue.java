// 如何实现队列
// 我们需要知道队列的入队操作是只在队尾进行的，相对的出队操作是只在队头进行的，所以需要两个变量front与rear分别来指向队头与队尾
// 由于是循环队列，我们在增加元素时，如果此时 rear = array.length - 1 ，rear 需要更新为 0；同理，在元素出队时，如果 front = array.length - 1, front 需要更新为 0. 对此，我们可以通过对数组容量取模来更新。

public class CircularQueue {
    
    int[] circularArray;
    int front;
    int rear;
    int size;
    public CircularQueue(int n) {
        // initialize your data structure here
        
        this.circularArray = new int[n];
        front = 0;
        rear = 0;
        size = 0;
    }
    /**
     * @return:  return true if the array is full
     */
    public boolean isFull() {
        // write your code here 
        return size == circularArray.length;
    }

    /**
     * @return: return true if there is no element in the array
     */
    public boolean isEmpty() {
        // write your code here
        return size == 0;
    }

    /**
     * @param element: the element given to be added
     * @return: nothing
     */
    public void enqueue(int element) {
        // write your code here
        if (isFull()) {
            throw new RuntimeException("Queue is already full");
        }
        rear = (front + size) % circularArray.length;
        circularArray[rear] = element;
        size += 1;
    }

    /**
     * @return: pop an element from the queue
     */
    public int dequeue() {
        // write your code here
        if (isEmpty()) {
            throw new RuntimeException("Queue is already empty");
        }
        int ele = circularArray[front];
        front = (front + 1) % circularArray.length;
        size -= 1;
        return ele;
    }
}