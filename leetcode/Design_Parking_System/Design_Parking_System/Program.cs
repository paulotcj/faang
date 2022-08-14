// See https://aka.ms/new-console-template for more information
//https://leetcode.com/problems/design-parking-system/

Console.WriteLine("Hello, World!");

ParkingSystem ps = new(1,1,0);
bool result;

Console.WriteLine($"Current capacity: BIG:1 , MEDIUM:1 , SMALL: 0");


result = ps.AddCar(1);
Console.WriteLine($"Adding BIG, result: {result} expected: TRUE");

result = ps.AddCar(2);
Console.WriteLine($"Adding MEDIUM, result: {result} expected: TRUE");

result = ps.AddCar(3);
Console.WriteLine($"Adding SMALL, result: {result} expected: FALSE");


result = ps.AddCar(1);
Console.WriteLine($"Adding BIG, result: {result} expected: FALSE");


public class ParkingSystem
{
    Dictionary<int, Parking> dicParking;
    public ParkingSystem(int big_spots, int medium_spots, int small_spots)
    {
        dicParking = new Dictionary<int, Parking>()
        {
            {1,new Parking(carType: 1,spots: big_spots      ,count: 0)},
            {2,new Parking(carType: 2,spots: medium_spots   ,count: 0)},
            {3,new Parking(carType: 3,spots: small_spots    ,count: 0)}
        };
    }

    public bool AddCar(int carType)
    {
        Parking parking = dicParking[carType];

        if (parking.spots == parking.count) { return false; }

        parking.count++;

        
        return true;
    }
}

public class Parking
{
    public int carType;
    public int spots;
    public int count;

    public Parking(int carType, int spots, int count = 0)
    {
        this.carType = carType;
        this.spots = spots;
        this.count = count;
    }
}
