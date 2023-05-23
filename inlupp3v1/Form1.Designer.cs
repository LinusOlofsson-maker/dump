namespace inlupp3v1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_add = new System.Windows.Forms.Button();
            this.btn_clear = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.list_info = new System.Windows.Forms.ListBox();
            this.btn_quit = new System.Windows.Forms.Button();
            this.text_firstname = new System.Windows.Forms.TextBox();
            this.text_lastname = new System.Windows.Forms.TextBox();
            this.text_number = new System.Windows.Forms.TextBox();
            this.name_ctrl = new System.Windows.Forms.Label();
            this.gender_ctrl = new System.Windows.Forms.Label();
            this.label_man = new System.Windows.Forms.Label();
            this.persnr_ctrl = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_add
            // 
            this.btn_add.Location = new System.Drawing.Point(227, 199);
            this.btn_add.Name = "btn_add";
            this.btn_add.Size = new System.Drawing.Size(75, 23);
            this.btn_add.TabIndex = 0;
            this.btn_add.Text = "OK";
            this.btn_add.UseVisualStyleBackColor = true;
            this.btn_add.Click += new System.EventHandler(this.btn_add_Click);
            // 
            // btn_clear
            // 
            this.btn_clear.Location = new System.Drawing.Point(227, 351);
            this.btn_clear.Name = "btn_clear";
            this.btn_clear.Size = new System.Drawing.Size(75, 23);
            this.btn_clear.TabIndex = 1;
            this.btn_clear.Text = "Clear";
            this.btn_clear.UseVisualStyleBackColor = true;
            this.btn_clear.Click += new System.EventHandler(this.btn_clear_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 71);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(55, 15);
            this.label1.TabIndex = 2;
            this.label1.Text = "Förnamn";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 109);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(62, 15);
            this.label2.TabIndex = 3;
            this.label2.Text = "Efternamn";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 149);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(89, 15);
            this.label3.TabIndex = 4;
            this.label3.Text = "Personnummer";
            // 
            // list_info
            // 
            this.list_info.FormattingEnabled = true;
            this.list_info.ItemHeight = 15;
            this.list_info.Location = new System.Drawing.Point(87, 199);
            this.list_info.Name = "list_info";
            this.list_info.Size = new System.Drawing.Size(120, 184);
            this.list_info.TabIndex = 5;
            // 
            // btn_quit
            // 
            this.btn_quit.Location = new System.Drawing.Point(597, 360);
            this.btn_quit.Name = "btn_quit";
            this.btn_quit.Size = new System.Drawing.Size(75, 23);
            this.btn_quit.TabIndex = 6;
            this.btn_quit.Text = "Avsluta";
            this.btn_quit.UseVisualStyleBackColor = true;
            this.btn_quit.Click += new System.EventHandler(this.btn_quit_Click);
            // 
            // text_firstname
            // 
            this.text_firstname.ForeColor = System.Drawing.SystemColors.InactiveCaption;
            this.text_firstname.Location = new System.Drawing.Point(107, 71);
            this.text_firstname.Name = "text_firstname";
            this.text_firstname.Size = new System.Drawing.Size(100, 23);
            this.text_firstname.TabIndex = 7;
            this.text_firstname.Text = "First Name";
            this.text_firstname.TextChanged += new System.EventHandler(this.text_firstname_TextChanged);
            this.text_firstname.Enter += new System.EventHandler(this.text_firstname_Enter);
            this.text_firstname.Leave += new System.EventHandler(this.text_firstname_Leave);
            // 
            // text_lastname
            // 
            this.text_lastname.ForeColor = System.Drawing.SystemColors.InactiveCaption;
            this.text_lastname.Location = new System.Drawing.Point(107, 109);
            this.text_lastname.Name = "text_lastname";
            this.text_lastname.Size = new System.Drawing.Size(100, 23);
            this.text_lastname.TabIndex = 8;
            this.text_lastname.Text = "Sir Name";
            this.text_lastname.TextChanged += new System.EventHandler(this.text_lastname_TextChanged);
            this.text_lastname.Enter += new System.EventHandler(this.text_lastname_Enter);
            this.text_lastname.Leave += new System.EventHandler(this.text_lastname_Leave);
            // 
            // text_number
            // 
            this.text_number.ForeColor = System.Drawing.SystemColors.InactiveCaption;
            this.text_number.Location = new System.Drawing.Point(107, 149);
            this.text_number.Name = "text_number";
            this.text_number.Size = new System.Drawing.Size(100, 23);
            this.text_number.TabIndex = 9;
            this.text_number.Text = "10 digits";
            this.text_number.Enter += new System.EventHandler(this.text_number_Enter);
            this.text_number.Leave += new System.EventHandler(this.text_number_Leave);
            // 
            // name_ctrl
            // 
            this.name_ctrl.AutoSize = true;
            this.name_ctrl.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.name_ctrl.Location = new System.Drawing.Point(570, 66);
            this.name_ctrl.Name = "name_ctrl";
            this.name_ctrl.Size = new System.Drawing.Size(0, 21);
            this.name_ctrl.TabIndex = 10;
            // 
            // gender_ctrl
            // 
            this.gender_ctrl.AutoSize = true;
            this.gender_ctrl.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.gender_ctrl.Location = new System.Drawing.Point(570, 105);
            this.gender_ctrl.Name = "gender_ctrl";
            this.gender_ctrl.Size = new System.Drawing.Size(0, 21);
            this.gender_ctrl.TabIndex = 11;
            // 
            // label_man
            // 
            this.label_man.AutoSize = true;
            this.label_man.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.label_man.Location = new System.Drawing.Point(628, 105);
            this.label_man.Name = "label_man";
            this.label_man.Size = new System.Drawing.Size(0, 21);
            this.label_man.TabIndex = 12;
            // 
            // persnr_ctrl
            // 
            this.persnr_ctrl.AutoSize = true;
            this.persnr_ctrl.Font = new System.Drawing.Font("Segoe UI Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.persnr_ctrl.Location = new System.Drawing.Point(570, 152);
            this.persnr_ctrl.Name = "persnr_ctrl";
            this.persnr_ctrl.Size = new System.Drawing.Size(0, 21);
            this.persnr_ctrl.TabIndex = 14;
            // 
            // label4
            // 
            this.label4.AllowDrop = true;
            this.label4.AutoSize = true;
            this.label4.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.label4.Font = new System.Drawing.Font("Vivaldi", 18F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point);
            this.label4.Location = new System.Drawing.Point(227, 54);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(327, 118);
            this.label4.TabIndex = 15;
            this.label4.Text = "Enter your name and Numbers \r\nI\'ll guess your gender & if you\'re lying\r\nI will kn" +
    "ow!\r\n\r\n";
            this.label4.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            // 
            // Form1
            // 
            this.AllowDrop = true;
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(893, 524);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.persnr_ctrl);
            this.Controls.Add(this.label_man);
            this.Controls.Add(this.gender_ctrl);
            this.Controls.Add(this.name_ctrl);
            this.Controls.Add(this.text_number);
            this.Controls.Add(this.text_lastname);
            this.Controls.Add(this.text_firstname);
            this.Controls.Add(this.btn_quit);
            this.Controls.Add(this.list_info);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn_clear);
            this.Controls.Add(this.btn_add);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "Form1";
            this.Text = "Guessing game";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button btn_add;
        private Button btn_clear;
        private Label label1;
        private Label label2;
        private Label label3;
        private ListBox list_info;
        private Button btn_quit;
        private TextBox text_firstname;
        private TextBox text_lastname;
        private TextBox text_number;
        private Label name_ctrl;
        private Label gender_ctrl;
        private Label label_man;
        private Label persnr_ctrl;
        private Label label4;
    }
}