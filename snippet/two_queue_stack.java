// 算法步骤
// 两个队列实现一个栈，其实并没有什么优雅的办法。就看大家怎么去写这个东西了。

// 构造的时候，初始化两个队列，queue1，queue2。queue1主要用来存储，queue2则主要用来帮助queue1弹出元素以及访问栈顶。
// push：将元素推入queue1当中。
// pop：注意要弹出的元素在queue1末端，故将queue1中元素弹出，并直接推入queue2，当queue1只剩一个元素时，把它pop出来，并作为结果。而后交换两个队列。
// top：类似pop，不过不扔掉queue1中最后一个元素，而是把它也推入queue2当中。
// isEmpty：判断queue1是否为空即可。

public class Stack {
    public Queue<Integer> queue1 = new LinkedList<Integer>();
    public Queue<Integer> queue2 = new LinkedList<Integer>();
    
    // 将queue1中元素移入queue2,留下最后一个。
    public void moveItems() {
        while (queue1.size() != 1) {
            queue2.offer(queue1.poll());
        }
    }
    
    // 交换两个队列
    public void swapQueues() {
        Queue<Integer> temp = queue1;
        queue1 = queue2;
        queue2 = temp;
    }

    public void push(int x) {
        queue1.offer(x);
    }

    public void pop() {
        moveItems();
        queue1.poll();
        swapQueues();
    }

    public int top() {
        moveItems();
        int item = queue1.poll();
        swapQueues();
        queue1.offer(item);
        return item;
    }

    public boolean isEmpty() {
        return queue1.isEmpty();
    }
}