// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/reorder-data-in-log-files/


Solution sol = new();
string[] logs;
string[] response;

Console.WriteLine("----------------------------------------------");

logs = new string[] { "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero" };
response = sol.ReorderLogFiles3_Test(logs);

Console.WriteLine($"Results:\n{sol.PrintSolution(response)} - Expected:\n" +
        $"[                         \n" +
        $"    [let1 art can],       \n" +
        $"    [let3 art zero],      \n" +
        $"    [let2 own kit dig],   \n" +
        $"    [dig1 8 1 5 1],       \n" +
        $"    [dig2 3 6]            \n" +
        $"]                         \n"
);



Console.WriteLine("----------------------------------------------");

logs = new string[] { "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo" };
response = sol.ReorderLogFiles3_Test(logs);

Console.WriteLine($"Results:\n{sol.PrintSolution(response)} - Expected:\n" +
        $"[                       \n" +
        $"    [g1 act car],       \n" +
        $"    [a8 act zoo],       \n" +
        $"    [ab1 off key dog],  \n" +
        $"    [a1 9 2 3 1],       \n" +
        $"    [zo4 4 7]           \n" +
        $"]                       \n" 
);

Console.WriteLine("----------------------------------------------");








public class Solution
{
    public string[] ReorderLogFiles3_Test(string[] logs)
    {
        List<string> digitLogs = new();
        List<string> letterLogs = new();
        List<string> responseObj;

        //--------------------
        // separate and identify them
        foreach (string str in logs)
        {
            if (str.Split(" ")[1].All(char.IsDigit) == true) //the result from split(" ")[0] is the log identifier, so by checking
            { digitLogs.Add(str); }                          //[1] we are checking the actual data after the identifier
            else
            { letterLogs.Add(str); }

        }
        //--------------------
        //Letter logs must be ordered
        //1 - by their content (i.e.: the data after the identifier)
        //2 - the content being the same, then by the identifier
        responseObj = letterLogs
            .OrderBy(
                x => x.Substring(startIndex: x.IndexOf(' ') + 1  )
            )
            .ThenBy(
                x => x.Substring(startIndex: 0 , length: x.IndexOf(' ') )
            )
            .ToList();
        //--------------------
        //Numbers log don't need to be ordered
        responseObj.AddRange(digitLogs);
        //--------------------
        return responseObj.ToArray();

    }


    public string[] ReorderLogFiles3(string[] logs)
    {
        var digitLogs = new List<string>();
        var letterLogs = new List<string>();

        foreach (string log in logs)
        {
            if (log.Split(" ")[1][0] >= '0' && log.Split(" ")[1][0] <= '9') 
            {                                                               
                digitLogs.Add(log);
            }
            else
            {
                letterLogs.Add(log);
            }
        }

        List<string> result = letterLogs
        .OrderBy(
            x => x.Substring(x.IndexOf(' ') + 1)
        )
        .ThenBy(
            x => x.Substring(0, x.IndexOf(' '))
        )
        .ToList();


        result.AddRange(digitLogs);
        return result.ToArray();
    }



    //------------------------
    //public string[] ReorderLogFiles2(string[] logs)
    //{
    //    List<string> digitLogs = new List<string>();
    //    List<string> letterLogs = new List<string>();


    //    foreach (var log in logs)
    //    {
    //        if (char.IsDigit(log.Split(' ')[1][0]))
    //            digitLogs.Add(log);
    //        else
    //            letterLogs.Add(log);
    //    }

    //    letterLogs.Sort((log1, log2) => {
    //        string word1 = log1.Substring(log1.IndexOf(" "));
    //        string word2 = log2.Substring(log2.IndexOf(" "));
    //        if (word1.Equals(word2))
    //            return log1.CompareTo(log2);
    //        else
    //            return word1.CompareTo(word2);
    //    });

    //    int index = 0;
    //    foreach (var log in letterLogs)
    //    {
    //        logs[index++] = log;
    //    }
    //    foreach (var log in digitLogs)
    //    {
    //        logs[index++] = log;
    //    }

    //    return logs;

    //}


    //-------------------------------

    public string[] ReorderLogFiles_Test1(string[] logs)
    {
        string[] returnObj = logs.
            Where(
                x => x.Split(" ")[1].All(char.IsDigit) == false //the first word is a identifier, this will always be a word, we want to
            )                                                   //select the next item (hence [1]) and check if it's only letters
            .OrderBy(
                x => x.Substring(startIndex: x.IndexOf(" ") + 1) //the first letter is the identifier, therefore we need to order by what comes next
            )
            .ThenBy(
                x => x.Substring(startIndex: 0, length: x.IndexOf(" ")) //case the content is the same, order by the identifier
            )
            .Union( //now we want the number logs
                logs
                .Where(
                    x => x.Split(" ")[1].All(char.IsDigit)  //get the first item after the identifier, is it all digits? if so that's what we want
                )                                           //the problem require us to keep the order of the number logs
            )
            .ToArray();

        return returnObj;
    }


    public string[] ReorderLogFiles(string[] logs)
    {
        if (logs.Length == 0) return logs;

        List<string> returnObj = logs.
            Where(
                x => x.Split(" ")[1].All(char.IsDigit) == false  //the first word is a identifier, this will always be a word, we want to
            )                                                    //select the next item (hence [1]) and check if it's only letters
            .OrderBy(
                x => x.Substring(x.IndexOf(" ") + 1) //the first letter is the identifier, therefore we need to order by what comes next
            )
            .ThenBy(
                x => x.Substring(0, x.IndexOf(" ")) //case the content is the same, order by the identifier
            )
            .Union( //now we want the number logs
                logs.
                Where(
                    x => x.Split(" ")[1].All(char.IsDigit) //get the first item after the identifier, is it all digits? if so that's what we want
                )                                          //the problem require us to keep the order of the number logs
            )
            .ToList();

        return returnObj.ToArray();
    }

    //---------------------------------------------

    public string PrintSolution(string[] str)
    {
        string response = "[\n";

        foreach (var a in str)
        {
            response += "    [" + a + "],\n";
        }

        response += "]\n";

        return response;
    }
}