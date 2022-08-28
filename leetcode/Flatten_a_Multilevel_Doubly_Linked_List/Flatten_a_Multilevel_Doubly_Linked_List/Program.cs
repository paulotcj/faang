// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography;
using System.Xml.Linq;

Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Solution sol = new();
Node? head;


Console.WriteLine("----------------------------------");

int?[] arr = { 1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10, null, null, 11, 12 };
head = sol.CreateList(arr: arr);

Console.WriteLine($"head: {sol.Print(head)}");

head = sol.Flatten3(head);

Console.WriteLine($"head: {sol.Print(head)} - Expected: 1,2,3,7,8,11,12,9,10,4,5,6");



public class Solution
{
    public Node Flatten2(Node head)
    {
        if (head == null) { return null; }
        List<Node> list = new();
        list = ListNodeHeadAndTail(head);
        return list[0];
    }

    public List<Node> ListNodeHeadAndTail(Node head)
    {
        Node curr = head, next = null;
        Node tail = head;
        List<Node> list = new();
        while (curr != null)
        {
            if (curr.next == null) { tail = curr; }
            next = curr.next;
            //---
            if (curr.child != null)
            {
                List<Node> childList = ListNodeHeadAndTail(curr.child);
                curr.next = childList[0];
                childList[0].prev = curr;

                if (next != null)
                {
                    next.prev = childList[1];
                    childList[1].next = next;
                }
                curr.child = null;
            }
            
            //---
            curr = curr.next;
        }
        list.Add(head);
        list.Add(tail);
        return list;

    }

    public Node Flatten3(Node head)
    {
        Stack<Node> stack = new();
        Node previous = new();
        //---
        stack.Push(head);
        while (stack.Count > 0)
        {
            Node current = stack.Pop();
            //---
            //lets adjust the relationship
            previous.next = current;
            current.prev = previous;
            previous = current;
            //---
            //stack push
            if (current.next != null) { stack.Push(current.next); }
            if (current.child != null){ stack.Push(current.child); }
            //---
            current.child = null;
        }
        //---
        head.prev = null;
        return head;

    }

    public Node Flatten(Node head)
    {
        if (head == null) { return null;}

        Stack<Node> stack = new();
        Node tempHead = head;
        Node previous = new();

        //---
        stack.Push(head);
        while (stack.Count > 0)
        {
            Node current = stack.Pop();

            //lets adjust the relationship
            previous.next = current;
            current.prev = previous;
            previous = current;

            //---
            //stack push
            if (current.next != null)
            {
                stack.Push(current.next);
            }
            if (current.child != null)
            {
                stack.Push(current.child);
            }
            //---
            current.child = null; //loop
        }
        //---
        tempHead.prev = null; //fixing the list


        return tempHead;
    }


    public string Print(Node head)
    {
        string returnStr = "";
        while(head != null)
        {
            returnStr += head.val + ",";
            head = head.next;
        }
        return returnStr;
    }

    public Node? CreateList(int?[] arr)
    {
        List<Node> list = new();

        //-------
        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] != null)
            {
                Node temp = new();
                temp.val = arr[i] ?? int.MaxValue;
                list.Add(temp);
            }
            else { list.Add(null); }
            
        }
        //-------
        Node prev = null, curr = null, next = null;
        for (int i = 0; i < list.Count; i++)
        {
            if (list[i] == null)
            {
                prev = null;
                curr = null;
                continue;
            }
            curr = list[i];
            curr.prev = prev;
            if (prev != null)
            {
                prev.next = curr;
            }
            prev = curr;
            
        }
        //-------
        int idx_header = 0, stepCount = 0;
        for (int i = 0; i < list.Count; i++)
        {
            if (list[i] == null)
            {
                stepCount = -1;
                while (list[i] == null && i < list.Count)
                {
                    stepCount++;
                    i++;
                }
                if (list[i] != null && i < list.Count)
                {
                    list[idx_header + stepCount].child = list[i];
                    idx_header = i;
                }
            }

        }


        return list.Count > 0 ? list[0]  : null;

    }
}

// Definition for a Node.
public class Node
{
    public int val;
    public Node prev;
    public Node next;
    public Node child;
}