// See https://aka.ms/new-console-template for more information
using System.Text;


Console.WriteLine("Brute Force");
string string1;
string string2;
bool result;

//----------------
string1 = "ab#z";
string2 = "az#z";
result = TypedOutStrings.BruteForce(string1, string2);

Console.WriteLine($"Strings: {string1} , {string2}");
Console.WriteLine($"Are these two string comparatively equal? {result}");

//----------------
string1 = "ab#z";
string2 = "azxxx####z";
result = TypedOutStrings.BruteForce(string1, string2);

Console.WriteLine($"Strings: {string1} , {string2}");
Console.WriteLine($"Are these two string comparatively equal? {result}");

//########################################################################################
Console.WriteLine($"-------------------------------------------------");
Console.WriteLine("Optimized");

//----------------
string1 = "ab#z";
string2 = "az#z";
result = TypedOutStrings.Optimized(string1, string2);

Console.WriteLine($"Strings: {string1} , {string2}");
Console.WriteLine($"Are these two string comparatively equal? {result}");


//----------------
string1 = "ab#z";
string2 = "azxxx####z";
result = TypedOutStrings.Optimized(string1, string2);

Console.WriteLine($"Strings: {string1} , {string2}");
Console.WriteLine($"Are these two string comparatively equal? {result}");


//----------------
string1 = "ab##";
string2 = "c#d#";
result = TypedOutStrings.Optimized(string1, string2);

Console.WriteLine($"Strings: {string1} , {string2}");
Console.WriteLine($"Are these two string comparatively equal? {result}");



public static class TypedOutStrings
{
    public static bool Optimized(string str1, string str2)
    {
        int str1Ptr = str1.Length - 1;
        int str2Ptr = str2.Length - 1;

        while (str1Ptr >= 0 || str2Ptr >= 0)
        {
            char? a = GetNextValidChar(str1, ref str1Ptr);
            char? b = GetNextValidChar(str2, ref str2Ptr);

            if (a != b) { return false; }

            str1Ptr--; 
            str2Ptr--;

        }
        return true;
    }

    public static char? GetNextValidChar(string str, ref int index)
    {
        int backspaceCount = 0;
        for (; index >= 0; index--)
        {
            if (str[index].CompareTo('#') == 0) { backspaceCount++; }
            else
            {
                if (backspaceCount > 0) { backspaceCount--; continue; }
                
                return str[index];
            }
        }
        return null;
        
    }

    //--------------------------
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