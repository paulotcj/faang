// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


Solution sol = new();

int[][] boxes = { new int[] {1,3 }, new int[] { 2, 2 } , new int[] { 3, 1 } };

for (int i = 0; i < boxes.Length ; i++ )
{
    Console.WriteLine($"Number of Boxes: {boxes[i][0]} - with {boxes[i][1]} items inside");
}

sol.MaximumUnits(boxTypes: null , truckSize : 4);




public class Solution
{
    public int MaximumUnits(int[][] boxTypes, int truckSize)
    {
        return 0;
    }
}