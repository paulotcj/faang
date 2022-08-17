// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/minimum-health-to-beat-game/

Solution sol = new();
int[] damage;
int armor = 0;
long response = 0;

Console.WriteLine("--------------------------------------------");

damage = new int[] { 2, 7, 4, 3 };
armor = 4;
response = sol.MinimumHealth_Test(damage: damage, armor: armor);
Console.WriteLine($"Response: {response} - Expected: 13");



Console.WriteLine("--------------------------------------------");

damage = new int[] { 2, 5, 3, 4 };
armor = 7;
response = sol.MinimumHealth_Test(damage: damage, armor: armor);
Console.WriteLine($"Response: {response} - Expected: 10");



Console.WriteLine("--------------------------------------------");

damage = new int[] { 3, 3, 3 };
armor = 0;
response = sol.MinimumHealth_Test(damage: damage, armor: armor);
Console.WriteLine($"Response: {response} - Expected: 10");




public class Solution
{
    public long MinimumHealth_Test(int[] damage, int armor)
    {
        long totalDamage = 0;
        long maxDamage = 0;
        long effectiveArmorProtection = 0;

        for (int i = 0; i < damage.Length ; i++ )
        {
            totalDamage += damage[i];
            maxDamage = Math.Max(maxDamage, damage[i]);
        }

        //We have to subtract now damages protected by the armor - and limited by a single level only
        //   If any max damage is less then the armor value, we subtract only the maxDamage
        //   If the armor is less than the maxDamage, we subtract only the value from the armor
        effectiveArmorProtection = Math.Min(maxDamage, armor);
        totalDamage = totalDamage - effectiveArmorProtection;

        return 1 + totalDamage; //if the total damage is X, you nees X+1 to survive.
    }


    public long MinimumHealth(int[] damage, int armor)
    {

        long totalDamage = 0, maxDamage = 0;
        long effectiveArmorProtection = 0;

        foreach (var d in damage)
        {
            totalDamage += d;

            maxDamage = Math.Max(maxDamage, d);
        }

        //We have to subtract now damages protected by the armor - and limited by a single level only
        //   If any max damage is less then the armor value, we subtract only the maxDamage
        //   If the armor is less than the maxDamage, we subtract only the value from the armor
        effectiveArmorProtection = Math.Min(armor, maxDamage);
        totalDamage = totalDamage - effectiveArmorProtection;

        return 1 + totalDamage; //if the total damage is X, you nees X+1 to survive.
    }
}