using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace ex2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            FileInfo novo = new FileInfo(@"c:\ficheiros\meuficheiro.txt");
            FileStream fstr = novo.Create();
            fstr.Close();
        }
    }
}
