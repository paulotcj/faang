// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

Traverse traverse = new();
List<int> result = traverse.TraverseDFS();

result = traverse.TraverseBFS();



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

        //----- DEBUG
        //if (matrix[row, col] == 16)
        //{ }
        //-----

        //this routine will look for the next number to visit (clockwise direction) if it cant find any new number in its
        //  neighbourhood then we stop. Note: with this method it's perfectly possible to pick the wrong number to start
        //  and end-up in a dead end, thus, return this function without visiting all nodes.
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
    //------------------------------------------------------------

    public List<int> TraverseBFS(int[,] matrix = null)
    {
        //lets set things up...
        if (matrix == null) { matrix = localMatrix; } //null paramter check...
        bool[,] seen = new bool[matrix.GetLength(0), matrix.GetLength(1)]; //declare and initialize matrix 'seen'
        List<int> valuesVisited = new(); //declares the values visited list

        Queue<int[]> q = new();
        q.Enqueue( new int[] {0,0} );

        while (q.Count > 0)
        {
            int[] current = q.Dequeue();
            int row = current[0];
            int col = current[1];

            //check if we are within the bounds - row and col must be greather than 0 and less than the matrix limits 
            //  (row < matrix.lenght and col < matrix[0].lenght), but of course since we are looking for ways where these
            //  conditions will fail, we flip the logic
            if (row < 0 || row >= matrix.GetLength(0) ||
                col < 0 || col >= matrix.GetLength(1) ||
                seen[row,col] == true
                )
            { continue; }

            seen[row, col] = true;
            valuesVisited.Add(matrix[row,col] );

            //---
            //this routine will place all possible moves (clockwise) from the current direction in the queue (up, right, down, left)
            // then in the next iteration of the 'while loop' we will check each of these moves agains the matrix of 'seen' values, if
            // we have visited the suggested position we will skip it. (of course we also check against our of bounds movements)
            for (int i = 0; i < directions.GetLength(0); i++)
            {
                int row_move = directions[i, 0];
                int col_move = directions[i, 1];

                q.Enqueue( new int[] { row + row_move, col + col_move } );
            }
            //---
        }

        return valuesVisited;
    }

}