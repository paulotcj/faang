// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int[] heights = new int[] { 0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2 };

var obj = new TrappingRainWater();

int solution1 = obj.Trap_BruteForce(heights);

int solution2 = obj.Trap(heights);

Console.ReadKey();


public class TrappingRainWater
{
    public int Trap(int[] heights)
    {
        //general idea: we calculate the total water level, checking the 'column' of water above a certain point
        // in the array. Once this number is known we add up to the total water accumulator.

        int currentHeight = 0;
        int totalWater    = 0;
        int rightIdx      = heights.Length - 1 , maxRightVal = 0;
        int leftIdx       = 0                  , maxLeftVal  = 0;


        while (leftIdx < rightIdx)
        {
            /* 
               the logic here is tricky, especially considering the initial conditions, so in the first loop, we start asking which one
                is bigger the left or the right side (wall side). If they are both 0 (zero) we will move left until we find its first wall,
                then we will move right until we find its first wall. And after that, we run the loop one more time hoping the next spot on
                the left or on the right will present with a terrain depression from the maxValues (either from left or right), and this being a
                depression, it should accumulate water on top of it. Then the formula is to get the lowest wall height, subtract the current height,
                and this should give you the column of water on top of this 'hole'.
            */

            //which one (wall) is the lowest?
            if (heights[leftIdx] <= heights[rightIdx]) //left is the lowest
            {
                if (heights[leftIdx] >= maxLeftVal) //if current height is greater it wont accumulate water, same if it's at the same level as max left
                {
                    maxLeftVal = heights[leftIdx];
                }
                else
                {
                    currentHeight = heights[leftIdx];
                    totalWater += maxLeftVal - currentHeight;
                }
                leftIdx++;
            }
            else //right is the lowest
            {
                if (heights[rightIdx] >= maxRightVal)
                {
                    maxRightVal = heights[rightIdx];
                }
                else
                {
                    currentHeight = heights[rightIdx];
                    totalWater += maxRightVal - currentHeight;
                }
                rightIdx--;
            }

        }

        return totalWater;
    }

    
    public int Trap_BruteForce(int[] heights)
    {
        //general idea: we calculate the total water level, checking the 'column' of water above a certain point
        // in the array. Once this number is known we add up to the total water accumulator.

        int currentHeight = 0;
        int currentWater = 0, totalWater = 0;
        int rightIdx = 0, maxRightVal = 0;
        int leftIdx = 0, maxLeftVal = 0;


        //the logic for this 'for-loop' is: at every entry in the array we loop and inside we start 2 loops, one checking the max value to
        // the left and another one checking the max value to the right. Then the water level is determined by the lowest
        // wall level, minus the current height
        for(int i = 0; i < heights.Length; i++)
        {
            maxLeftVal = 0; maxRightVal = 0;
            leftIdx = i; rightIdx = i;

            //---
            // Navigation/scout section
            //we start checking at current point heights[i] and explore to the left of it, therefore we need to be sure this index is above 0
            while (leftIdx >= 0)
            {
                maxLeftVal = Math.Max(maxLeftVal, heights[ leftIdx ]);
                leftIdx--;
            }

            //we start checking at current point heights[i] and explore to the right of it, therefore we need to be sure this index
            // is below heights.Length
            while (rightIdx < heights.Length)
            {
                maxRightVal = Math.Max(maxRightVal, heights[ rightIdx ]);
                rightIdx++;
            }
            //---


            currentHeight = heights[i];
            currentWater = Math.Min(maxLeftVal, maxRightVal) - currentHeight; // ( height* width(1) ) - currentHeight
            if (currentWater > 0) { totalWater += currentWater; }
        }

        return totalWater;
    }
}