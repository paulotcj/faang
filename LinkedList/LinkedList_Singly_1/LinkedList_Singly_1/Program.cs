Console.WriteLine("Hello, World!");

LinkedListActions lnkactions = new();

ListNode? head = lnkactions.StartNewList(5);

lnkactions.PrintLinkedList(head);


head = lnkactions.ReverseList(head);

Console.WriteLine($"List was reversed, checking the results");

lnkactions.PrintLinkedList(head);

//----------------------------------------------------------------

public class LinkedListActions
{
    public ListNode? ReverseList(ListNode node)
    {
        ListNode? curr = null;
        ListNode? prev = null;
        ListNode? next = null;

        for (curr = node ; curr != null ; )
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
        ListNode? head = new(1, null);
        ListNode? current = head;
        ListNode? prev = null;

        for (int i = 2; i <= numElements; i++)
        {
            prev = current;
            current = new(i, null);
            prev.next = current;
        }

        return head;
    }


    public void PrintLinkedList(ListNode? node)
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
    public ListNode? next;
    
    public ListNode(int val, ListNode? next = null) 
    {
        this.val = val;
        this.next = next;
    }
}

