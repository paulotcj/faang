// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/


Solution sol = new();
int result;
int[] arr = { 7, 1, 5, 3, 6, 4 };


result = sol.MaxProfit_2(arr);

Console.WriteLine($"Maximum Profit: {result}");
arr = new int[] { 7,6,4,3,1};

result = sol.MaxProfit_2(arr);
Console.WriteLine($"Maximum Profit: {result}");


public class Solution
{

    public int MaxProfit_2(int[] prices)
    {
        if (prices == null || prices.Length == 0) { return 0; }

        int min = prices[0];
        int max = prices[0];
        int diff = 0;

        for (int i = 0; i < prices.Length; i++)
        {
            if (prices[i] < min)
            {
                min = prices[i];
                max = min;
            }
            else 
            {
                max = Math.Max(max, prices[i]);
                diff = Math.Max(diff, max - min);
            }
        }

        return diff;
    }


    public int MaxProfit(int[] prices)
    {
        if (prices == null || prices.Length == 0) { return 0; }

        int[] responseArr = new int[prices.Length];
        int response;
        int currPrice;

        //--------------        
        int diff = -prices[0];
        for (int i = 1; i < prices.Length; i++)
        {
            response = responseArr[i - 1];
            currPrice = prices[i];
            responseArr[i] = Math.Max(response, currPrice + diff);
            diff = Math.Max(diff, -prices[i]);
        }

        return responseArr[prices.Length - 1];
    }
}