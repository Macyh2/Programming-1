import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(291, 15)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(443, 35)
        self._textBox1.TabIndex = 1
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Teal
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Location = System.Drawing.Point(754, 8)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(163, 102)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Teal
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Location = System.Drawing.Point(754, 125)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(163, 102)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Teal
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._button3.Location = System.Drawing.Point(754, 244)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(163, 102)
        self._button3.TabIndex = 4
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(21, 15)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(264, 34)
        self._label1.TabIndex = 5
        self._label1.Text = "Enter your test value:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(20, 358)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(509, 66)
        self._label2.TabIndex = 6
        self._label2.Text = "The sum of even integers"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(371, 346)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(158, 66)
        self._label3.TabIndex = 7
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(535, 358)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(174, 66)
        self._label4.TabIndex = 8
        self._label4.Text = "is >= to"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(683, 346)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(174, 66)
        self._label5.TabIndex = 9
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Linen
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(21, 72)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(712, 273)
        self._label6.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.NavajoWhite
        self.ClientSize = System.Drawing.Size(1027, 418)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Program 152b"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
        self._label5.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()
       
    def Button1Click(self, sender, e):
        numb = self._textBox1.Text
        heading = "Even Integer\t\tSum"
        self._listBox1.Items.Add(heading)
        
        self._label5.Text = str(numb)
        self._label3.Text = "0" + "..." + str(numb)
        
        even_num = 0
        sum = 0
        
        while sum < numb:
        	even_num = even_num + 2
        	sum = sum + even_num
        	line = even_num + "\t\t" + sum
        	return self._label6.Item.Add(line)
