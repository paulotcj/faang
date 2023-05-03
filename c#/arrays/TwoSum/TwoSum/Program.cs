// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int[] arr = { 1, 3, 7, 9, 2 };

int findThis = 11;

var answer = TwoSum.BruteForce(arr, findThis);
TwoSum.PrintResult(arrValues: arr, answer: answer, whatToFind: findThis);

var answer2 = TwoSum.Optimized(arr, findThis);
TwoSum.PrintResult(arrValues: arr, answer: answer2, whatToFind: findThis);


public static class TwoSum
{
    public static int[] BruteForce(int[] arr, int target)
    {
        for (int i = 0; i < arr.Length; i++)
        {
            int numberToFind = target - arr[i];

            for (int j = i + 1; j < arr.Length; j++)
            {
                if (numberToFind == arr[j]) 
                { 
                    return new int[] { i, j }; 
                }
            }
        }

        return null;
    }



    //the idea here is to start looping through the array, and finding the difference between the actual number and the target
    //  so suppose we want to find 2 numbers that sums up to 7, and the current value is 2 at index 3; we then store the difference
    //  and the index where this difference was calculated from, taking this example we would have: dic[5] = 3
    //  since diff = 7 - 2 -> diff = 5
    // so then we will be looping trying to find a number which the difference will match an existing diff in the dictionary
    //  suppose now the current value is 5 at index 22, we check if there's an entry in the dictionary where the key is 5
    //  and given our example, we have one entry, and by looking at this we know that we will find the matching pair at index 3 of the
    //  array given
    //  we would have an answer then by looking at arr[3] = 2 , arr[22] = 5 , and 5+2 = 7, the answer is [3,22]
    public static int[] Optimized(int[] arr, int target)
    {
        Dictionary<int, int> dicNumberToFind_Indexes = new();
        for (int i = 0; i < arr.Length; i++)
        {
            int? arrayIndexAnswer = null;
            int currentValue = arr[i];

            if (dicNumberToFind_Indexes.ContainsKey(currentValue) == true) //is this the (difference) value we are looking for?
            {
                arrayIndexAnswer = dicNumberToFind_Indexes[currentValue];
            }
                
            //it's useful if you think of this part as starting point
            if (arrayIndexAnswer == null)
            {
                int numberToFind = target - currentValue;
                dicNumberToFind_Indexes[numberToFind] = i; //dictionary key = number to find , value = index of where to find it
            }
            else
            {
                return new int[] { (int)arrayIndexAnswer, i };
            }
        }

        return null;
    }

    //------------------------

    public static void PrintResult(int[] arrValues, int[] answer, int whatToFind)
    {
        if (answer == null || answer.Length != 2) 
        { 
            Console.WriteLine($"Input is null or of invalid length - No answer was found");
            return;
        }
        Console.WriteLine($"Seeking for {whatToFind}");
        Console.WriteLine($"    Answer - Arr[{answer[0]}] = {arrValues[answer[0]]} , Arr[{answer[1]}] = {arrValues[answer[1]]}  - Sum: { arrValues[answer[0]] + arrValues[answer[1]] }");

    }
}


