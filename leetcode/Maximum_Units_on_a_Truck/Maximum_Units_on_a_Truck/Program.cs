//https://leetcode.com/problems/maximum-units-on-a-truck/
Console.WriteLine("Hello, World!");


Solution sol = new();

int[][] boxes = { new int[] { 3, 1 }, new int[] {1,3 }, new int[] { 2, 2 } ,  };


//int[][] boxes = { new int[] { 3, 1 }, new int[] { 1, 3 }, new int[] { 2, 2 }, new int[] { 2, 4 } };

int result = sol.MaximumUnits(boxTypes: boxes, truckSize : 4);

Console.WriteLine($"Result: {result}");

Console.WriteLine("---------------------------------------");

int[][] boxes2 = { new int[] { 3, 1 }, new int[] { 1, 3 }, new int[] { 2, 2 }, };
result = sol.MaximumUnits2(boxTypes: boxes2, truckSize: 4);
Console.WriteLine($"Result: {result}");


public class Solution
{

    public int MaximumUnits2(int[][] boxTypes, int truckSize) 
    {
        //Array.Sort(boxTypes, comparison: (a,b) => { return a[1] - b[1]; }); //array sorted from smallest to biggest
        Array.Sort(boxTypes, comparison: (a, b) => { return b[1] - a[1]; }); //array sorted from biggest to smallest

        int totalBoxes = 0;
        int totalUnits = 0;
        int availableSpaceForBoxes = truckSize;

        int numBoxes;
        int numUnits;

        for (int i = 0; i < boxTypes.Length ; i++ )
        {
            numBoxes = boxTypes[i][0];
            numUnits = boxTypes[i][1];

            availableSpaceForBoxes = truckSize - totalBoxes;

            totalUnits += numBoxes * Math.Min(numBoxes, availableSpaceForBoxes);

            totalBoxes += numBoxes;

            if (totalBoxes >= truckSize) { break; }


        }

        return totalUnits;
    }


    public int MaximumUnits(int[][] boxTypes, int truckSize)
    {
        //----
        // let's sort, shall we?
                   //int[][] array                           //e.g.: 3-1 = 2  or  2-3 = -1
        Array.Sort(array : boxTypes, comparison: (a, b) => 
            { 
                //Console.WriteLine($"b[1] : {b[1]} - a[1]: {a[1]} = {b[1] - a[1]} ");   
                return b[1] - a[1]; 
            });
        //-----

        int totalBoxes = 0;
        int totalUnits = 0;
        int availableSpaceForBoxes;

        int numBoxes;
        int numItems;


        for (int i = 0 ; i < boxTypes.Length; i++)
        {
            numBoxes = boxTypes[i][0];
            numItems = boxTypes[i][1];

            availableSpaceForBoxes = truckSize - totalBoxes;

            totalUnits += numItems * Math.Min(numBoxes, availableSpaceForBoxes);
            totalBoxes += numBoxes;
            if (totalBoxes >= truckSize) { break; }

        }

        return totalUnits;
    }
}