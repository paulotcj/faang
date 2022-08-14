// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

Solution sol = new();

string date1;
string date2;
int result = 0;


//Console.WriteLine("---------------------------------------");
//date1 = "2019-06-29";
//date2 = "2019-06-30";
//result = sol.DaysBetweenDates2(date1, date2);
//Console.WriteLine($"Days between dates {date2} and {date1} is : {result}");

Console.WriteLine("---------------------------------------");
date1 = "2020-01-15";
date2 = "2019-12-31";
result = sol.DaysBetweenDates2(date1, date2);
Console.WriteLine($"Days between dates {date2} and {date1} is : {result}");






public class Solution
{

    public int DaysBetweenDates2(string date1, string date2)
    {
        int d1 = CountSinceEpoch(date1);
        int d2 = CountSinceEpoch(date2);
        int days = d1 - d2;

        //-------------

        //int d3 = CountSinceEpoch2(date1);
        //int d4 = CountSinceEpoch2(date2);
        //int days_B = d3 - d4;



        days = Math.Abs(days);
        return days;
    }




    public int CountSinceEpoch(string date)
    {
        int[] monthDays = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

        string[] dateSplit = date.Split("-");

        int year    = int.Parse(dateSplit[0]);
        int month   = int.Parse(dateSplit[1]);
        int day     = int.Parse(dateSplit[2]);


        //Add days in the year, considering leap years
        //  note: we are only counting past years, not necessarily this year
        for (int i = 1971; i < year; i++)
        {
            if (IsALeapYear(i)) { day += 366; }
            else { day += 365; }
        }

        for (int i = 0; i < month; i++)
        {
            day += monthDays[i];
        }


        if (IsALeapYear(year) == true && month > 2) { day += 1; }


        return day;

    }

    //public int CountSinceEpoch(String date)
    //{

    //    int[] monthDays = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
    //    string[] dateSplit = date.Split("-");

    //    int year = Int32.Parse(dateSplit[0]);
    //    int month = Int32.Parse(dateSplit[1]);
    //    int day = Int32.Parse(dateSplit[2]);

    //    for (int i = 1971; i < year; i++)
    //    {
    //        day += IsALeapYear(i) ? 366 : 365;
    //    }
    //    for (int i = 1; i < month; i++)
    //    {
    //        if (IsALeapYear(year) && i == 2)
    //        {
    //            day += 1;
    //        }
    //        day += monthDays[i];
    //    }
    //    return day;
    //}

    public bool IsALeapYear(int year)
    {
        return ( (year % 4)     == 0 && //is year div by 4 but not by 100
                 (year % 100)   != 0) || 
                 (year % 400)    == 0;
    }

    //----------------------------------------------------

    public int DaysBetweenDates3(string date1 , string  date2)
    {
        DateTime d1 = DateTime.ParseExact(date1, "yyyy-MM-dd", null);
        DateTime d2 = DateTime.ParseExact(date2, "yyyy-MM-dd", null);

        int days = (int)(d2 - d1).TotalDays;
        days = Math.Abs(days);
        return days;
    }

    public int DaysBetweenDates(string date1, string date2)
    {
        var d1 = DateTime.ParseExact(date1, "yyyy-MM-dd", null);
        var d2 = DateTime.ParseExact(date2, "yyyy-MM-dd", null);
        return Math.Abs((int)(d2 - d1).TotalDays);
    }
}