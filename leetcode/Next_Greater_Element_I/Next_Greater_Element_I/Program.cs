// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/next-greater-element-i/

int[] arr1;// = { 4, 1, 2 };
int[] arr2;// = { 1, 3, 4, 2 };
int[] response;

Solution sol = new();

Console.WriteLine("--------------------");
arr1 = new int[] { 4, 1, 2 };
arr2 = new int[] { 1, 3, 4, 2 };

response = sol.NextGreaterElement(arr1, arr2);
Console.WriteLine($"Response: [{sol.ArrayToString(response)}]  - Expected: [-1,3,-1]");
Console.WriteLine("--------------------");



arr1 = new int[] { 2, 4 };
arr2 = new int[] { 1, 2, 3, 4 };

response = sol.NextGreaterElement(arr1, arr2);
Console.WriteLine($"Response: [{sol.ArrayToString(response)}]  - Expected: [3,-1]");
Console.WriteLine("--------------------");



public class Solution
{
    public int[] NextGreaterElement2(int[] a, int[] b)
    {
        if (a == null || b == null || a.Length == 0 || b.Length == 0 || a.Length > b.Length) { return new int[0]; }

        int[] response = new int[a.Length];
        int curr = 0;
        for (int i = 0; i < a.Length; i++)
        {
            curr = a[i];
            int matchingIndex = FindMatchingIndex(b, curr);
            if (matchingIndex == -1) { response[i] = -1; }
            else
            {

            }


        }
    }

    //------------------------------------------

    public int ArraySeekGreaterElement(int[] arr, int idxWhereToStart, int valueToSeek)
    { 


        return -1;
    }

    //------------------------------------------

public int FindMatchingIndex(int[] arr, int value)
    {
        int index;
        for (int i = 0; i < arr.Length; i ++) 
        {
            if (arr[i] == value) { return i; }
        }
        return -1;
    }




    public int[] NextGreaterElement(int[] a, int[] b)
    {
        if (a == null || b == null || a.Length > b.Length)
            return new int[0];

        var s = new Stack<int>();
        var o = new int[a.Length];
        var d = new Dictionary<int, int>();

        for (int i = 0; i < a.Length; i++)
        {
            d[a[i]] = i;
            o[i] = -1;
        }

        for (int i = 0; i < b.Length; i++)
        {
            if (d.Count == 0)
                break;

            var cur = b[i];

            while (s.Count > 0 && cur > s.Peek())
            {
                var prev = s.Pop();
                if (d.ContainsKey(prev))
                {
                    o[d[prev]] = cur;
                    d.Remove(prev);
                }
            }

            s.Push(cur);
        }

        return o;
    }
    //-----------------------------------------------
    public string ArrayToString(int[] arr)
    {
        string output = "";
        for (int i = 0; i < arr.Length ; i++ )
        {
            output += arr[i] + ",";
        }

        return output;
    }
}