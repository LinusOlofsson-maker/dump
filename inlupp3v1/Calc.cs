using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Numerics;
using System.Runtime.ConstrainedExecution;
using System.Text;
using System.Threading.Tasks;

namespace inlupp3v1
{
    // Inlämningsuppgift 3 L0002B "Den egna klassen"!
    // Linus Olofsson
    // linolz-2@student.ltu.se
    internal class Calc
    {
        public Calc(List<char> persnr)
        {
            int[] pers_calc = new int[9];
            
            Persnr =  persnr;
       
            
                                        // Tar fram varje int värde från perssonnummret. 
            for (int i = 0; i < 9; i++)
            {
                pers_calc[i] = (int)Char.GetNumericValue(Persnr[i]);
            }
            
                                        // Här multipliverar jag varannat värde med 1 och 2 
            for(int k = 0; k < 9; k++)
            {
                if(k%2 == 0)
                {
             
                    pers_calc[k] = pers_calc[k]*2;
                
                }
                else
                {
                    pers_calc[k] = pers_calc[k] * 1;
                
                }
            }
            List<int> sumlist = new List<int>();
            int z;
            foreach (int b in pers_calc)
            {
                                        // Genom att itterera över " pers_calc " listan a.e då z=b. 
                                        // Jag ansätter även z som variabel iställer för b 
                                        // då eventuella beräkningar måste genomföras 
                z = b;
                while (z > 0) 
                {
                    int mod = z % 10;   // Medans z inte är noll så tas hela tiden sista siffran bort för
                    sumlist.Add(mod);   // Att dela upp alla värden över 10 så vi kan addera produkterna  
                    z = z / 10;         // tillsammans För att ta reda på kontrollsiffran  
                }
                                        // Obs! Jag tar ej hänsyn till de gånger 0 återfinns i personnummret
                                        // Då addition av 0 är trivialt 0 ;) 
            }           
            int num;
            num = sumlist.Sum();
            numercontrol = 10 - (num % 10); // "Entallsiffran" == (num % 10) där av är            
        }
        public List<char> Persnr { get; set; }
        public int numercontrol { get; set; }

        public override string ToString()
        { 
            return " Kontrollnummer: " + numercontrol;
        }

    }
}
        
