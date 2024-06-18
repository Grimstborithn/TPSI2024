using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ex4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FileInfo fich = new FileInfo(@"c:\ficheiros\ficheiro.txt");
            StreamWriter.WriteLine("Esta é a minha primeira linha");

        }
    }
}
