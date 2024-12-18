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
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(51, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(146, 43)
        self._label1.TabIndex = 0
        self._label1.Text = "Tickets Sold"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(331, 25)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(211, 43)
        self._label2.TabIndex = 1
        self._label2.Text = "Revenue Generated"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightYellow
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(40, 68)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(261, 245)
        self._label3.TabIndex = 2
        self._label3.Text = "Enter the number of tickets sold"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightYellow
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(51, 132)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(83, 25)
        self._label4.TabIndex = 3
        self._label4.Text = "Class A:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightYellow
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(51, 175)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(83, 25)
        self._label5.TabIndex = 4
        self._label5.Text = "Class B:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightYellow
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(51, 221)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(83, 25)
        self._label6.TabIndex = 5
        self._label6.Text = "Class C:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(431, 185)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(185, 25)
        self._label10.TabIndex = 15
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(431, 147)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(185, 25)
        self._label11.TabIndex = 14
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(431, 111)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(185, 25)
        self._label12.TabIndex = 13
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.LightYellow
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(342, 185)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(83, 25)
        self._label13.TabIndex = 12
        self._label13.Text = "Class C:"
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.LightYellow
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(342, 147)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(83, 25)
        self._label14.TabIndex = 11
        self._label14.Text = "Class B:"
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.LightYellow
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.Location = System.Drawing.Point(342, 111)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(83, 25)
        self._label15.TabIndex = 10
        self._label15.Text = "Class A:"
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.LightYellow
        self._label16.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.Location = System.Drawing.Point(321, 68)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(308, 245)
        self._label16.TabIndex = 9
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.LightYellow
        self._label17.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.Location = System.Drawing.Point(331, 239)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(157, 25)
        self._label17.TabIndex = 16
        self._label17.Text = "Total Revenue:"
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.DarkSeaGreen
        self._label18.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.Location = System.Drawing.Point(471, 239)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(145, 25)
        self._label18.TabIndex = 17
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightGray
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(25, 341)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(202, 72)
        self._button1.TabIndex = 18
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightGray
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(233, 341)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(202, 72)
        self._button2.TabIndex = 19
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightGray
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(441, 341)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(202, 72)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.DarkSeaGreen
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(140, 128)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(108, 29)
        self._textBox1.TabIndex = 21
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.DarkSeaGreen
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(140, 172)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(108, 29)
        self._textBox2.TabIndex = 22
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.DarkSeaGreen
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(140, 218)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(108, 29)
        self._textBox3.TabIndex = 23
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSeaGreen
        self.ClientSize = System.Drawing.Size(667, 433)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StadiumSeating"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label18.Text = ""
        self._label12.Text = ""
        self._label11.Text = ""
        self._label10.Text = ""

    def Button1Click(self, sender, e):
        ClassA = float(self._textBox1.Text)
        ClassB = float(self._textBox2.Text)
        ClassC = float(self._textBox3.Text)
        
        classacost = ClassA * 15
        self._label12.Text = "$" + str(round(classacost, 2))
        
        classbcost = ClassB * 12
        self._label11.Text = "$" + str(round(classbcost, 2))
        
        classccost = ClassC * 9
        self._label10.Text = "$" + str(round(classccost, 2))
        
        totalrev = classacost + classbcost + classccost
        self._label18.Text = "$" + str(round(totalrev, 2))

    def Button3Click(self, sender, e):
        Application.Exit()