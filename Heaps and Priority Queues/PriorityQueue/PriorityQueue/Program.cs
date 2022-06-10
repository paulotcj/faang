// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

PriorityQueue pq = new();

pq.Push(15);
pq.Push(12);
pq.Push(50);
pq.Push(7);
pq.Push(40);
pq.Push(22);

pq.Push(51);
pq.Push(47);
pq.Push(30);
pq.Push(25);
pq.Push(63);
pq.Push(65);
pq.Push(67);
pq.Push(61);
pq.Push(62);
pq.Push(64);
pq.Push(1);

Console.WriteLine($"The following should print the results of the priority Queue.\nThe result should be an ordered list from higher to lower values.");
while (pq.IsEmpty() == false)
{
    Console.WriteLine(pq.Pop());
}




//-----------------------


public class PriorityQueue
{
    private List<int> _heap;
    private Func<int, int, bool> _comparator;

    public PriorityQueue(Func<int,int,bool> comparator = null)
    { 
        _comparator = comparator ?? ((x, y) => x > y);
        _heap = new();
    }

    public int Size() { return _heap.Count; }
    public int? Peek() { return _heap[0]; }
    public bool IsEmpty() { return _heap.Count == 0 ? true : false;  }
    
    //---
    private int ParentIdx(int childIdx) { return (int)Math.Floor(    (decimal)((childIdx - 1) / 2)    ); }
    private int LeftChildIdx(int parentIdx) { return parentIdx * 2 + 1; }
    private int RightChildIdx(int parentIdx) { return parentIdx * 2 + 2; }
    //---

    private void Swap(int idx_a , int idx_b)
    {
        int temp = _heap[idx_a];
        _heap[idx_a] = _heap[idx_b];
        _heap[idx_b] = temp;
    }

    private bool Compare(int idx_a, int idx_b)
    {
        return _comparator(_heap[idx_a], _heap[idx_b]);
    }

    public void Push(int value)
    {
        _heap.Add(value);
        SiftUp();

    }

    
    //siftUp swaps a node that is too large with its parent (thereby moving it up) until it is no larger than the node above it. 
    //The buildHeap function takes an array of unsorted items and moves them until it they all satisfy the heap property.
    private void SiftUp()
    {
        int nodeIdx = _heap.Count - 1;
        int parentIdx = ParentIdx(nodeIdx);

        //                      heap[nodeIdx] > heap[parentIdx]
        while (nodeIdx > 0 && Compare(nodeIdx, parentIdx) == true ) 
        { 
            Swap(nodeIdx, parentIdx);
            nodeIdx = parentIdx;
            parentIdx = ParentIdx(nodeIdx);
        }
    }

    // siftDown swaps a node that is too small with its largest child(thereby moving it down) until it is at least as large as both nodes below it.
    //
    // WTF? this is pure nonsense - revise!
    private void SiftDown()
    {
        int size = Size();
        
        int nodeIdx = 0;
        int leftChildIdx = LeftChildIdx(nodeIdx);
        int rightChildIdx = RightChildIdx(nodeIdx);

        // generally we are looking for the children of the node, starting at the root (index 0)
        //  we look down the tree/array and try to find the 'greatest' child, and once found
        //  it's then replaced parent <-> child, thus now the child is sitting on the parent's spot
        // Right at this spor we are truing to identify if we are within index bounds, and if any of the children
        //  of the current node is bigger
        while (                            // heap[A]     >  heap[B]
            (leftChildIdx  < size && Compare(leftChildIdx, nodeIdx)) == true ||
            (rightChildIdx < size && Compare(rightChildIdx, nodeIdx) == true )
        )
        {
            int greaterChildIdx;

            // which child is the greatest/biggest? left or right?
            //                                   heap[A]     >    heap[B]
            if (rightChildIdx < size && Compare(rightChildIdx, leftChildIdx) )
            { greaterChildIdx = rightChildIdx; }
            else { greaterChildIdx = leftChildIdx; }

            //found the bigger child, now swap with the parent
            Swap(greaterChildIdx, nodeIdx);
            nodeIdx = greaterChildIdx; //since we swapped, now we assume the position of the child and we will loop again checking its (possible) children

            //-------
            leftChildIdx = LeftChildIdx(nodeIdx);
            rightChildIdx = RightChildIdx(nodeIdx);

        }
    }

    public int Pop()
    {
        int size = Size();
        if (size > 1) { Swap(0, size - 1); }

        //pop
        int popVal = _heap[_heap.Count - 1];
        _heap.RemoveAt(_heap.Count - 1);

        SiftDown();

        return popVal;

    }




}