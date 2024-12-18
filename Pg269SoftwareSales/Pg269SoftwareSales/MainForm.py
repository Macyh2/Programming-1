import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label7 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.DarkSlateGray
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._groupBox1.Location = System.Drawing.Point(97, 17)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(430, 259)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Quantity Sold"
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(52, 44)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(154, 38)
        self._label1.TabIndex = 0
        self._label1.Text = "Package A:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(52, 102)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(154, 38)
        self._label2.TabIndex = 1
        self._label2.Text = "Package B:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(52, 165)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(164, 38)
        self._label3.TabIndex = 2
        self._label3.Text = "Package C:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(212, 41)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(199, 38)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(212, 99)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(199, 38)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(212, 162)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(199, 38)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(28, 294)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(285, 33)
        self._label4.TabIndex = 1
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(28, 327)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(285, 33)
        self._label5.TabIndex = 2
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(28, 360)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(285, 33)
        self._label6.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(406, 287)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(146, 50)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(334, 350)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 50)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(486, 350)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(146, 50)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(28, 393)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(285, 33)
        self._label7.TabIndex = 7
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkSlateGray
        self.ClientSize = System.Drawing.Size(644, 445)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg269SoftwareSales"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        packa = float(self._textBox1.Text)
        packb = float(self._textBox2.Text)
        packc = float(self._textBox3.Text)
        
        if packa >= 10 and packa <= 19:
            totala = packa * 99 
            totalaf = totala - (totala * 0.2)
            self._label4.Text = "Package A: $" + str(round(totalaf, 2))
        elif packa >= 20 and packa <= 49:
            totala = packa * 99
            totalaf = totala - (totala * 0.3)
            self._label4.Text = "Package A: $" + str(round(totalaf, 2))
        elif packa >= 50 and packa <= 99:
            totala = packa * 99
            totalaf = totala - (totala * 0.4)
            self._label4.Text = "Package A: $" + str(round(totalaf, 2))
        elif packa >= 100:
            totala = packa * 99
            totalaf = totala - (totala * 0.5)
            self._label4.Text = "Package A: $" + str(round(totalaf, 2))
            
        if packb >= 10 and packb <= 19:
            totalb = packb * 199
            totalbf = totalb - (totalb * 0.2)
            self._label5.Text = "Package B: $" + str(round(totalbf, 2))
        elif packb >= 20 and packb <= 49:
            totalb = packb * 199
            totalbf = totalb - (totalb * 0.3)
            self._label5.Text = "Package B: $" + str(round(totalbf, 2))
        elif packb >= 50 and packb <= 99:
            totalb = packb * 199
            totalbf = totalb - (totalb * 0.4)
            self._label5.Text = "Package B: $" + str(round(totalbf, 2))
        elif packb >= 100:
            totalb = packb * 199
            totalbf = totalb - (totalb * 0.5)
            self._label5.Text = "Package B: $" + str(round(totalbf, 2))
            
        if packc >= 10 and packc <= 19:
            totalc = packc * 199 - (packc * 0.2)
            totalcf = totalc - (totalc * 0.2)
            self._label6.Text = "Package C: $" + str(round(totalcf, 2))
        elif packc >= 20 and packc <= 49:
            totalc = packc * 199
            totalcf = totalc - (totalc * 0.3)
            self._label6.Text = "Package C: $" + str(round(totalcf, 2))
        elif packc >= 50 and packc <= 99:
            totalc = packc * 199
            totalcf = totalc - (totalc * 0.4)
            self._label6.Text = "Package C: $" + str(round(totalcf, 2))
        elif packc >= 100:
            totalc = packc * 199
            totalcf = totalc - (totalc * 0.5)
            self._label6.Text = "Package C: $" + str(round(totalcf, 2))
            
        grandtotal = totalaf + totalbf + totalcf
        self._label7.Text = "$" + str(round(grandtotal, 2))