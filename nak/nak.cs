using System;
using System.Linq;

namespace nak
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split();
            int planCount = int.Parse(inputs[1]);
            int[] players = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Tuple<int, int>[] plans = new Tuple<int, int>[planCount];

            for (int i = 0; i < planCount; i++)
            {
                int[] planInputs = Console.ReadLine().Split().Select(int.Parse).ToArray();
                plans[i] = new Tuple<int, int>(planInputs[0], planInputs[1]);
            }

            foreach (var plan in plans)
            {
                var sortedPlayers = players.Skip(plan.Item1).Take(plan.Item2 - plan.Item1 + 1).OrderBy(p => p);
                int oldestPlayer = sortedPlayers.ElementAt(10);
                Console.WriteLine(oldestPlayer);
            }
        }
    }
}
