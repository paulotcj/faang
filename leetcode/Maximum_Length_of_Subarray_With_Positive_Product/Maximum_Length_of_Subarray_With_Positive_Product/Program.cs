// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Solution sol = new();
int response;
int[] nums;



Console.WriteLine("--------------------------------------");
nums = new int[] { 9, 10, 1, 0, 19, 20, -28, 30, -12, 20, 11, -8, 7, 21, -26 };
//nums = new int[] { 19, 20, -28, 30, -12, 20, 11, -8, 7, 21, -26 };

response = sol.GetMaxLen(nums: nums);
Console.WriteLine($"Result: {response} - Expected: 11");

//Console.WriteLine("--------------------------------------");
//nums = new int[] { -16, 0, -5, 2, 2, -13, 11, 8 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 6");

//Console.WriteLine("--------------------------------------");
//nums = new int[] { 1, 2, 3, 5, -6, 4, 0, 10 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 4");

//Console.WriteLine("--------------------------------------");
//nums = new int[] { 1, -2, -3, 4 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 4");


//Console.WriteLine("--------------------------------------");
//nums = new int[] { -1, 2 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 1");

//Console.WriteLine("--------------------------------------");
//nums = new int[] { 0, 1, -2, -3, -4 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 3");


//Console.WriteLine("--------------------------------------");
//nums = new int[] { -1, -2, -3, 0, 1 };
//response = sol.GetMaxLen(nums: nums);
//Console.WriteLine($"Result: {response} - Expected: 2");

public class Solution
{

    public int GetMaxLen_Temp(int[] nums)
    {

        int result = 0;
        int pos = 0;
        int neg = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == 0) //0 will make the array useless, restart the search
            {
                pos = 0;
                neg = 0;
            }
            else if (nums[i] > 0)
            {
                pos++;
                neg = (neg == 0) ? 0 : neg + 1; //we only start counting negatives after the first neg
            }
            else //negative num
            {
                int tmp = pos;
                pos = (neg == 0) ? 0 : neg + 1;  //is this the first negative? if so positive is zero, otherwise it will be neg+1
                neg = tmp + 1;
            }
            result = Math.Max(pos, result);
        }

        return result;

    }



    public int GetMaxLen(int[] nums)
    {
        int result = 0;
        int pos = 0;
        int neg = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == 0) //0 will make the array useless, restart the search
            {
                pos = 0;
                neg = 0;
            }
            else if (nums[i] > 0)
            {
                pos++;
                neg = (neg == 0) ? 0 : neg + 1;
            }
            else
            {
                int tmp = pos;
                pos = (neg == 0) ? 0 : neg + 1;
                neg = tmp + 1;
            }
            result = Math.Max(pos, result);
        }

        return result;

    }
    //0 will make the array useless, restart the search
    //Console.WriteLine($"   i: {i},  neg: {negative},  pos: {positive},  prevPos: {prevPositive},  maxPosLen: {maxPosLen},  num:{num}");
}