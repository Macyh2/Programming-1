import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(99, 62)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(292, 39)
        self._label1.TabIndex = 0
        self._label1.Text = "Radius of Circle:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(411, 57)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(393, 49)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(124, 257)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(292, 54)
        self._label2.TabIndex = 2
        self._label2.Text = "Circumfrence:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(411, 257)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(418, 64)
        self._label3.TabIndex = 3
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.PaleGoldenrod
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(411, 375)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(418, 64)
        self._label4.TabIndex = 4
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(113, 375)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(292, 54)
        self._label5.TabIndex = 5
        self._label5.Text = "Area of a Circle:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gainsboro
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(93, 492)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(247, 81)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gainsboro
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(368, 492)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(247, 81)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gainsboro
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(636, 492)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(247, 81)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumAquamarine
        self.ClientSize = System.Drawing.Size(955, 633)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Lang52c GUI"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        radius = float(self._textBox1.Text)
        pi = 3.14159
        circumfrence = 2 * pi * radius
        area = pi * radius**2
        circumfrence = round(circumfrence, 3)
        area = round(area, 3)
        self._label3.Text = str(circumfrence)
        self._label4.Text = str(area)
        # + - * / %     ** pow      // divide & round down
        # int (Integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (String): a string of text
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()