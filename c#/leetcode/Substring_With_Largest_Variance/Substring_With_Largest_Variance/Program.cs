// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/substring-with-largest-variance/

Solution sol = new();
string input;
int result = 0;


////Console.WriteLine("----------------------------------");
//input = "aababbb";
//result = sol.LargestVariance(input);
//Console.WriteLine($"Result: {result} - expected: 3");

//Console.WriteLine("----------------------------------");
//input = "abcde";
//result = sol.LargestVariance(input);
//Console.WriteLine($"Result: {result} - expected: 0");

//Console.WriteLine("----------------------------------");
//input = "lripaa";
//result = sol.LargestVariance(input);
//Console.WriteLine($"Result: {result} - expected: 1");


//Console.WriteLine("----------------------------------");
//input = "nuqjhcmkyossynftzkpjlfbwkxrufzzmttoxb";
//result = sol.LargestVariance(input);
//Console.WriteLine($"Result: {result} - expected: 2");

Console.WriteLine("----------------------------------");
input = "ukabckdek";
result = sol.LargestVariance(input);
Console.WriteLine($"Result: {result} - expected: 2");



//input = "abcde";

public class Solution
{
    public int LargestVariance_Test(string s)
    {
        HashSet<char> unique = new(s);
        int largestVariance = 0;

        for (int i = 0; i < unique.Count ; i++ )
        {
            char a = unique.ElementAt(i);
            //---

            for (int j = 0; j < unique.Count; j++)
            {
                char b = unique.ElementAt(j);
                if (a == b) { continue; }

                largestVariance = Math.Max(largestVariance, FindVariance(a, b, s));

            }

            //---
        }
        

        return largestVariance;
    }



    // Kadane's algorithm
    // Time complexity: O(C^2*N)
    // Space complexity: O(C)
    // where C is number of unique characters in S
    public int LargestVariance(string s)
    {
        HashSet<char> unique = new(s);
        int max = 0;

        foreach (char a in unique)
        {
            foreach (char b in unique)
            {
                if (a == b)
                    continue;
                if (a == 'k' && b == 'u')
                {
                    //a = 'k';
                }

                max = Math.Max(max, FindVariance_Test(a, b , s));

            }
        }

        return max;


    }


    public int FindVariance_Test(char a, char b, string strInput)
    {
        int max = 0;
        int countA = 0;
        bool hasB = false;

        foreach (char curr in strInput)
        {
            if (curr == a)
            {
                countA++;
            }
            else if (curr == b)
            {
                if (countA == 0)
                { hasB = false; } 
                else
                {
                    countA--;
                    hasB = true;
                }
            }

            max = Math.Max(max, hasB ? countA : countA - 1);
        }

        return max;
    }





    public int FindVariance(char a, char b , string strInput)
    {
        int max = 0;
        int res = 0;
        bool hasB = false;

        foreach (char c in strInput)
        {
            if (c == a)
            {
                res++;
            }
            else if (c == b)
            {
                if (res == 0)
                    hasB = false;
                else
                {
                    res--;
                    hasB = true;
                }
            }

            max = Math.Max(max, hasB ? res : res - 1);
        }

        return max;
    }




}