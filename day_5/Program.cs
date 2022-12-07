namespace AdventOfCode
{
    class Program
    {
        static void Main(string[] args)
        {
            int counter = 0;




            List<List<String>> arr = new List<List<string>>();

            arr.Add(new List<string> { "b", "s", "j", "z", "v", "d", "g" });
            arr.Add(new List<string> { "p", "v", "g", "m", "s", "z" });
            arr.Add(new List<string> { "f", "q", "t", "w", "s", "b", "l", "c" });
            arr.Add(new List<string> { "q", "v", "r", "m", "w", "g", "j", "h" });
            arr.Add(new List<string> { "d", "m", "f", "n", "s", "l", "c" });
            arr.Add(new List<string> { "d", "c", "g", "r" });
            arr.Add(new List<string> { "q", "s", "d", "j", "r", "t", "g", "h" });
            arr.Add(new List<string> { "v", "f", "p" });
            arr.Add(new List<string> { "j", "t", "s", "r", "d" });




            // Read the file and display it line by line.  
            foreach (string line in System.IO.File.ReadLines(@"./input"))
            {
                Console.WriteLine(line);
                List<string> parsed = new List<string>(line.Split(' ', StringSplitOptions.RemoveEmptyEntries));
                List<string> subList = arr[(Int32.Parse(parsed[3])) - 1].GetRange(0, Int32.Parse(parsed[1]));
                //subList.Reverse(); Part 1

                for (int index = (Int32.Parse(parsed[1]) - 1); index >= 0; index--)
                {
                    arr[Int32.Parse(parsed[3]) - 1].RemoveAt(index);
                }


                arr[(Int32.Parse(parsed[5]) - 1)].InsertRange(0, subList);



                counter++;
            }
            foreach (List<string> i in arr)
            {
                Console.WriteLine(String.Join(" ", i));
            }

        }

    }
}