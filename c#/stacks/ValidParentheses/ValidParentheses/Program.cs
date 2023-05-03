// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

bool result;
string str;

str = "()[]{}";
result = ValidParentheses.IsValid(str);
Console.WriteLine($"Parentheses analisis for string {str} is : {result}");



str = "[";
result = ValidParentheses.IsValid(str);
Console.WriteLine($"Parentheses analisis for string {str} is : {result}");



str = "]";
result = ValidParentheses.IsValid(str);
Console.WriteLine($"Parentheses analisis for string {str} is : {result}");

public static class ValidParentheses
{
    public static bool IsValid(string s)
    {
        Dictionary<char, char> stackPush = new() { { '(', ')' }, { '[', ']' }, { '{', '}' } };
        Dictionary<char, char> stackPop = new()  { { ')', '(' }, { ']', '[' }, { '}', '{' } };

        Stack<char> localStack = new ();

        for (int i = 0; i < s.Length; i++)
        {
            char current = s[i];
            if (stackPush.ContainsKey(current) == true) { localStack.Push(current); }
            else if (stackPop.ContainsKey(current) == true)
            {
                if (localStack.Count == 0) { return false; }
                char pop = localStack.Pop();
                if (pop != stackPop[current]) { return false; }
            }
        }
        if (localStack.Count > 0) { return false; }

        return true;

    }
}