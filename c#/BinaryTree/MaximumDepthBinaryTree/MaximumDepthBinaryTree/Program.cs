// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

Tree tree = new();
int?[] insert;
insert = new int?[] { 3, 9, 20, null, null, 15, 7 };

tree.Insert(insert);


var result = tree.MaxDepth(tree.root);
result = tree.MaxDepth_DFS(tree.root); ;

result = result;




//-------------------------------
tree = new();
insert = new int?[] { 3, 9, 20, null, null, 15, 7 };
tree.Insert(insert);
result = tree.MaxDepth_BFS(tree.root); ;
Console.WriteLine($"result BFS : {result}");
//-------------------------------
tree = new();
insert = new int?[] { 1, null, 2 };
tree.Insert(insert);
result = tree.MaxDepth_BFS(tree.root); ;
Console.WriteLine($"result BFS : {result}");




//------------------------------------------



public class Tree
{
    public TreeNode root;

    public void Insert(int?[] values)
    {
        if (values.Length == 0) { return; }
        root = new TreeNode(values[0] ?? 0, null, null);
        
        Queue<TreeNode> q = new();
        q.Enqueue(root);
        TreeNode currentNode = q.Dequeue();

        for (int i = 1; i < values.Length; i++)
        {
            //if (values[i] == null) { continue; }
            int currentValue = values[i]??0;

            if (currentNode.left != null && currentNode.right != null) 
            {
                currentNode = q.Dequeue();
            }


            if (currentNode.left == null)
            {
                currentNode.left = new TreeNode(currentValue, null, null);
                q.Enqueue(currentNode.left);
            }
            else if (currentNode.right == null)
            {
                currentNode.right = new TreeNode(currentValue, null, null);
                q.Enqueue(currentNode.right);
            }

            

        }







    }


    //using DFS
    public int MaxDepth(TreeNode node, int currentDepth = 0)
    {
        if (node == null) { return currentDepth; }

        currentDepth++;

        return Math.Max( MaxDepth(node.left, currentDepth) , MaxDepth(node.right, currentDepth) );
    }

    //JUNK - TOO SLOW - TOO MUCH CODE
    public int MaxDepth_DFS(TreeNode node)
    {
        if (node == null) { return 0; }
        int currentDepth = 1;
        int maxDepth = 1;

        Stack<TreeNode> visiting = new();
        Dictionary<int,int> visited = new();

        visiting.Push(node);

        TreeNode curr;

        while (visiting.Count() > 0 )
        {
            curr = visiting.Pop();

            bool visitedContainsLeft = curr.left == null? false : visited.ContainsKey(curr.left.val);
            bool VisitedContainsRight = curr.right== null? false : visited.ContainsKey(curr.right.val);


            if (  (curr.left == null && curr.right == null)
                  || ( visitedContainsLeft == true && VisitedContainsRight == true )
               ) //pop
            {
                maxDepth = Math.Max(maxDepth, currentDepth);

                visited.Add(curr.val, currentDepth);

                currentDepth--;
                continue;
            }

            if (visitedContainsLeft == false)
            {
                visiting.Push(curr.left);
                currentDepth++;
            }
            else 
            {
                visiting.Push(curr.right);
                currentDepth++;
            }


        }

        return maxDepth;

    }

    public int MaxDepth_BFS(TreeNode node)
    {
        if (node == null) { return 0; }
        int currentDepth = 0;

        Queue<TreeNode> q = new();

        q.Enqueue(node);

        while (q.Count > 0)
        {

            for (int sizeCurrentLevel = q.Count(); sizeCurrentLevel > 0; sizeCurrentLevel--  )
            {
                TreeNode curr = q.Dequeue();

                if (curr.left != null) { q.Enqueue(curr.left); }
                if (curr.right != null) { q.Enqueue(curr.right); }
            }
            currentDepth++;
        }

        return currentDepth;    
    }

}


public class TreeNode 
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) 
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
