// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/meeting-rooms-ii/

Solution sol = new();
int response = 0;
int[][] intervals;

Console.WriteLine("------------------------------------------");
intervals = new int[][] { new int[] { 0, 30 }, new int[] { 5, 10 }, new int[] { 15, 20 } };
response = sol.MinMeetingRooms_Test1(intervals);
Console.WriteLine($"Result: {response} - Expected: 2");


Console.WriteLine("------------------------------------------");
intervals = new int[][] { new int[] { 7, 10 }, new int[] { 2, 4 } };
response = sol.MinMeetingRooms_Test1(intervals);
Console.WriteLine($"Result: {response} - Expected: 1");


public class Solution
{
    public int MinMeetingRooms_Test1(int[][] intervals)
    {
        int[] starts = new int[intervals.Length];
        int[] ends = new int[intervals.Length];
        //-----------------
        for (int i = 0; i < intervals.Length; i++)
        {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        //-----------------
        Array.Sort(starts);
        Array.Sort(ends);
        //-----------------

        //we had the arrays sorted, and now we start looking at the start times and the end times, and from there we can figure out the situation
        //starts: 0, ends: 10  - earliest start is at 0 and earliest end is at 10, we need a room (total:1)
        //starts: 5, ends: 10  - the second earliest start is at 5, and still the earliest end is at 10, we need another room (total: 2)
        //starts: 15, ends: 10 - the third start is at 15 and the earliest end is at 10, so our start is past the end time of a previous
        //                        meeting, therefore we don't need a new room (total: 2)
        //
        //Second Example:
        //starts: 2, ends: 4   - The earliest meeting start at 2, and the earliest end is at 4, we will need a room (total:1)
        //starts: 7, ends: 4   - The second earliest meeting starts at 7, but is past the first end, so we don't need an extra room (total: 1)
        int minRoomsRequired = 0;
        int j = 0;
        for (int i = 0; i < intervals.Length; i++) 
        {
            if (starts[i] < ends[j])
            { 
                minRoomsRequired++;
            }
            else 
            {
                j++;
            }
        }
        //-----------------

        return minRoomsRequired;
    }


    public int MinMeetingRooms(int[][] intervals)
    {
        int[] starts = new int[intervals.Length];
        int[] ends = new int[intervals.Length];

        //--------
        for (int i = 0; i < intervals.Length; i++)
        {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        //--------
        Array.Sort(starts);
        Array.Sort(ends);
        //--------

        int minRoomsReq = 0;

        //we had the arrays sorted, and now we start looking at the start times and the end times, and from there we can figure out the situation
        //starts: 0, ends: 10  - earliest start is at 0 and earliest end is at 10, we need a room (total:1)
        //starts: 5, ends: 10  - the second earliest start is at 5, and still the earliest end is at 10, we need another room (total: 2)
        //starts: 15, ends: 10 - the third start is at 15 and the earliest end is at 10, so our start is past the end time of a previous
        //                        meeting, therefore we don't need a new room (total: 2)
        //
        //Second Example:
        //starts: 2, ends: 4   - The earliest meeting start at 2, and the earliest end is at 4, we will need a room (total:1)
        //starts: 7, ends: 4   - The second earliest meeting starts at 7, but is past the first end, so we don't need an extra room (total: 1)
        int j = 0;
        for(int i = 0; i < intervals.Length ; i++)
        {
            //Console.WriteLine($"    starts: {starts[i]}, ends:{ends[j]}");
            if (starts[i] < ends[j])
            {
                minRoomsReq++;
            }
            else
            {
                j++;
            }
        }
        return minRoomsReq;

    }
}