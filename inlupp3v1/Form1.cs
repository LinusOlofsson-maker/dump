using System;
using System.Diagnostics;
using System.Collections;
// Inl�mningsuppgift 3 L0002B "programmet"!
// Linus Olofsson
// linolz-2@student.ltu.se
namespace inlupp3v1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
                                       // Avslutar programmet 
        private void btn_quit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btn_add_Click(object sender, EventArgs e)
        {
                                        // Definerar lite utg�ngs variabler jag anv�nder. 
            string x = text_number.Text;
            char chr;
            char cont;
            List<char> ints = new List<char>();
            List<char> control = new List<char>();
                                        // Presenterar de olika inputsen fr�n anv�ndaren i Windows Form. 
            list_info.Items.Add(text_firstname.Text);
            list_info.Items.Add(text_lastname.Text);
            list_info.Items.Add(text_number.Text);
            name_ctrl.Text = text_firstname.Text + " " + text_lastname.Text;
            gender_ctrl.Text = "�r en: ";
                                        // H�r sparar jag egentligen bara sista sifran i perssonnummret  
                                        // f�r att kolla s� att mina ber�kningar st�mmer.
            for (int p = 0; p < x.Length; p++)
            {
                cont = x[p];
                control.Add(cont);
            }
            cont = control.Last();
             
                                        // H�r skickar vi in de f�rsta 9 siffrorna f�r att kontrollera om personnummret st�mmer.
            
            for (int i = 0; i < 9;i++)
            {
                chr = x[i];
                ints.Add(chr);

            }
                                        // H�r kollar jag om det �r en man eller kvinna genom att kontrollera om den sista
                                        // siffra dvs 9 �r j�mn eller udda. 
            var item = ints[^1];
            if (item%2 == 0)
            {
                // Kvinna
                label_man.Text = "Kvinna";

            }
            else
            {
                // Man
                label_man.Text = "Man";
            }
                                        // Ropar p� min andra klass d�r jag ber�knar och kollar personnummret. 
            Calc calc = new Calc(ints);
 
                                        // Kontrollerar s� att mitt ber�knade v�rde p� siffran 10 i personnummret st�mmer �verens 
                                        // med det som anv�ndaren har angett. 
            if (calc.numercontrol == (int)Char.GetNumericValue(cont))
            {
                persnr_ctrl.Text = "Personnummret �r Godk�nnt";
            }
            if (calc.numercontrol != (int)Char.GetNumericValue(cont))
            {
                persnr_ctrl.Text = "Personnummret �r EJ Godk�nnt";
            }
        }
                                        // Rensar all info som jag tillf�rt till anv�ndaren! 
        private void btn_clear_Click(object sender, EventArgs e)
        {
            list_info.Items.Clear();
            text_firstname.Text = "";
            text_lastname.Text = "";
            text_number.Text = "";
            persnr_ctrl.Text = "";
            name_ctrl.Text = "";
            gender_ctrl.Text = "";
            label_man.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void text_lastname_TextChanged(object sender, EventArgs e)
        {

        }

        private void text_firstname_TextChanged(object sender, EventArgs e)
        {

        }
                                    // UNDER DENNA KOMMENTAR //
                                    // S� �terfinns endast 
                                    // Kod f�r Placeholders 
                                    // P� textf�lten !
        private void text_firstname_Enter(object sender, EventArgs e)
        {
            if(text_firstname.Text == "First Name")
            {
                text_firstname.Text = "";
                text_firstname.ForeColor = Color.Black;
            }
        }

        private void text_firstname_Leave(object sender, EventArgs e)
        {
            if (text_firstname.Text == "")
            {
                text_firstname.Text = "First Name";
                text_firstname.ForeColor = Color.Silver;
            }
        }

        private void text_lastname_Enter(object sender, EventArgs e)
        {
            if (text_lastname.Text == "Sir Name")
            {
                text_lastname.Text = "";
                text_lastname.ForeColor = Color.Black;
            }
        }

        private void text_lastname_Leave(object sender, EventArgs e)
        {
            if (text_lastname.Text == "")
            {
                text_lastname.Text = "Sir Name";
                text_lastname.ForeColor = Color.Silver;
            }
        }

        private void text_number_Enter(object sender, EventArgs e)
        {
            if (text_number.Text == "10 digits")
            {
                text_number.Text = "";
                text_number.ForeColor = Color.Black;
            }
        }

        private void text_number_Leave(object sender, EventArgs e)
        {
            if (text_number.Text == "")
            {
                text_number.Text = "10 digits";
                text_number.ForeColor = Color.Silver;
            }
        }
    }
}