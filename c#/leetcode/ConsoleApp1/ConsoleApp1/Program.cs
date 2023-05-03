// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
Solution sol = new();
int[] intArr;
string[] strArr;
long response;
//sol.Validate();

//List<int> list = new();
//list.Add(2);
//list.Add(9);
//list.Add(10);
//list.Add(3);
//list.Add(7);



//List<int> list = new();
//list.Add(4);
//list.Add(30);
//list.Add(15);
//list.Add(5);
//list.Add(9);


List<int> list = new();
list.Add(2);
list.Add(3);
list.Add(2);
list.Add(1);



Console.WriteLine("---------------------------------");
//intArr = new int[] { };
//strArr = new string[] { };
response = Solution.findTotalPower(list);
//Console.WriteLine($"Result: {0} - Expected: 1");



Console.WriteLine("---------------------------------");

public class Solution
{

    public static int findTotalPower(List<int> power)
    {
        int totalPower = 0;

        int start = 0;
        int length = 1;
        List<int> sumList = new List<int>();
        long sum = 0;

        for (int i  = 0; i < power.Count; i++  )
        {
            //incomplete

            for (length = 1; length < power.Count; length++)
            {
                var min = power.Take(i..(i+length)).Min();
                int localSum = power.Take(i..(i + length)).Sum();

                sumList.Add(min * localSum);
            }

        }

        foreach (int item in sumList)
        {
            sum += item;
        }

        sum = sum % (1000000000 + 7);
        return (int)sum;


    }



    public static long getHeaviestPackage(List<int> packageWeights)
    {
        //NOTE: Full transparency - HackerRank warned me about changing windows, but I understand that using a IDE
        // was allowed in this task. So I used VS2022
        long heaviestPackage = 0;


        for (int i = packageWeights.Count - 1; i > 0; i--) //do not loop to zero as we need to check i-1 = 0
        {
            int packAt_i = packageWeights[i];
            int packAt_imin1 = packageWeights[i - 1];
            if (packAt_i > packAt_imin1)
            {
                int sum = packageWeights[i] + packageWeights[i - 1];
                packageWeights.RemoveAt(i);
                packageWeights[i - 1] = sum;

                heaviestPackage = Math.Max(heaviestPackage, sum);
            }

        }

        return heaviestPackage;
    }



    public static long getHeaviestPackage_temp(List<int> packageWeights)
    {
        //NOTE: Full transparency - HackerRank warned me about changing windows, but I understand that using a IDE
        // was allowed in this task. So I used VS2022
        long heaviestPackage = 0;


        for (int i = 0; i < packageWeights.Count - 2; i++)
        {
            int a = 0;
            int b = 0;
            if (packageWeights[i] < packageWeights[i + 1])
            {
                int sum = packageWeights[i] + packageWeights[i + 1];
                packageWeights.RemoveAt(i + 1);
                packageWeights[i] = sum;

                heaviestPackage = Math.Max(heaviestPackage, sum);
            }

        }

        return heaviestPackage;
    }


    //---
    public void Validate()
    {
        Console.WriteLine("we are good");
    }
    //---
}