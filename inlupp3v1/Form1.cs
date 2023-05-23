using System;
using System.Diagnostics;
using System.Collections;
// Inlämningsuppgift 3 L0002B "programmet"!
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
                                        // Definerar lite utgångs variabler jag använder. 
            string x = text_number.Text;
            char chr;
            char cont;
            List<char> ints = new List<char>();
            List<char> control = new List<char>();
                                        // Presenterar de olika inputsen från användaren i Windows Form. 
            list_info.Items.Add(text_firstname.Text);
            list_info.Items.Add(text_lastname.Text);
            list_info.Items.Add(text_number.Text);
            name_ctrl.Text = text_firstname.Text + " " + text_lastname.Text;
            gender_ctrl.Text = "Är en: ";
                                        // Här sparar jag egentligen bara sista sifran i perssonnummret  
                                        // för att kolla så att mina beräkningar stämmer.
            for (int p = 0; p < x.Length; p++)
            {
                cont = x[p];
                control.Add(cont);
            }
            cont = control.Last();
             
                                        // Här skickar vi in de första 9 siffrorna för att kontrollera om personnummret stämmer.
            
            for (int i = 0; i < 9;i++)
            {
                chr = x[i];
                ints.Add(chr);

            }
                                        // Här kollar jag om det är en man eller kvinna genom att kontrollera om den sista
                                        // siffra dvs 9 är jämn eller udda. 
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
                                        // Ropar på min andra klass där jag beräknar och kollar personnummret. 
            Calc calc = new Calc(ints);
 
                                        // Kontrollerar så att mitt beräknade värde på siffran 10 i personnummret stämmer överens 
                                        // med det som användaren har angett. 
            if (calc.numercontrol == (int)Char.GetNumericValue(cont))
            {
                persnr_ctrl.Text = "Personnummret är Godkännt";
            }
            if (calc.numercontrol != (int)Char.GetNumericValue(cont))
            {
                persnr_ctrl.Text = "Personnummret är EJ Godkännt";
            }
        }
                                        // Rensar all info som jag tillfört till användaren! 
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
                                    // Så återfinns endast 
                                    // Kod för Placeholders 
                                    // På textfälten !
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