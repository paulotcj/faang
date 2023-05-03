// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Solution sol = new();

int[][] moves;
string result;
//----------------------

Console.WriteLine("----------------------------------------------------");
moves = new int[][] { 
    new int[] { 0, 1 }, new int[] { 0, 2 }, 
    new int[] { 1, 1 }, new int[] { 1, 2 }, 
    new int[] { 2, 1 }, new int[] { 2, 2 } };
result = sol.Tictactoe(moves);

Console.WriteLine($"The result of [[0,1],[0,2],[1,1],[1,2],[2,1],[2,2]] is: '{result}' - Expected: 'A'");


Console.WriteLine("----------------------------------------------------");
moves = new int[][] { new int[] { 0, 0 }, new int[] { 2, 0 }, new int[] { 1, 1 }, new int[] { 2, 1 }, new int[] { 2, 2 } };
result = sol.Tictactoe(moves);

Console.WriteLine($"The result of [[0,0],[2,0],[1,1],[2,1],[2,2]] is: '{result}' - Expected: 'A'");



Console.WriteLine("----------------------------------------------------");
moves = new int[][] {
    new int[] {0,0},new int[] {1,1},
    new int[] {0,1},new int[] {0,2},
    new int[] {1,0},new int[] {2,0}
};

result = sol.Tictactoe(moves);

Console.WriteLine($"The result of [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]] is: '{result}' - Expected: 'B'");


Console.WriteLine("----------------------------------------------------");
moves = new int[][] {
    new int[] {0,0},new int[] {1,1},
    new int[] {2,0},new int[] {1,0},
    new int[] {1,2},new int[] {2,1},
    new int[] {0,1},new int[] {0,2},
    new int[] {2,2}
};

result = sol.Tictactoe(moves);

Console.WriteLine($"The result of [0,0],[1,1]," +
                                $"[2,0],[1,0]," +
                                $"[1,2],[2,1]," +
                                $"[0,1],[0,2]," +
                                $"[2,2] " +
    $"is: '{result}' - Expected: 'DRAW'");
Console.WriteLine("----------------------------------------------------");

public class Solution
{
    public string Tictactoe(int[][] moves)
    {
        int[][] board = {
            new int[] {0,0,0 },
            new int[] {0,0,0 },
            new int[] {0,0,0 },
        };

        int player = 1;
        int victory = 0;

        for (int i = 0; i < moves.Length; i++) 
        {
            int row = moves[i][0];
            int column = moves[i][1];

            board[row][column] = player;

            //-----
            victory = CheckVictory(board);
            if (victory == 1) { return "A";  }
            else if (victory == 2 ) { return "B"; }
            if (i >= 9) { return "Draw"; }
            //-----

            if (player == 1) { player = 2; }
            else { player = 1; }
        }


        return "Draw";
    }

    public int CheckVictory(int[][] board)
    {
        //checking rows
        for (int i = 0; i < 3 ; i++ ) 
        {
            if (board[i][0] > 0 && board[i][0] == board[i][1] && board[i][0] == board[i][2]) { return board[i][0]; }
        }

        //checking columns
        for (int i = 0; i < 3; i++)
        {
            if (board[0][i] > 0 && board[0][i] == board[1][i] && board[0][i] == board[2][i]) { return board[0][i]; }
        }

        //Checking Diagonals
        if (board[0][0] > 0 && board[0][0] == board[1][1] && board[0][0] == board[2][2]) { return board[0][0]; }
        if (board[0][0] > 0 && board[0][2] == board[1][1] && board[0][2] == board[2][0]) { return board[0][2]; }

        return 0;
    }


    public string Tictactoe_2(int[][] moves)
    {
        int player = 1;
        int[] rows = new int[3];
        int[] cols = new int[3];
        int diag = 0;
        int anti_diag = 0;


        for (int i = 0; i < moves.Length; i++)
        {
            int row = moves[i][0];
            int col = moves[i][1];

            rows[row] += player;
            cols[col] += player;

            if (row == col)
            {
                diag += player;
            }

            //  row + col == 2      -> this will translate into coordinates [0,2],[1,1],[2,0] which are the anti-diagonal
            if (row + col == 2 )
            {
                anti_diag += player;
            }

            //the actual value might be 3 or -3 for a win
            // then we decide who won based on whose movement was just played
            if (Math.Abs(rows[row]) == 3 || 
                Math.Abs(cols[col]) == 3 || 
                Math.Abs(diag)      == 3 || 
                Math.Abs(anti_diag) == 3 )
            {
                if (player == 1) { return "A"; }
                return "B";
            }


            player *= -1;
        }

        return moves.Length == 3 * 3 ? "Draw" : "Pending";

    }
}