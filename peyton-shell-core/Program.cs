using System;

class Program
{
    static void Main(string[] args)
    {
        /* ----- VARIABLES ----- */
        bool a = true;
        string command;


        /* ----- PRESENTATION ----- */
        Console.WriteLine("PEYTON SHELL - v.b.0.1");
        Console.WriteLine("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||");
        Console.WriteLine("This program is a simple shell like PowerShell.");
        Console.WriteLine("So, if you use this shell, you don't will become a hacker (lol).");
        Console.WriteLine("Press a key for get access to program.");
        Console.ReadKey();
        /* ----- MAKE A PAUSE ----- */
        Console.WriteLine("Oups, this program is in development...");
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
