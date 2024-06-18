using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace exercicios
{
    internal class Program
    {
        static void Main(string[] args)
        {

            DirectoryInfo pasta = new DirectoryInfo(@"C:\ficheiros");

            FileInfo[] ficheiros = pasta.GetFiles("*.*");
            foreach (FileInfo fich in ficheiros)
            {
                Console.WriteLine($"\n{fich.Name} - {fich.CreationTime} - {fich.Length}kb");
            }
            Console.ReadKey();
        }
    }
}
