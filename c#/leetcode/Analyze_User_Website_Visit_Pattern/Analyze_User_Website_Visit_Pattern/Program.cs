// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//https://leetcode.com/problems/analyze-user-website-visit-pattern/

string[] username;
int[] timestamp;
string[] website;
IList<string> response;

Solution sol = new();

Console.WriteLine("-------------------------------------------");

username = new string[] { "joe","joe","joe","james","james","james","james","mary","mary","mary" };
timestamp = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
website = new string[] { "home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career" };


response = sol.MostVisitedPattern(username: username , timestamp : timestamp , website: website);

Console.WriteLine($"Response: {sol.PrintList(response)} - expected: [home,about,career]");



public class Solution
{


    public IList<string> MostVisitedPattern(string[] username, int[] timestamp, string[] website)
    {

        string result = string.Empty;
        //basic idea is to iterate thru all the patterns and idenfity their score
        //if u get the max score then return the result othwerise which ever score is lex small then return that pattern

        //as a first step, lets map users to website & timestamp for iteration

        Dictionary<string, List<TimeWeb>> userTimeweb_Dic = SetUpData(username, timestamp, website);

        //----------------------------

        Dictionary<string, HashSet<string>> patternUser_dict = new ();
        int maxScore = 0;

        //now we need to iterate thru all the users and identify patterns and score them


        foreach (string user in userTimeweb_Dic.Keys)
        {
            //what if the given input time is not sorted

            List<TimeWeb> sortedTimeWebObjs = userTimeweb_Dic[user]
                    .OrderBy(o => o.time)
                    .ToList();


            //now identify the pattern
            for (int i = 0; i < sortedTimeWebObjs.Count() - 2; i++) 
            {
                for (int j = i + 1; j < sortedTimeWebObjs.Count() - 1; j++)
                {
                    for (int k = j + 1; k < sortedTimeWebObjs.Count(); k++)
                    {
                        //we are printing the pattern here. We need to save it somewhere to identify
                        //the scores of that pattern and adding it to our dict to identify our score
                        //
                        // We are adding a sliding pattern - suppose the web site list is: a,b,c,d,e
                        //  the first entry in the dictionary will be: 'a:b:c' , the second: 'b:c:d'
                        //  and the third: 'c:d:e'
                        string pattern =    sortedTimeWebObjs[i].web + ":" + 
                                            sortedTimeWebObjs[j].web + ":" +
                                            sortedTimeWebObjs[k].web;

                        //----

                        //now we use the pattern as a key in the dictionary and we try to match users that
                        // have the same pattern in their history
                        if (patternUser_dict.ContainsKey(pattern) == false) //new pattern entry
                        {
                            HashSet<string> userHashSet = new();
                            userHashSet.Add(user);
                            patternUser_dict.Add(pattern, userHashSet);
                        }
                        else //pattern exists, add user to pattern
                        {
                            patternUser_dict[pattern].Add(user);
                        }

                        //----

                        //is this the most visited pattern?
                        if (patternUser_dict[pattern].Count() > maxScore) //so far it is, add this as a response
                        {
                            //new result found
                            maxScore = patternUser_dict[pattern].Count();
                            result = pattern;
                        }
                        else if (patternUser_dict[pattern].Count() == maxScore) //same score
                        {
                            //same result for two diff patterns. The first pattern (result) precedes the second in the sort order 
                            result = result.CompareTo(pattern) <= 0 ? result : pattern;
                        }
                    } //for (int k = j + 1; k < sortedTimeWebObjs.Count(); k++)
                } //for (int j = i + 1; j < sortedTimeWebObjs.Count() - 1; j++)
            } //for (int i = 0; i < sortedTimeWebObjs.Count() - 2; i++)


        } //foreach (string user in userTimeweb_Dic.Keys)

        return result.Split(':').ToList();
    }



    private Dictionary<string, List<TimeWeb>> SetUpData(string[] username, int[] timestamp, string[] website)
    {
        Dictionary<string, List<TimeWeb>> userTimeweb_Dic = new();

        for (int i = 0; i < username.Length; i++)
        {
            string user = username[i];
            int time = timestamp[i];
            string web = website[i];
            TimeWeb tw = new TimeWeb(time, web);
            //----

            if (userTimeweb_Dic.ContainsKey(user) == false) //user doesnt exist in the dictionary
            {
                List<TimeWeb> newList = new();
                newList.Add(tw);
                userTimeweb_Dic.Add(user, newList);
            }
            else
            {
                userTimeweb_Dic[user].Add(tw); //add a new (TimeWeb) entry for the user - this contains the website visited and the time
            }
        }

        return userTimeweb_Dic;
    }


    //--------------------------------------------------------------------------
    //########################################
    //########################################
    //########################################
    //########################################
    //########################################
    //########################################
    //########################################
    //--------------------------------------------------------------------------

    public IList<string> MostVisitedPattern_LINQ(string[] username, int[] timestamp, string[] website)
    {

        var dataObj = Enumerable.
            Range(0, username.Length)
            .Select(
                x => new { User = username[x], Time = timestamp[x], Site = website[x] }
            );

        var joinObj = from item1 in dataObj
                   from item2 in dataObj
                   from item3 in dataObj
                   where 
                        item1.User == item2.User && 
                        item2.User == item3.User && 
                        item1.Time < item2.Time && 
                        item2.Time < item3.Time
                   group 
                        item1.User by new { Site1 = item1.Site, Site2 = item2.Site, Site3 = item3.Site } into siteGroups
                   select new { siteGroups.Key, Count = siteGroups.Distinct().Count() };

        var returnObj = joinObj.
            OrderByDescending(x => x.Count)
            .ThenBy(x => x.Key.Site1)
            .ThenBy(x => x.Key.Site2)
            .ThenBy(x => x.Key.Site3).
            Select(
                x => new List<string> { x.Key.Site1, x.Key.Site2, x.Key.Site3 }
            )
            .First();

        return returnObj;
    }

    //------------------------------------------------

    public string PrintList(IList<string> list)
    {
        string returnObj = "[";

        foreach (string str in list)
        {
            returnObj += str + ",";
        }
        returnObj += "]";

        return returnObj;

    }
}



public class TimeWeb
{
    public int time;
    public string web;

    public TimeWeb(int time, string web)
    {
        this.time = time;
        this.web = web;

    }
}