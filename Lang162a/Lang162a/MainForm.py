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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(60, 46)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(213, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter a Number:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(25, 123)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(166, 33)
        self._label2.TabIndex = 1
        self._label2.Text = "The value of"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(186, 123)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(56, 33)
        self._label3.TabIndex = 2
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(239, 123)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(34, 33)
        self._label4.TabIndex = 3
        self._label4.Text = "is"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(269, 123)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(225, 33)
        self._label5.TabIndex = 4
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(25, 169)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(143, 67)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(174, 169)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 67)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(323, 169)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 67)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(269, 43)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(197, 38)
        self._textBox1.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self.ClientSize = System.Drawing.Size(506, 248)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Lang162a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label5.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        num = float(self._textBox1.Text)
        self._label3.Text = str(round(num, 2)) + "!"
        
        product = num[1] * num[-1]
        
        while product < num: