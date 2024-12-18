﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSteelBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label1.Location = System.Drawing.Point(414, 204)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(329, 60)
        self._label1.TabIndex = 0
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Location = System.Drawing.Point(47, 205)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(361, 59)
        self._label2.TabIndex = 1
        self._label2.Text = "Salary per pay period:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Location = System.Drawing.Point(57, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(361, 59)
        self._label3.TabIndex = 2
        self._label3.Text = "Pay periods per year:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Location = System.Drawing.Point(170, 43)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(214, 59)
        self._label4.TabIndex = 3
        self._label4.Text = "Anual Salary:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(414, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(329, 45)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(414, 121)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(329, 45)
        self._textBox2.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightGray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(26, 295)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(244, 95)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightGray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(286, 295)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(244, 95)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightGray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(545, 295)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(244, 95)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Navy
        self.ClientSize = System.Drawing.Size(817, 435)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg153SalaryCalc"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        salary = float(self._textBox1.Text)
        payperiods = float(self._textBox2.Text)
        salaryperperiod = salary / payperiods
        self._label1.Text = str(round(salaryperperiod, 2))
