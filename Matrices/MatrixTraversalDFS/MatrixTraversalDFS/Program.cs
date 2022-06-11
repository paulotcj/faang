// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

Traverse traverse = new();

List<int> result = traverse.TraverseDFS();

var abc = "";


public class Traverse
{
    private int[,] directions = new int[,] {
       //row , column
        {-1,  0 }, //up
        { 0 , 1 }, //right
        { 1 , 0 }, //down
        { 0 ,-1 }  //left
    };

    private int[,] localMatrix = new int[,] {
        { 1 ,  2 ,  3 ,  4 ,  5 },
        { 6 ,  7 ,  8 ,  9 , 10 },
        {11 , 12 , 13 , 14 , 15 },
        {16 , 17 , 18 , 19 , 20 },
    };

    private void DFS(int[,] matrix, int row, int col, bool[,] seen, List<int> valuesVisited)
    {
        //check if we are within the bounds - row and col must be greather than 0 and less than the matrix limits 
        //  (row < matrix.lenght and col < matrix[0].lenght), but of course since we are looking for ways where these
        //  conditions will fail, we flip the logic
        if ( row < 0 ||
             col < 0 ||
             row >= matrix.GetLength(0) || //typically 4 in this example
             col >= matrix.GetLength(1)  || //typically 5 in this example
             seen[row,col] == true
        )
        { return; }

        seen[row,col] = true; //mark this coordinate as seen
        valuesVisited.Add(matrix[row,col]); //add the current value to the list of values explored

        for (int i = 0; i < directions.GetLength(0); i++)
        {
            //we try to check our neighbourhood in clockwise movements: up, right, down, left
            int row_move = directions[i, 0]; // row movements: -1 = up   , 0 = no movement, 1 = down
            int col_move = directions[i, 1]; // col movements: -1 = left , 0 = no movement, 1 = right
            DFS(matrix, row + row_move, col + col_move, seen, valuesVisited);
        }
    }

    public List<int> TraverseDFS(int[,] matrix = null)
    {
        //lets set things up...
        if (matrix == null) { matrix = localMatrix; } //null paramter check...
        bool[,] seen = new bool[matrix.GetLength(0), matrix.GetLength(1)]; //declare and initialize matrix 'seen'
        List<int> valuesVisited = new(); //declares the values visited list


        DFS(matrix: matrix, row: 0, col: 0, seen: seen, valuesVisited: valuesVisited);

        return valuesVisited;

    }

}