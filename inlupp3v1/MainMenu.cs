using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace inlupp3v1
{
    // Inlämningsuppgift 3 L0002B "MainMenu"!
    // Linus Olofsson
    // linolz-2@student.ltu.se
    public partial class MainMenu : Form
    {
        public MainMenu()
        {
            InitializeComponent();
        }

        private void btn_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void LoadGame(object sender, EventArgs e)
        {
            Form1 gameWindow = new Form1();
            gameWindow.Show();
            this.Hide();

        }

        private void MainMenu_Load(object sender, EventArgs e)
        {

        }
    }
}
