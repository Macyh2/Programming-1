import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.MistyRose
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(303, 59)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(451, 38)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.MistyRose
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(303, 103)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(451, 38)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.MistyRose
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(303, 147)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(451, 38)
        self._textBox3.TabIndex = 2
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.MistyRose
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(303, 191)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(451, 38)
        self._textBox4.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(145, 62)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(152, 42)
        self._label1.TabIndex = 4
        self._label1.Text = "Digit 1:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(145, 99)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(152, 42)
        self._label2.TabIndex = 5
        self._label2.Text = "Digit 2:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(145, 147)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(152, 41)
        self._label3.TabIndex = 6
        self._label3.Text = "Digit 3:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(145, 188)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(152, 42)
        self._label4.TabIndex = 7
        self._label4.Text = "Digit 4:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightSalmon
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(303, 294)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(450, 61)
        self._label5.TabIndex = 8
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightSalmon
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(303, 375)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(450, 61)
        self._label6.TabIndex = 9
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(129, 294)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(152, 61)
        self._label7.TabIndex = 10
        self._label7.Text = "Sum"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(129, 375)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(152, 61)
        self._label8.TabIndex = 11
        self._label8.Text = "Average"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(90, 471)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(227, 81)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(375, 471)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(227, 81)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(657, 471)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(227, 81)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.IndianRed
        self.ClientSize = System.Drawing.Size(937, 583)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Lang54b"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        digit1 = int(self._textBox1.Text)
        digit2 = int(self._textBox2.Text)
        digit3 = int(self._textBox3.Text)
        digit4 = int(self._textBox4.Text)
        Sum    = digit1 + digit2 + digit3 + digit4
        average= Sum/4
        self._label5.Text = str(Sum)
        self._label6.Text = str(average)
        # + - * / %     ** pow     // divide & round down
        # int (Integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (String): a string of text

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()