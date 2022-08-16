// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

ListNode head;
int[] arr;
Solution sol = new();
int response = 0;

Console.WriteLine("------------------------------------------");
arr = new int[] { 5, 4, 2, 1 };
head = sol.CreateList(arr);

response = sol.PairSum2(head);
Console.WriteLine($"Response: {response} - expected: 6");

Console.WriteLine("------------------------------------------");


arr = new int[] { 4, 2, 2, 3 };
head = sol.CreateList(arr);

response = sol.PairSum2(head);
Console.WriteLine($"Response: {response} - expected: 7");




public class Solution
{

    public int PairSum2(ListNode head)
    {
        //we will trade-off some space complexity in order to reduce time complexity
        List<int> list = new();
        ListNode temp = head;
        
        while(temp != null)
        {
            list.Add(temp.val);
            temp = temp.next;
        }
        //---------------------------
        int max_i_range = list.Count / 2 - 1 ; //range: 0 <= i <= (n/2)-1

        int maxValue = 0;
        int curr = 0;
        int twinIndex = 0;
        int twin = 0;
        int twinsSum = 0;
        for (int i = 0; i <= max_i_range; i++)
        {
            curr = list[i];
            twinIndex = (list.Count - 1 - i); //twin index: (n - 1 - i)
            twin = list[twinIndex];
            twinsSum = curr + twin;

            maxValue = Math.Max(maxValue, twinsSum);

        }


        return maxValue;
    }


    public int PairSum(ListNode head)
    {
        // store the node vals in the list
        List<int> list = new List<int>();
        while (head != null)
        {
            list.Add(head.val);
            head = head.next;
        }
        // iterate from end and start of the list
        // reducing the window in every iteration
        int i = 0;
        int j = list.Count() - 1;
        int maxVal = Int32.MinValue;
        while (i < j)
        {
            if (maxVal < list[i] + list[j])
            { maxVal = list[i] + list[j]; }

            i++;
            j--;
        }
        return maxVal;
    }

    public ListNode CreateList(int[] arr)
    {
        ListNode head = null;
        ListNode temp = null;
        for (int i = arr.Length-1; i >=0; i--)
        {
            head = new(val: arr[i], next: temp);
            temp = head;
        }

        return head;
    }
}

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}