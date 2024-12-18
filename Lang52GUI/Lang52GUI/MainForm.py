﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(398, 63)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(378, 47)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(398, 116)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(378, 47)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(208, 64)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(140, 46)
        self._label1.TabIndex = 2
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(208, 116)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(140, 46)
        self._label2.TabIndex = 3
        self._label2.Text = "Width:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label3.Location = System.Drawing.Point(399, 246)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(376, 57)
        self._label3.TabIndex = 4
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.LightBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._label4.Location = System.Drawing.Point(400, 312)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(376, 57)
        self._label4.TabIndex = 5
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(208, 246)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(140, 46)
        self._label5.TabIndex = 6
        self._label5.Text = "Area:"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(208, 312)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(186, 46)
        self._label6.TabIndex = 7
        self._label6.Text = "Perimeter:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button1.Location = System.Drawing.Point(80, 404)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(256, 113)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button2.Location = System.Drawing.Point(364, 404)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(256, 113)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._button3.Location = System.Drawing.Point(645, 404)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(256, 113)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Teal
        self.ClientSize = System.Drawing.Size(965, 560)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.ForeColor = System.Drawing.SystemColors.ControlLight
        self.Name = "MainForm"
        self.Text = "Lang52GUI"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width  = int(self._textBox2.Text)
        area   = length * width
        perim  = 2 * length + 2 * width
        self._label3.Text = str(area)
        self._label4.Text = str(perim)
        # + - * / %     ** pow     // divide & round down
        # int (Integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (String): a string of text

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()