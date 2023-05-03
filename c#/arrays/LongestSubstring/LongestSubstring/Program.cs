// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//const string str = "abccabb";

const string str = "abcbdaac";

Solution solution = new();

int result = solution.LengthOfLongestSubstring(str);

Console.WriteLine($"Longest substring: {result}");

public class Solution
{
    public int LengthOfLongestSubstring(string str)
    {
        if (str.Length <= 1) { return str.Length; }

        Dictionary<char, int> seen = new();
        int left = 0, longest = 0;


        //----------
        for (int right = 0; right < str.Length; right ++) //we are moving the right pointer continuously to the right
        {
            char curr = str[right];

            //main logic: check whether we have this character in the dictionary, and also important to remember
            //  we dont clear the dictionary when we move the window, so dictionary entries stay in there regardless
            //
            // check if we have 'curr' character in the dictionary
            // If we DON'T have it: 
            //       - add this 'curr' character to the dictionary using the 'right' pointer as a indicator of its location
            // ELSE (meaning if we do have it):
            //       - check if this index is within our 'window' frame
            //         if it is we need to move the left pointer to the position where this characters was last seen plus 1
            //         and that's because the 'right' pointer is sitting right at where this 'repeated' character is
            //       - update the position of the last occurent of the current character with the right pointer, as it's sitting
            //          right there
            //
            // THEN get the max: either the current longest substring sequence, or the current substring within our window
            if (seen.ContainsKey(curr) == false)
            { seen.Add(curr, right); }
            else
            {
                int idxPrevSeenCurrChar = seen[curr];

                if (left <= idxPrevSeenCurrChar) //is this repeadted char within the window frame? because if it's not it doesn't matter
                {
                    left = idxPrevSeenCurrChar + 1; // move the left pointer to the position where this characters was last seen plus 1
                                                    //because the 'right' pointer is sitting right at where this 'repeated' character is
                }

                seen[curr] = right; //update its last position
            }

            longest = Math.Max(longest, ( right - left + 1 ) ); //which one is bigger? longest or the current substring being investigated?

            
        }
        //----------
        return longest;
    }


    public int LengthOfLongestSubstring_Suboptimal(string str)
    {
        if (str.Length <= 1) { return str.Length; }

        int longest = 0;

        for (int left = 0; left < str.Length; left++) //for every loop we move the left pointer one step to the right
        {
            Dictionary<char, int> seenChars = new();
            int currentLenght = 0;

            for (int right = left; right < str.Length; right++) 
            {
                char currentChar = str[right];

                if (seenChars.ContainsKey(currentChar) == false)
                {
                    currentLenght++;
                    seenChars.Add(currentChar, right);
                    longest = Math.Max(longest, currentLenght);
                }
                else 
                {
                    break; //in situations like this we are bailing out before the end of the array, identifying individual substrings
                }
            }

        }

        return longest;

    }
}