using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace exerciciopratico1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Artigo> list_artigo = new List<Artigo>();
            StreamReader ler = new StreamReader(@"c:\ficheiros\auchan.txt",
                            Encoding.GetEncoding("utf-8"));




            string linha;
            while ((linha = ler.ReadLine()) != null)
            {
                Artigo art = new Artigo();
                string tipo = linha.Substring(0, );
                Console.WriteLine($"{tipo}");
            }
            int opcao = 0;
            do
            {
                Console.WriteLine("1 – Mostrar no ecran o conteúdo de todo o ficheiro");
                Console.WriteLine("2 – Mostrar no ecran apenas os produtos do Hipermercado de “Setúbal”");
                Console.WriteLine("3 – Mostrar no ecran apenas os produtos da seção “Charcutaria” ordenados por quantidade de forma descendente");
                Console.WriteLine("4 – Mostrar no ecran apenas os produtos do Hipermercado do “Porto” e que sejam da seção “Charcutaria”");
                Console.WriteLine("5 – Mostrar no ecran o total da soma de todos os preços finais");
                Console.WriteLine("6 – Gerar um ficheiro “Setubal.txt” que deverá conter todos os produtos do Hipermercado “Setúbal”");
                Console.WriteLine("7 – Gerar um ficheiro “Peixaria.txt” que deverá conter todos os produtos da seção “Peixaria”");
                Console.WriteLine("8 – Sair");
                opcao = int.Parse(Console.ReadLine());

                switch (opcao)
                {
                    case 1:
                        
                        break;

                        case 2:
                        foreach (Artigo art in list_artigo)
                        {
                            Console.WriteLine($)
                        }
                            break;

                }
            } while (opcao > 0 || opcao < 9);




        }
    }
    class Artigo
    {
        public void add_artigo(string f_nome, int f_quantidade, int f_precofinal, string f_seccao, string f_loja)
        {
            Nome = f_nome;
            Precofinal = f_precofinal;
            Quantidade = f_quantidade;            
            Seccao = f_seccao;
            Loja = f_loja;
        }
        public string Nome { get; set; }
        public int Precofinal { get; set; }
        public int Quantidade { get; set; }        
        public string Seccao { get; set; }

        public string Loja { get; set; }



    }
}
