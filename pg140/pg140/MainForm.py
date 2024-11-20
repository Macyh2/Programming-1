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
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self._button8 = System.Windows.Forms.Button()
        self._button9 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(10, 43)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(118, 44)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(10, 230)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(118, 44)
        self._label2.TabIndex = 1
        self._label2.Text = "Number 2:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(10, 126)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(118, 44)
        self._label3.TabIndex = 2
        self._label3.Text = "Operation:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(40, 306)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(79, 44)
        self._label4.TabIndex = 3
        self._label4.Text = "Result:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(157, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(333, 31)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(157, 227)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(333, 31)
        self._textBox2.TabIndex = 5
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(151, 123)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(338, 46)
        self._label5.TabIndex = 6
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightGray
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(152, 304)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(338, 46)
        self._label6.TabIndex = 7
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(513, 22)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(89, 65)
        self._button1.TabIndex = 8
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(608, 22)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(89, 65)
        self._button2.TabIndex = 9
        self._button2.Text = "-"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(513, 93)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(89, 65)
        self._button3.TabIndex = 10
        self._button3.Text = "^"
        self._button3.UseVisualStyleBackColor = True
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(703, 22)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(89, 65)
        self._button4.TabIndex = 11
        self._button4.Text = "*"
        self._button4.UseVisualStyleBackColor = True
        # 
        # button5
        # 
        self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(608, 93)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(89, 65)
        self._button5.TabIndex = 12
        self._button5.Text = "/"
        self._button5.UseVisualStyleBackColor = True
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(703, 93)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(89, 65)
        self._button6.TabIndex = 13
        self._button6.Text = "//"
        self._button6.UseVisualStyleBackColor = True
        # 
        # button7
        # 
        self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button7.Location = System.Drawing.Point(581, 180)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(144, 65)
        self._button7.TabIndex = 14
        self._button7.Text = "Mod"
        self._button7.UseVisualStyleBackColor = True
        # 
        # button8
        # 
        self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button8.Location = System.Drawing.Point(513, 268)
        self._button8.Name = "button8"
        self._button8.Size = System.Drawing.Size(275, 65)
        self._button8.TabIndex = 15
        self._button8.Text = "Clear"
        self._button8.UseVisualStyleBackColor = True
        self._button8.Click += self.Button8Click
        # 
        # button9
        # 
        self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 30, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button9.Location = System.Drawing.Point(513, 353)
        self._button9.Name = "button9"
        self._button9.Size = System.Drawing.Size(275, 65)
        self._button9.TabIndex = 16
        self._button9.Text = "Exit"
        self._button9.UseVisualStyleBackColor = True
        self._button9.Click += self.Button9Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkOliveGreen
        self.ClientSize = System.Drawing.Size(800, 430)
        self.Controls.Add(self._button9)
        self.Controls.Add(self._button8)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg140"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button8Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button9Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        num1 = self._textBox1.Text
        num2 = self._textBox2.Text
        
        sum = str(num1 + num2)
        
        self._label5.Text = "+"
        self._label6.Text = str(sum)
        