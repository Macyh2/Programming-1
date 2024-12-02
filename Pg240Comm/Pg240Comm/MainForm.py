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
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 21)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(233, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "Sales for the month:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(3, 66)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(275, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "Advanced pay awarded:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(29, 163)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(233, 45)
        self._label3.TabIndex = 2
        self._label3.Text = "Commission Rate:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(82, 208)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(233, 45)
        self._label4.TabIndex = 3
        self._label4.Text = "Commission:"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(131, 253)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(233, 45)
        self._label5.TabIndex = 4
        self._label5.Text = "Net Pay:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(234, 163)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(233, 32)
        self._label6.TabIndex = 5
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(234, 208)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(233, 32)
        self._label7.TabIndex = 6
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.Black
        self._label8.Location = System.Drawing.Point(234, 253)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(233, 32)
        self._label8.TabIndex = 7
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(234, 18)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(232, 35)
        self._textBox1.TabIndex = 8
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(272, 63)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(194, 35)
        self._textBox2.TabIndex = 9
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.LightSteelBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(3, 317)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(153, 105)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.LightSteelBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(162, 317)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(153, 105)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.LightSteelBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(321, 317)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(153, 105)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MidnightBlue
        self.ClientSize = System.Drawing.Size(479, 444)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg240Comm"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._laebl6.Text = ""
        self._label7.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        sales = float(self._textBox1.Text)
        advancedpay = float(self._textBox2.Text)
        
        if sales < 9999:
            commissionrate = 5
            print(self._label6.Text = str(commissionrate) + "%")
        elif sales > 10000 and sales < 14999:
            commissionrate = 10
            print(self._label6.Text = str(commissionrate) + "%")
        elif sales > 15000 and sales < 17999:
            commissionrate = 12
            print(self._label6.Text = str(commissionrate) + "%")
        elif sales > 18000 and sales < 21999:
            commissionrate = 14
            print(self._label6.Text = str(commissionrate) + "%")
        else sales > 22000:
            commissionrate = 16
            print(self._label6.Text = str(commissionrate) + "%")
        
        commission = (commissionrate*0.01) * sales
        self._label7.Text = "$" + str(round(commission, 2))
        
        netpay = commission - advancedpay
        self._label8.Text = "$" + str(round(netpay, 2))