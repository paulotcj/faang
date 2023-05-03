// See https://aka.ms/new-console-template for more information
using System.Text.RegularExpressions;

Console.WriteLine("Hello, World!");
string str = "A man, a plan, a canal: Panama";
str = "aabcdxcbaa";
Solution solution = new();
bool result = false;


str = "aabccbaa";
result = solution.IsPalindrome_Reverse(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdcbaa";
result = solution.IsPalindrome_Reverse(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdxcbaa";
result = solution.IsPalindrome_Reverse(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: false");



Console.WriteLine("-----------------------------------------------");


str = "aabccbaa";
result = solution.IsPalindrome_Outside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdcbaa";
result = solution.IsPalindrome_Outside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdxcbaa";
result = solution.IsPalindrome_Outside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: false");



Console.WriteLine("-----------------------------------------------");
str = "aabccbaa";
result = solution.IsPalindrome_Inside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdcbaa";
result = solution.IsPalindrome_Inside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: true");

str = "aabcdxcbaa";
result = solution.IsPalindrome_Inside(str);
Console.WriteLine($"Is {str} Palindrome: {result} - expected: false");


Console.WriteLine("-----------------------------------------------");


str = "aba";
result = solution.AlmostPalindrome(str);
Console.WriteLine($"Is {str} almost a palindrome: {result} - expected: true");

str = "abca";
result = solution.AlmostPalindrome(str);
Console.WriteLine($"Is {str} almost a palindrome: {result} - expected: true");

str = "abc";
result = solution.AlmostPalindrome(str);
Console.WriteLine($"Is {str} almost a palindrome: {result} - expected: false");


public class Solution
{

    //------------------------------
    public bool AlmostPalindrome(string str)
    {
        str = System.Text.RegularExpressions.Regex.Replace(str, "[^A-Za-z0-9]", "");//.ToLower();

        int left = 0;
        int right = str.Length - 1;

        while(left < right)
        {
            if (str[left] != str[right])
            {
                return (
                           SubPalindrome(str, left + 1, right) || 
                           SubPalindrome(str, left, right - 1)
                        );
            }

            left++;
            right--;
        }


        return true;
    }

    public bool SubPalindrome(string str, int left, int right) //calculates the palindrome but without the overhead and set up
    {
        while ( left < right)
        {
            if (str[left] != str[right])
            {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }


    //------------------------------



    public bool IsPalindrome_Inside(string str)
    {
        str = System.Text.RegularExpressions.Regex.Replace(str, "[^A-Za-z0-9]", "").ToLower();

        int left = str.Length / 2; //we don't need to round (floor) this value in C#
        int right = left;

        if ((str.Length % 2) == 0) { left--; }

        while(left >= 0 && right < str.Length)
        {
            if (str[left] != str[right]) { return false; }

            left--;
            right++;
        }




        return true;

    }


    public bool IsPalindrome_Outside(string str)
    {
        str = System.Text.RegularExpressions.Regex.Replace(str, "[^A-Za-z0-9]", "").ToLower();

        int left = 0;
        for (int right = str.Length - 1; right >= 0; )
        {
            if (str[left] != str[right]) { return false; }

            right--;
            left++;
        }

        return true;
    }


    public bool IsPalindrome_Reverse(string str)
    {

        str = System.Text.RegularExpressions.Regex.Replace(str, "[^A-Za-z0-9]", "").ToLower();

        //--------------------
        // reverse string
        char[] charStr = str.ToCharArray();
        int j = 0;
        for (int i = str.Length-1; i >= 0; i--)
        {
            charStr[j++] = str[i];
        }
        //--------------------

        return String.Compare(str, new String(charStr)) == 0 ? true : false;


    }
}