namespace inlupp3v1
{
    partial class MainMenu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_start = new System.Windows.Forms.Button();
            this.btn_exit = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_start
            // 
            this.btn_start.Font = new System.Drawing.Font("Stencil", 20.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.btn_start.Location = new System.Drawing.Point(117, 113);
            this.btn_start.Name = "btn_start";
            this.btn_start.Size = new System.Drawing.Size(227, 162);
            this.btn_start.TabIndex = 0;
            this.btn_start.Text = "START\r\n";
            this.btn_start.UseVisualStyleBackColor = true;
            this.btn_start.Click += new System.EventHandler(this.LoadGame);
            // 
            // btn_exit
            // 
            this.btn_exit.Font = new System.Drawing.Font("Stencil", 20.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.btn_exit.Location = new System.Drawing.Point(479, 113);
            this.btn_exit.Name = "btn_exit";
            this.btn_exit.Size = new System.Drawing.Size(227, 162);
            this.btn_exit.TabIndex = 1;
            this.btn_exit.Text = "EXIT\r\n";
            this.btn_exit.UseVisualStyleBackColor = true;
            this.btn_exit.Click += new System.EventHandler(this.btn_exit_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Stencil", 18F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.label1.Location = new System.Drawing.Point(117, 57);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(244, 29);
            this.label1.TabIndex = 2;
            this.label1.Text = "Dare you enter?...";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Stencil", 18F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point);
            this.label2.Location = new System.Drawing.Point(340, 310);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(366, 29);
            this.label2.TabIndex = 3;
            this.label2.Text = "Or just leave while you can";
            // 
            // MainMenu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn_exit);
            this.Controls.Add(this.btn_start);
            this.Name = "MainMenu";
            this.Text = "MainMenu";
            this.Load += new System.EventHandler(this.MainMenu_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button btn_start;
        private Button btn_exit;
        private Label label1;
        private Label label2;
    }
}