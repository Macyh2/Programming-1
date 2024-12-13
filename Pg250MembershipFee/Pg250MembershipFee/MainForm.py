import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._radioButton4)
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Location = System.Drawing.Point(51, 27)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(273, 178)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Type of Membership"
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._textBox1)
        self._groupBox2.Controls.Add(self._label1)
        self._groupBox2.Location = System.Drawing.Point(51, 222)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(273, 111)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Membership Length"
        # 
        # groupBox3
        # 
        self._groupBox3.Controls.Add(self._checkBox3)
        self._groupBox3.Controls.Add(self._checkBox2)
        self._groupBox3.Controls.Add(self._checkBox1)
        self._groupBox3.Location = System.Drawing.Point(396, 27)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(273, 178)
        self._groupBox3.TabIndex = 1
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Options"
        # 
        # groupBox4
        # 
        self._groupBox4.Controls.Add(self._label5)
        self._groupBox4.Controls.Add(self._label4)
        self._groupBox4.Controls.Add(self._label3)
        self._groupBox4.Controls.Add(self._label2)
        self._groupBox4.Location = System.Drawing.Point(396, 231)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(273, 111)
        self._groupBox4.TabIndex = 2
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Membership Fees"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Silver
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(55, 355)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(230, 94)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Silver
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(291, 355)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(230, 94)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Silver
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(527, 355)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(230, 94)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(26, 24)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(214, 30)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Standard Adult"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(26, 60)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(241, 30)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child (12 and Under)"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(26, 96)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(214, 30)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Students"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(26, 132)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(214, 30)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizens"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._checkBox1.Location = System.Drawing.Point(21, 32)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(230, 28)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Yoga"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._checkBox2.Location = System.Drawing.Point(21, 75)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(230, 28)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self._checkBox3.Location = System.Drawing.Point(21, 119)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(230, 28)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(16, 16)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(233, 53)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter the Number of Months:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(18, 16)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(233, 31)
        self._label2.TabIndex = 1
        self._label2.Text = "Monthly Fee:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(75, 62)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(74, 31)
        self._label3.TabIndex = 2
        self._label3.Text = "Totals:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(23, 72)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(226, 30)
        self._textBox1.TabIndex = 1
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(146, 16)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(121, 31)
        self._label4.TabIndex = 3
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(146, 63)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(121, 30)
        self._label5.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.MediumSeaGreen
        self.ClientSize = System.Drawing.Size(815, 467)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg250MembershipFee"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox2.PerformLayout()
        self._groupBox3.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        length = float(self._textBox1.Text)
        if self._radioButton1.Checked == True:
             price = 40
        elif self._radioButton2.Checked == True:
             price = 20
        elif self._radioButton3.Checked == True:
             price = 25
        elif self._radioButton3.Checked == True:
             price = 30
             
        if self._checkBox1.Checked == True:
           extra = 10
        if self._checkBox2.Checked == True:
            extra = 30
        if self._checkBox3.Checked == True:
            extra = 50
            
        if length <= 3:
            discount = 0
        elif length <= 6 and length >= 4:
            discount = 0.05
        elif length <= 9 and length >= 7:
            discount = 0.08
        elif length >= 10:
            discount = 0.1
            
        monthlyfee = (price - (price * discount) + extra)
        self._label4.Text = "$" + str(round(monthlyfee, 2))
        
        total = monthlyfee * length
        self._label5.Text = "$" + str(round(total,2))