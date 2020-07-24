

csharp_code = """using System;

class HelloWorld
{
    static void Main()
    {
        Console.WriteLine("I'm Rocky");
    }
}"""


rock_it_bro = RockStar(days=400, file_name='rockstar.cs', code=csharp_code)
rock_it_bro.make_me_a_rockstar()