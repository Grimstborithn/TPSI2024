using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ex8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numero = new List<int>();

            Random aleatorio = new Random();


            for (int i = 0; i < 20; i++) { 
            numero.Add(aleatorio.Next(1, 1000));
            }

            Console.WriteLine("------------- Listar todos os números ------------");

            foreach(int num in numero)
            {
                Console.Write($"{num} ");
            }
          

            Console.WriteLine("\n\n------------- Listar nºs > 250 ------------");

            foreach (int num in numero.Where(x => x > 250))
            {
                Console.Write($"{num} ");
            }


            Console.WriteLine("\n\n------------- Listar nºs pares ------------");

            foreach (int num in numero.Where(x => x %2 == 0))
            {
                Console.Write($"{num} ");
            }

            Console.WriteLine("\n\n------------- Listar nºs ímpares ------------");

            foreach (int num in numero.Where(x =>  x % 2 != 0))
            {
                Console.Write($"{num} ");
            }
            
            
            Console.WriteLine("\n\n------------- Listar nºs de forma ASC ------------");

            foreach (int num in numero.OrderBy(x => x))
            {
                Console.Write($"{num} ");
            }

            Console.WriteLine("\n\n------------- Listar nºs de forma DSC ------------");

            foreach (int num in numero.OrderByDescending(x => x))
            {
                Console.Write($"{num} ");
            }


            Console.WriteLine("\n\n------------- Mostrar o maior ------------");

            int maior = numero.Max();
                Console.WriteLine($"O maior é {maior}");

            Console.WriteLine("\n\n------------- Mostrar o menor ------------");

            int menor = numero.Min();
            Console.WriteLine($"O menor é {menor}");

            Console.WriteLine("\n\n------------- Mostrar a média ------------");

            double media = numero.Average();
            Console.WriteLine($"O média é {media}");

            Console.WriteLine("\n\n------------- A soma de todos ------------");

            int soma = numero.Sum();
            Console.WriteLine($"O soma é {soma}");


            Console.ReadKey();
        }
    }
}
