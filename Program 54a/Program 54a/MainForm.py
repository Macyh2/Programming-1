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
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Tan
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(57, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(179, 66)
        self._label1.TabIndex = 0
        self._label1.Text = "Pick a Car:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Tan
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(57, 201)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(179, 72)
        self._label2.TabIndex = 1
        self._label2.Text = "Miles:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Tan
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(57, 287)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(179, 72)
        self._label3.TabIndex = 2
        self._label3.Text = "Gallons:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Tan
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(57, 370)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(179, 72)
        self._label4.TabIndex = 3
        self._label4.Text = "MPG:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MistyRose
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(242, 201)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(471, 72)
        self._label5.TabIndex = 4
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MistyRose
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(242, 287)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(471, 72)
        self._label6.TabIndex = 5
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MistyRose
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(242, 370)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(471, 72)
        self._label7.TabIndex = 6
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PeachPuff
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(57, 96)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(209, 87)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PeachPuff
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(284, 96)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(215, 87)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PeachPuff
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(521, 96)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(192, 87)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # comboBox1
        # 
        self._comboBox1.BackColor = System.Drawing.Color.MistyRose
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"]))
        self._comboBox1.Location = System.Drawing.Point(242, 16)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(471, 47)
        self._comboBox1.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSalmon
        self.ClientSize = System.Drawing.Size(764, 451)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Program 54a"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        mile = 1
        gallons = 1
        car = self._comboBox1.Text
        
        # TODO: Repeat for all 4 cars
        if car == "1970 VW Bug":
            miles = 286
            gallons = 9
        # elif car == "second car":
            # miles = ...
            # gallons = ...
        elif car == "1979 Firebird":
            miles = 412
            gallons = 40
        elif car == "1980 Subaru":
            miles = 361
            gallons = 18
        elif car == "1975 Cutlass":
            miles = 161
            gallons = 11
        else:
            MessageBox.Show("Invalid car!")
            return # Prevent the rest of the code from running
        
        mpg = miles / float(gallons)
        mpg = round(mpg, 1)
        
        self._label7.Text = str(mpg)
        
        

    def Button2Click(self, sender, e):
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()