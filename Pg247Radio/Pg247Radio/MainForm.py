import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(66, 107)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(139, 54)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = """Choice 1
"""
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(66, 167)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(139, 54)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(66, 227)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(139, 54)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(43, 71)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(189, 33)
        self._label1.TabIndex = 3
        self._label1.Text = "Radio Buttons"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(406, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(175, 33)
        self._label2.TabIndex = 4
        self._label2.Text = "Check Boxes"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(108, 314)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(214, 87)
        self._label3.TabIndex = 5
        self._label3.Text = "Calculate"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(353, 314)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(214, 87)
        self._label5.TabIndex = 7
        self._label5.Text = "Exit"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label5.Click += self.Label5Click
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(405, 113)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(176, 44)
        self._checkBox1.TabIndex = 8
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(405, 173)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(176, 44)
        self._checkBox2.TabIndex = 9
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(405, 233)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(176, 44)
        self._checkBox3.TabIndex = 10
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self.ClientSize = System.Drawing.Size(682, 446)
        self.Controls.Add(self._checkBox3)
        self.Controls.Add(self._checkBox2)
        self.Controls.Add(self._checkBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "MainForm"
        self.Text = "Pg247Radio"
        self.ResumeLayout(False)


    def Label3Click(self, sender, e):
        if self._radioButton1.Checked == True:
             MessageBox.Show("You selected choice 1")
        elif self._radioButton2.Checked == True:
             MessageBox.Show("You selected choice 2")
        elif self._radioButton3.Checked == True:
             MessageBox.Show("You selected choice 3")
             
        if self._checkBox1.Checked == True:
            MessageBox.Show("and choice 4")
        if self._checkBox2.Checked == True:
            MessageBox.Show("and choice 5")
        if self._checkBox3.Checked == True:
            MessageBox.Show("and choice 6")

    def Label5Click(self, sender, e):
        Application.Exit()