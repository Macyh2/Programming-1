﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LemonChiffon
        self._label1.Font = System.Drawing.Font("Lucida Bright", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(129, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(709, 354)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LemonChiffon
        self._button1.Font = System.Drawing.Font("Lucida Bright", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(80, 422)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(265, 87)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LemonChiffon
        self._button2.Font = System.Drawing.Font("Lucida Bright", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(351, 422)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(265, 87)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LemonChiffon
        self._button3.Font = System.Drawing.Font("Lucida Bright", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(622, 422)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(265, 87)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SandyBrown
        self.ClientSize = System.Drawing.Size(968, 542)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Your Scheldule"
        self.ResumeLayout(False)



    def Button1Click(self, sender, e):
        self._label1.Text = "1. AP Physics \n 2. Ceramics \n 3. AP Spanish \n 4. Intro to Logic \n 5. AP Lang \n 6. AP Calc BC \n 7. AP Bio \n 8. Computer Programming"

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()