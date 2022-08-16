// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/k-closest-points-to-origin/

int[][] points;
int k;
int[][] result;
Solution sol = new();

Console.WriteLine("-----------------------------------------------");

points = new int[][] { new int[] { 1, 3 }, new int[] { - 2, 2 } };
k = 1;
result = sol.KClosest(points, k);

Console.WriteLine($"Expected result: \n" +
    $"[          \n" +
    $"    [-2,2] \n" +
    $"]          \n" + 
    $"Actual result:\n {sol.Stringfy(result)}"
);

Console.WriteLine("-----------------------------------------------");


points = new int[][] { new int[] { 3, 3 }, new int[] { 5, -1 }, new int[] { -2, 4 }, };
k = 2;
result = sol.KClosest(points, k);

Console.WriteLine($"Expected result: \n" +
    $"[         \n" +
    $"	[3,3],  \n" +
    $"	[-2,4]  \n" +
    $"]         \n" +
    $"Actual result:\n{sol.Stringfy(result)}"
);

Console.WriteLine("-----------------------------------------------");




public class Solution
{

    public int[][] KClosest2(int[][] points, int K)
    {
        if (points == null || points.Length == 0) { return new int[][] { }; }

        // dist = SQRT( (x1-x2)^2 + (y1-y2)^2 )
        // but since the origin is (0,0) we can simplify -> SQRT( (x1)^2 + (y1)^2 )
        int[][] result = points.OrderBy(
                //x => Math.Sqrt(  Math.Pow(x[0], 2) + Math.Pow(x[1], 2) )
                x => Math.Pow(x[0], 2) + Math.Pow(x[1], 2) //we can get away without doing SQRT here
            )
            .Take(K)
            .ToArray();

        return result;
    }


    public int[][] KClosest(int[][] points, int K)
    {
        if (points == null || points.Length == 0)
            return new int[][] { };

        return points.OrderBy(x => Math.Pow(x[0], 2) + Math.Pow(x[1], 2)).Take(K).ToArray();
    }

    //-------------------------------------------

    public string Stringfy(int[][] points)
    {
        string response = "[\n";

        foreach(var item_a in points)
        {
            response += "    [";

            foreach (var item_b in item_a)
            {
                response += item_b + ",";
            }


            response += "],\n";
        }


        response += "]\n";


        return response;
    }
}