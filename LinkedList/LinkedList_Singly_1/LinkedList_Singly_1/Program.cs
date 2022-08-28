Console.WriteLine("Hello, World!");

LinkedListActions lnkactions = new();

Console.WriteLine("---------------------------------");
ListNode head = lnkactions.StartNewList(5);
lnkactions.PrintLinkedList(head);
head = lnkactions.ReverseList(head);
Console.WriteLine($"List was reversed, checking the results");
lnkactions.PrintLinkedList(head);


//Console.WriteLine("---------------------------------");
//head = lnkactions.StartNewList(5);
//lnkactions.PrintLinkedList(head);
//head = lnkactions.ReverseBetween(head, 2, 4);
//lnkactions.PrintLinkedList(head);


//Console.WriteLine("---------------------------------");
//head = lnkactions.StartNewList(1);
//lnkactions.PrintLinkedList(head);
//head = lnkactions.ReverseBetween(head, 1, 1);
//lnkactions.PrintLinkedList(head);


Console.WriteLine("---------------------------------");

ListNode temp = new(5, null);
head = new(3, temp);



head = lnkactions.ReverseBetween(head, 1, 2);
lnkactions.PrintLinkedList(head);



//----------------------------------------------------------------

public class LinkedListActions
{
    public ListNode ReverseBetween(ListNode head, int left, int right)
    {
        ListNode leftNode_Prev = head, leftNode = head;
        int steps;
        for (steps = 1; steps < left; steps++)
        {
            leftNode_Prev = leftNode;
            leftNode = leftNode.next;
        }
        //------------
        ListNode rightNode_Next = leftNode.next, rightNode = leftNode;
        //------------
        ListNode prev = null, curr = null, next = null;

        for (curr = leftNode; curr!= null; steps++)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            //---
            if (steps == right)
            {
                rightNode = curr;
                rightNode_Next = next;
                break;
            }
            //---
            curr = next;

        }
        leftNode_Prev.next = rightNode;
        leftNode.next = rightNode_Next;

        if (left > 1) { return head; }

        return curr;
    }



    public ListNode ReverseList(ListNode head)
    {
        ListNode curr = null;
        ListNode prev = null;
        ListNode next = null;

        for (curr = head ; curr != null ; )
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            //---
            curr = next; //loop
        }

        return prev;


    }
       


    public ListNode StartNewList(int numElements)
    {
        //create list
        ListNode head = new(1, null);
        ListNode current = head;
        ListNode prev = null;

        for (int i = 2; i <= numElements; i++)
        {
            prev = current;
            current = new(i, null);
            prev.next = current;
        }

        return head;
    }


    public void PrintLinkedList(ListNode node)
    {
        Console.Write($"\nNodes -> ");
        while (node != null)
        {
            Console.Write($"{node.val},");
            node = node.next;
        }
        Console.WriteLine();
    }
}



public class ListNode
{
    public int val;
    public ListNode next;
    
    public ListNode(int val, ListNode next = null) 
    {
        this.val = val;
        this.next = next;
    }
}

