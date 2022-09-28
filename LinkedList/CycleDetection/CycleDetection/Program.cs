#nullable disable
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int[] arr = { 8, 7, 6, 5, 4, 3, 2, 1 };

ListNode head = LinkedListActions.CreateNewList(arr);
LinkedListActions.SetCycleAtValue(head, 3);

Solution sol = new();
var result = sol.DetectCycle(head);


var result2 = sol.DetectCycle2(head);

















Console.ReadKey();

public class Solution
{
    //Floyd's 
    public ListNode DetectCycle(ListNode head)
    {
        if (head == null) return null;

        ListNode tortoise = head, hare = head;

        //-------
        do
        {
            if (tortoise == null || tortoise.next == null ||
                hare == null || hare.next == null || hare.next.next == null)
            { return null; }
            tortoise = tortoise.next;
            hare = hare.next.next;

            //if (tortoise == hare) { break; }
        } while (hare != tortoise);
        //-------

        //-------
        ListNode p1 = head, p2 = tortoise;
        while (p1 != p2)
        {
            p1 = p1.next;
            p2 = p2.next;
        }
        //-------

        return p2;
    }

    public ListNode DetectCycle2(ListNode head)
    {
        if (head == null) return null;
        HashSet<ListNode>  hashset = new();
        ListNode temp = head;

        while (hashset.Contains(temp) == false )
        { 
            hashset.Add(temp);
            if (temp.next == null) { return null; }
            temp = temp.next;
        }

        return temp;


    }
}


public static class LinkedListActions
{
    public static ListNode CreateNewList(int[] arr)
    {
        if (arr.Length == 0) return null;
        ListNode head = new (arr[0]);

        ListNode prev, temp = head;

        for (int i = 1; i < arr.Length; i++)
        {
            prev = temp;
            temp = new(arr[i]);
            prev.next = temp;
        }


        return head;
    }

    public static void SetCycleAtValue(ListNode node, int value)
    {
        if (node == null) { return; }
        ListNode targetLoop = null, last = null;

        while (node != null)
        {
            last = node;
            if (node.val == value) { targetLoop = node; }

            node = node.next;

        }

        last.next = targetLoop;

    }
}




//public class ListNode2
//{
//    public int val = 0;
//    public ListNode next;
//    public ListNode(int val, ListNode next = null)
//    {
//        this.val = val;
//        this.next = next;
//    }
//}

  public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int x) {
          val = x;
          next = null;
      }
  }


