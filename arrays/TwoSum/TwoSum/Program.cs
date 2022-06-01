// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int[] arr = { 1, 3, 7, 9, 2 };

int findThis = 11;

var answer = TwoSum.BruteForce(arr, findThis);
TwoSum.PrintResult(arrValues: arr, answer: answer, whatToFind: findThis);

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

    //------------------------

    public static void PrintResult(int[] arrValues, int[] answer, int whatToFind)
    {
        if (answer == null || answer.Length != 2) 
        { 
            Console.WriteLine($"Input is null or of invalid length - No answer was found");
            return;
        }
        Console.WriteLine($"Seeking for {whatToFind}");
        Console.WriteLine($"    Answer - Arr[{answer[0]}] = {arrValues[answer[0]]} , Arr[{answer[1]}] = {arrValues[answer[1]]} ");
    }
}


