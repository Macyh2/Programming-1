import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(66, 472)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(192, 108)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(337, 472)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(192, 108)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(601, 472)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(192, 108)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(88, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(199, 67)
        self._label1.TabIndex = 3
        self._label1.Text = "Kilowatts:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(293, 25)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(421, 35)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(88, 169)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(199, 67)
        self._label2.TabIndex = 5
        self._label2.Text = "Surcharge:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(88, 236)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(199, 67)
        self._label3.TabIndex = 6
        self._label3.Text = "Citytax:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(2, 402)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(285, 67)
        self._label4.TabIndex = 7
        self._label4.Text = "Total After November 2:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.LightGray
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(293, 178)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(421, 49)
        self._label5.TabIndex = 8
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.LightGray
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(293, 245)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(421, 49)
        self._label6.TabIndex = 9
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.PeachPuff
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(293, 408)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(421, 49)
        self._label7.TabIndex = 10
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.PeachPuff
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(293, 336)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(421, 49)
        self._label8.TabIndex = 11
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(88, 335)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(199, 67)
        self._label9.TabIndex = 12
        self._label9.Text = "Total:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(88, 91)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(199, 67)
        self._label10.TabIndex = 13
        self._label10.Text = "Base Rate:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.LightSteelBlue
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(317, 91)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(104, 49)
        self._label11.TabIndex = 14
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.LightSteelBlue
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(411, 91)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(75, 49)
        self._label12.TabIndex = 15
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.LightSteelBlue
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(456, 92)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(86, 49)
        self._label13.TabIndex = 16
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.LightGray
        self._label14.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(594, 91)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(120, 49)
        self._label14.TabIndex = 17
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightSteelBlue
        self.ClientSize = System.Drawing.Size(846, 591)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        kilowatts = float(self._textBox1.Text)
        self._label11.Text = str(kilowatts)
        self._label12.Text = "@$"
        self._label13.Text = "0.0475"
        baserate = kilowatts * 0.0475
        baserate = round(baserate, 2)
        self._label14.Text = str(baserate)
        surcharge = baserate * 0.1
        surcharge = round(surcharge, 2)
        self._label5.Text = str(surcharge)
        citytax = baserate * 0.03
        citytax = round(citytax, 2)
        self._label6.Text = str(citytax)
        total = baserate + surcharge + citytax
        latetotal = (total * 0.04) + total
        latetotal = round(latetotal, 2)
        self._label7.Text = str(latetotal)

        self._label8.Text = str(total)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._label13.Text = ""
        self._label14.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label8.Text = ""
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()