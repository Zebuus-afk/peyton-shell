using System;

class Program
{
    static void Main(string[] args)
    {
        /* ----- VARIABLES ----- */
        bool a = true;
        string command;
        string title = "SHELL TITLE";
        string version = "v.b.0.1";


        /* ----- PRESENTATION ----- */
        Console.WriteLine(title + "-" + version);
        Console.WriteLine("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||");
        //Console.WriteLine("Comments.");
        //Console.WriteLine("Comments.");
        //Console.WriteLine("Comments.");
        Console.ReadKey();
        /* ----- MAKE A PAUSE ----- */
        while (a == true)
        {
            Console.Write(">>>");
            command = Console.ReadLine();
            if (command == "exit")
            {
                a = false;
                continue;
            }
            else
            {
                Console.WriteLine(command);
            }
        }
    }
}
