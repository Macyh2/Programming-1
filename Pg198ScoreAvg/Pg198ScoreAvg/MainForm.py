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
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(8, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(396, 320)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter Test Scores"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(90, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(95, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "Score 1:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(90, 106)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(95, 34)
        self._label3.TabIndex = 2
        self._label3.Text = "Score 2:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(90, 153)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(95, 34)
        self._label4.TabIndex = 3
        self._label4.Text = "Score 3:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(78, 242)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(107, 34)
        self._label5.TabIndex = 4
        self._label5.Text = "Average:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.PaleVioletRed
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(175, 242)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(163, 34)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleVioletRed
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(8, 332)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(128, 102)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PaleVioletRed
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(142, 332)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(128, 102)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PaleVioletRed
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(276, 332)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(128, 102)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.LightPink
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(175, 62)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(163, 31)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.LightPink
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(175, 106)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(163, 31)
        self._textBox2.TabIndex = 10
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.LightPink
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(175, 150)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(163, 31)
        self._textBox3.TabIndex = 11
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(32, 284)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(347, 31)
        self._label7.TabIndex = 12
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightPink
        self.ClientSize = System.Drawing.Size(412, 436)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg198ScoreAvg"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.Text = ""

    def Button1Click(self, sender, e):
        score1 = float(self._textBox1.Text)
        score2 = float(self._textBox2.Text)
        score3 = float(self._textBox3.Text)
        
        average = (score1 + score2 + score3) / 3
        self._label6.Text = str(round(average, 2))
        
       # if average > 95:
       #     return self._label7.Text = "Congradulations! Great Job!"

    def Button3Click(self, sender, e):
        Application.Exit()