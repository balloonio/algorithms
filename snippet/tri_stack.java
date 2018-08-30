// 算法描述
// 这道题的本质是把数组索引当作地址，用链表来实现栈。数组buffer中的每一个元素，并不能单单是简单的int类型，而是一个链表中的节点，它包含值value，栈中向栈底方向的之前元素索引prev，向栈顶方向的后来元素索引next。
// 在该三栈数据结构中，要记录三个栈顶指针stackPointer，也就是三个栈顶所在的数组索引，通过这三个栈顶节点，能够用prev找到整串栈。
// 此外还要用indexUsed记录整个数组中的所用的索引数。其实也就是下一次push的时候，向数组的indexUsed位置存储。

// 具体操作：

// 构造：要初始化stackPointer为3个-1,表示没有;indexUsed=0;buffer为一个长度为三倍栈大小的数组。
// push：要把新结点new在buffer[indexUsed]，同时修改该栈的stackPointer，indexUsed自增。注意修改当前栈顶结点prev和之前栈顶结点的next索引。
// peek：只需要返回buffer中对应的stackPointer即可。
// isEmpty：只需判断stackPointer是否为-1。
// pop：pop的操作较为复杂，因为有三个栈，所以栈顶不一定在数组尾端，pop掉栈顶之后，数组中可能存在空洞。而这个空洞又很难push入元素。所以，解决方法是，当要pop的元素不在数组尾端（即indexUsed-1）时，交换这两个元素。不过一定要注意，交换的时候，要注意修改这两个元素之前、之后结点的prev和next指针，使得链表仍然是正确的，事实上这就是结点中next的作用——为了找到之后结点并修改它的prev。在交换时，一种很特殊的情况是栈顶节点刚好是数组尾端元素的后继节点，这时需要做特殊处理。在交换完成后，就可以删掉数组尾端元素，并修改相应的stackPointer、indexUsed和新栈顶的next。

public class ThreeStacks {
    public int stackSize;
    public int indexUsed;
    public int[] stackPointer;
    public StackNode[] buffer;

    public ThreeStacks(int size) {
        // do intialization if necessary
        stackSize = size;
        stackPointer = new int[3];
        for (int i = 0; i < 3; ++i)
            stackPointer[i] = -1;
        indexUsed = 0;
        buffer = new StackNode[stackSize * 3];
    }

    public void push(int stackNum, int value) {
        // Write your code here
        // Push value into stackNum stack
        int lastIndex = stackPointer[stackNum];
        stackPointer[stackNum] = indexUsed;
        indexUsed++;
        buffer[stackPointer[stackNum]] = new StackNode(lastIndex, value, -1);
        if (lastIndex != -1) {
            buffer[lastIndex].next = stackPointer[stackNum];
        }
    }

    public int pop(int stackNum) {
        // Write your code here
        // Pop and return the top element from stackNum stack
        int value = buffer[stackPointer[stackNum]].value;
        int lastIndex = stackPointer[stackNum];
        if (lastIndex != indexUsed - 1)
            swap(lastIndex, indexUsed - 1, stackNum);

        stackPointer[stackNum] = buffer[stackPointer[stackNum]].prev;
        if (stackPointer[stackNum] != -1)
            buffer[stackPointer[stackNum]].next = -1;

        buffer[indexUsed-1] = null;
        indexUsed --;
        return value;
    }

    public int peek(int stackNum) {
        // Write your code here
        // Return the top element
        return buffer[stackPointer[stackNum]].value;
    }

    public boolean isEmpty(int stackNum) {
        // Write your code here
        return stackPointer[stackNum] == -1;
    }

    public void swap(int lastIndex, int topIndex, int stackNum) {
        if (buffer[lastIndex].prev == topIndex) {
            int tmp = buffer[lastIndex].value;
            buffer[lastIndex].value = buffer[topIndex].value;
            buffer[topIndex].value = tmp;
            int tp = buffer[topIndex].prev;
            if (tp != -1) {
                buffer[tp].next = lastIndex;
            }
            buffer[lastIndex].prev = tp;
            buffer[lastIndex].next = topIndex;
            buffer[topIndex].prev = lastIndex;
            buffer[topIndex].next = -1;
            stackPointer[stackNum] = topIndex;
            return;
        }

        int lp = buffer[lastIndex].prev;
        if (lp != -1)
            buffer[lp].next = topIndex;

        int tp = buffer[topIndex].prev;
        if (tp != -1)
            buffer[tp].next = lastIndex;

        int tn = buffer[topIndex].next;
        if (tn != -1)
            buffer[tn].prev = lastIndex;
        else {
            for (int i = 0; i < 3; ++i)
                if (stackPointer[i] == topIndex)
                    stackPointer[i] = lastIndex;
        }

        StackNode tmp = buffer[lastIndex];
        buffer[lastIndex] = buffer[topIndex];
        buffer[topIndex] = tmp;
        stackPointer[stackNum] = topIndex;
    }
}

class StackNode {
    public int prev, next;
    public int value;
    public StackNode(int p, int v, int n) {
        value = v;
        prev = p;
        next = n;
    }
}