import math
import System.Drawing
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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(100, 39)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(177, 100)
        self._label1.TabIndex = 0
        self._label1.Text = "Integer A"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(100, 139)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(177, 100)
        self._label2.TabIndex = 1
        self._label2.Text = "Integer B"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(100, 239)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(177, 100)
        self._label3.TabIndex = 2
        self._label3.Text = "Integer C"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.PaleGoldenrod
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(300, 68)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(534, 38)
        self._textBox1.TabIndex = 3
        self._textBox1.TextChanged
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.PaleGoldenrod
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(300, 167)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(534, 38)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.PaleGoldenrod
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(300, 267)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(534, 38)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(100, 339)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(177, 100)
        self._label4.TabIndex = 6
        self._label4.Text = "Roots"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.SeaShell
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(306, 342)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(514, 45)
        self._label5.TabIndex = 7
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Location = System.Drawing.Point(12, 489)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(287, 110)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Location = System.Drawing.Point(319, 489)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(287, 110)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Location = System.Drawing.Point(625, 489)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(287, 110)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.SeaShell
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(306, 394)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(514, 45)
        self._label6.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Thistle
        self.ClientSize = System.Drawing.Size(943, 643)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        c = int(self._textBox3.Text)
        rootpos = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
        rootneg = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
        self._label5.Text = str(rootpos)
        self._label6.Text = str(rootneg)
        
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()