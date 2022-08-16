// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
//https://leetcode.com/problems/search-suggestions-system/

string[] products;
string searchword;
IList<IList<string>> response;
Solution sol = new();

Console.WriteLine("------------------------------------------------------");

products = new string[] { "mobile", "mouse", "moneypot", "monitor", "mousepad" };
searchword = "mouse";
response = sol.SuggestedProducts_Test2(products: products , searchWord: searchword);

Console.WriteLine($"Expected output: \n" +
$"[                              \n" +
$"    [mobile,moneypot,monitor], \n" +
$"    [mobile,moneypot,monitor], \n" +
$"    [mouse,mousepad],          \n" +
$"    [mouse,mousepad],          \n" +
$"    [mouse,mousepad]           \n" +
$"]                              \n" +
$"actual output: \n{sol.Print(response)}");

sol.Print(response);


Console.WriteLine("------------------------------------------------------");


products = new string[] { "havana" };
searchword = "havana";
response = sol.SuggestedProducts_Test2(products: products, searchWord: searchword);
Console.WriteLine($"Expected output: \n" +
$"[             \n" +
$"    [havana], \n" +
$"    [havana], \n" +
$"    [havana], \n" +
$"    [havana], \n" +
$"    [havana], \n" +
$"    [havana]  \n" +
$"]             \n" +
$"actual output: \n{sol.Print(response)}");

sol.Print(response);


Console.WriteLine("------------------------------------------------------");



products = new string[] { "bags", "baggage", "banner", "box", "cloths" };
searchword = "bags";
response = sol.SuggestedProducts_Test2(products: products, searchWord: searchword);
Console.WriteLine($"Expected output: \n" +
$"[                          \n" +
$"    [baggage,bags,banner], \n" +
$"    [baggage,bags,banner], \n" +
$"    [baggage,bags],        \n" +
$"    [bags]                 \n" +
$"]                          \n" +
$"actual output: \n{sol.Print(response)}");

sol.Print(response);


Console.WriteLine("------------------------------------------------------");




public class Solution
{

    public IList<IList<string>> SuggestedProducts_Test2(string[] products, string searchWord)
    {
        List<IList<string>> responseObj = new();
        List<string> productList = products.ToList().OrderBy(x => x).ToList(); //we need to produce the answer in alphabetical order
        //----------------
        for (int i  = 0; i < searchWord.Length ; i++ ) 
        {
            //the logic here is: we are start with the first character and filter the list and assign to itself. Anything that doesn't match
            // the first char is not supposed to be returned anyway. Then we keep the process for all characters of the searchWord
            productList = productList
                .Where( x =>
                    x.StartsWith( searchWord.Substring(0, (i+1))  )
                ).ToList();

            responseObj.Add(productList.Take(3).ToList()); //note: product list is already ordered

        }

        return responseObj;
    }


    public IList<IList<string>> SuggestedProducts2(string[] products, string searchWord)
    {
        var lists = new List<IList<string>>();
        var list = products.ToList().OrderBy(w => w).ToList();
        for (int i = 0; i < searchWord.Length; i++)
        {
            list = list
                .Where(
                    w => w.StartsWith(searchWord.Substring(0, i + 1))
                )
                .ToList();


            lists.Add(list.Take(3).ToList());
        }
        return lists;
    }

    //------------------------------------------------------

    public IList<IList<string>> SuggestedProducts_Test1(string[] products , string searchWord)
    {
        Array.Sort(products); //we need to produce the answer in alphabetical order
        var returnObj = Enumerable //Static Library Enumerable
            .Range(1, searchWord.Length) //ints ranging from 1 to length, this effectively do the trick where we have to get results basen on the 1st to nth character
            .Select( paramInt => //SELECT 'EM!!!
                products
                .Where( 
                    strProd => string.Compare(strA : searchWord, indexA : 0, strB : strProd, indexB : 0, length:  paramInt) == 0
                )
                .Take(3)
                .ToArray()
            )
            .ToArray();

        return returnObj;
    }

    //public IList<IList<string>> SuggestedProducts(string[] products, string searchWord)
    //{
    //    Array.Sort(products);
    //    return Enumerable.Range(1, searchWord.Length)
    //        .Select(i =>
    //            products.Where(p => string.Compare(searchWord, 0, p, 0, i) == 0).Take(3).ToArray()
    //        )
    //        .ToArray();
    //}





    public string Print(IList<IList<string>> list)
    {
        string response = "[\n";
        foreach ( var item_a in list )
        {
            response += "    [";
            foreach (var item_b in item_a)
            {
                response += item_b + ",";
            }
            response += "],\n";
        }
        response += "]\n";

        return response;
    }
}
