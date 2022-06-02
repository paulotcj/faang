// See https://aka.ms/new-console-template for more information
using System.Text;

Console.WriteLine("Hello, World!");

string string1 = "ab#z";
string string2 = "az#z";

bool result1 = TypedOutStrings.BruteForce(string1, string2);

Console.WriteLine($"Are these two string comparatively equal? {result1}");

string1 = "ab#z";
string2 = "azxxx####z";

bool result2 = TypedOutStrings.BruteForce(string1, string2);

Console.WriteLine($"Are these two string comparatively equal? {result2}");


public static class TypedOutStrings
{
    private static string BuildString(string str)
    {
        StringBuilder sb = new();
        int backspaceCount = 0;

        for (int i = str.Length-1; i >= 0 ; i--)
        {
            if (str[i].CompareTo('#') == 0)
            { backspaceCount++; }
            else
            {
                if (backspaceCount > 0) { backspaceCount--; continue; }
                sb.Append(str[i]);
            }
        }

        return sb.ToString();
    }



    public static bool BruteForce(string str1, string str2)
    {
        string finalStr1 = BuildString(str1);
        string finalStr2 = BuildString(str2);

        if (finalStr1.CompareTo(finalStr2) != 0) { return false; }
        return true;

    }
}