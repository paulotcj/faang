// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//https://leetcode.com/problems/sum-of-subarray-ranges/

int[] arr;
long response = 0;
Solution sol = new();

//---------------------------------------
arr = new int[] { 1, 2, 3 };
response = sol.SubArrayRanges2(arr);
Console.WriteLine($"Response: {response} - expected : 4");


arr = new int[] { 1, 3, 3 };
response = sol.SubArrayRanges2(arr);
Console.WriteLine($"Response: {response} - expected : 4");


arr = new int[] { 4, -2, -3, 4, 1 };
response = sol.SubArrayRanges2(arr);
Console.WriteLine($"Response: {response} - expected : 59");

public class Solution
{

    public long SubArrayRanges2(int[] nums)
    {
        long sum = 0;
        int max = 0;
        int min = 0;
        int curr = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            min = nums[i];
            max = nums[i];

            for (int j = i+1; j < nums.Length ; j++ ) 
            { 
                curr = nums[j];
                if (curr > max) { max = curr; }
                else if (curr < min) { min = curr; }

                sum = sum + (max - min);
            }

        }
        //---------

        return sum;
    }


    public long SubArrayRanges(int[] nums)
    {
        long sum = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            var min = nums[i];
            var max = nums[i];


            for (int k = i; k < nums.Length; k++)
            {
                var cur = nums[k];

                if (cur > max) max = cur;
                if (cur < min) min = cur;

                sum += (max - min);
            }
        }

        return sum;
    }
}