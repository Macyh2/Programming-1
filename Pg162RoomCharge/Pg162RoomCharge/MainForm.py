import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
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
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label24 = System.Windows.Forms.Label()
        self._label25 = System.Windows.Forms.Label()
        self._label26 = System.Windows.Forms.Label()
        self._label27 = System.Windows.Forms.Label()
        self._label28 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Mistral", 72, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(188, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(261, 99)
        self._label1.TabIndex = 0
        self._label1.Text = "Hotel"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(14, 111)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(281, 39)
        self._label4.TabIndex = 3
        self._label4.Text = "Room Information"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(372, 111)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(295, 39)
        self._label5.TabIndex = 4
        self._label5.Text = "Aditional Charges"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label6.Location = System.Drawing.Point(58, 170)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(91, 39)
        self._label6.TabIndex = 5
        self._label6.Text = "Nights:"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label7.Location = System.Drawing.Point(14, 209)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(191, 39)
        self._label7.TabIndex = 6
        self._label7.Text = "Nightly Charge:"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Location = System.Drawing.Point(15, 297)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(204, 39)
        self._label8.TabIndex = 7
        self._label8.Text = "Total Charges"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label9.Location = System.Drawing.Point(342, 170)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(157, 39)
        self._label9.TabIndex = 8
        self._label9.Text = "Room Service:"
        # 
        # label10
        # 
        self._label10.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label10.Location = System.Drawing.Point(372, 209)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(127, 39)
        self._label10.TabIndex = 9
        self._label10.Text = "Telephone:"
        # 
        # label11
        # 
        self._label11.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label11.Location = System.Drawing.Point(426, 248)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(67, 39)
        self._label11.TabIndex = 10
        self._label11.Text = "Misc:"
        # 
        # label12
        # 
        self._label12.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label12.Location = System.Drawing.Point(138, 368)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(181, 39)
        self._label12.TabIndex = 11
        self._label12.Text = "Room Charges:"
        # 
        # label13
        # 
        self._label13.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label13.Location = System.Drawing.Point(104, 416)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(206, 39)
        self._label13.TabIndex = 12
        self._label13.Text = "Aditional Charges:"
        # 
        # label14
        # 
        self._label14.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label14.Location = System.Drawing.Point(200, 465)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(119, 39)
        self._label14.TabIndex = 13
        self._label14.Text = "Subtotal:"
        # 
        # label16
        # 
        self._label16.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label16.Location = System.Drawing.Point(249, 514)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(61, 39)
        self._label16.TabIndex = 15
        self._label16.Text = "Tax:"
        # 
        # label17
        # 
        self._label17.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._label17.Location = System.Drawing.Point(144, 564)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(166, 39)
        self._label17.TabIndex = 16
        self._label17.Text = "Total Charges:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkRed
        self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self._button1.Font = System.Drawing.Font("Palatino Linotype", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(33, 622)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(205, 92)
        self._button1.TabIndex = 17
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkRed
        self._button2.Font = System.Drawing.Font("Palatino Linotype", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(247, 622)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(205, 92)
        self._button2.TabIndex = 18
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkRed
        self._button3.Font = System.Drawing.Font("Palatino Linotype", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(462, 622)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(205, 92)
        self._button3.TabIndex = 19
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label24
        # 
        self._label24.BackColor = System.Drawing.Color.White
        self._label24.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label24.Location = System.Drawing.Point(311, 368)
        self._label24.Name = "label24"
        self._label24.Size = System.Drawing.Size(280, 33)
        self._label24.TabIndex = 27
        # 
        # label25
        # 
        self._label25.BackColor = System.Drawing.Color.White
        self._label25.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label25.Location = System.Drawing.Point(311, 416)
        self._label25.Name = "label25"
        self._label25.Size = System.Drawing.Size(280, 33)
        self._label25.TabIndex = 28
        # 
        # label26
        # 
        self._label26.BackColor = System.Drawing.Color.White
        self._label26.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label26.Location = System.Drawing.Point(311, 465)
        self._label26.Name = "label26"
        self._label26.Size = System.Drawing.Size(280, 33)
        self._label26.TabIndex = 29
        # 
        # label27
        # 
        self._label27.BackColor = System.Drawing.Color.White
        self._label27.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label27.Location = System.Drawing.Point(311, 514)
        self._label27.Name = "label27"
        self._label27.Size = System.Drawing.Size(280, 33)
        self._label27.TabIndex = 30
        # 
        # label28
        # 
        self._label28.BackColor = System.Drawing.Color.LightGray
        self._label28.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label28.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label28.Location = System.Drawing.Point(311, 564)
        self._label28.Name = "label28"
        self._label28.Size = System.Drawing.Size(280, 33)
        self._label28.TabIndex = 31
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.IndianRed
        self._textBox1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(144, 167)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(175, 36)
        self._textBox1.TabIndex = 32
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.IndianRed
        self._textBox2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(182, 209)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(137, 36)
        self._textBox2.TabIndex = 33
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.IndianRed
        self._textBox3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(492, 164)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(191, 36)
        self._textBox3.TabIndex = 34
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.IndianRed
        self._textBox4.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(492, 206)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(191, 36)
        self._textBox4.TabIndex = 35
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.IndianRed
        self._textBox5.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(492, 248)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(191, 36)
        self._textBox5.TabIndex = 36
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Brown
        self.ClientSize = System.Drawing.Size(692, 728)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label28)
        self.Controls.Add(self._label27)
        self.Controls.Add(self._label26)
        self.Controls.Add(self._label25)
        self.Controls.Add(self._label24)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
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
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg162RoomCharge"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._label15.Text = ""
        self._label18.Text = ""
        self._label24.Text = ""
        self._label25.Text = ""
        self._label26.Text = ""
        self._label27.Text = ""
        self._label28.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        
        nights = float(self._textBox1.Text)
        nightlycharge = float(self._textBox2.Text)
        roomservice = float(self._textBox3.Text)
        phone = float(self._textBox4.Text)
        misc = float(self._textBox5.Text)
        
        roomcharge = nights * nightlycharge
        self._label24.Text = "$" + str(round(roomcharge, 2))
        addcharge = roomservice + misc + phone
        self._label25.Text = "$" + str(round(addcharge, 2))
        subtotal = roomcharge + addcharge
        self._label26.Text = "$" +str(round(subtotal, 2))
        tax = subtotal * 0.08
        self._label27.Text = "$" + str(round(tax, 2))
        totalcharge = subtotal + tax
        self._label28.Text = "$" + str(round(totalcharge, 2))
        
        
        