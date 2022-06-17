// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int[] heights = { 4, 8, 1, 2, 3, 9 };
ContainerWithMostWater obj = new();

int result = obj.MaxArea_BruteForce(heights);

int result2 = obj.MaxArea(heights);

Console.ReadKey();



public class ContainerWithMostWater
{
    public int MaxArea_BruteForce(int[] heights)
    {
        int maxArea = 0;

        for (int p1 = 0; p1 < heights.Length; p1++)
        {
            for (int p2 = p1+1; p2 < heights.Length; p2++) 
            {
                int height = Math.Min(heights[p1], heights[p2]);
                int width = p2 - p1;

                int area = height * width;
                maxArea = Math.Max(maxArea, area);
            }
        }

        return maxArea;
    }

    public int MaxArea(int[] heights) 
    {
        int maxArea = 0;
        int p1 = 0;
        int p2 = heights.Length - 1;

        while (p1 < p2)
        {
            int height = Math.Min(heights[p1], heights[p2]);
            int width = p2 - p1;
            int area = height * width;
            maxArea = Math.Max(maxArea, area);

            if (heights[p1] <= heights[p2])
            { p1++; }
            else
            { p2--; }
        }

        return maxArea;
    }
}