using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ex3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FileInfo apagar = new FileInfo(@"c:\ficheiros\meuficheiro.txt");
            apagar.Delete();
        }
    }
}
