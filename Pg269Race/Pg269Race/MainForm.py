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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(42, 69)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(99, 28)
        self._label1.TabIndex = 0
        self._label1.Text = "Runner 1:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(42, 118)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(99, 28)
        self._label2.TabIndex = 1
        self._label2.Text = "Runner 2:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(42, 165)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(99, 28)
        self._label3.TabIndex = 2
        self._label3.Text = "Runner 3:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(179, 26)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(66, 28)
        self._label4.TabIndex = 3
        self._label4.Text = "Name"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(323, 26)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(172, 28)
        self._label5.TabIndex = 4
        self._label5.Text = "Finishing Time"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(147, 66)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(140, 30)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(147, 118)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(140, 30)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(147, 165)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(140, 30)
        self._textBox3.TabIndex = 7
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(323, 66)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(140, 30)
        self._textBox4.TabIndex = 8
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(323, 115)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(140, 30)
        self._textBox5.TabIndex = 9
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(323, 165)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(140, 30)
        self._textBox6.TabIndex = 10
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._label11)
        self._groupBox1.Controls.Add(self._label10)
        self._groupBox1.Controls.Add(self._label9)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._groupBox1.Location = System.Drawing.Point(34, 210)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(428, 197)
        self._groupBox1.TabIndex = 11
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Race Results"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Location = System.Drawing.Point(68, 39)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(116, 28)
        self._label6.TabIndex = 12
        self._label6.Text = "First Place"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.Location = System.Drawing.Point(68, 88)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(143, 28)
        self._label7.TabIndex = 13
        self._label7.Text = "Second Place"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Location = System.Drawing.Point(68, 134)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(116, 28)
        self._label8.TabIndex = 14
        self._label8.Text = "Third Place"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.MediumPurple
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(222, 39)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(153, 28)
        self._label9.TabIndex = 15
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.MediumPurple
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(222, 88)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(153, 28)
        self._label10.TabIndex = 16
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.MediumPurple
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(222, 134)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(153, 28)
        self._label11.TabIndex = 17
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(33, 434)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(137, 67)
        self._button1.TabIndex = 12
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(179, 434)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(137, 67)
        self._button2.TabIndex = 13
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(322, 434)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(137, 67)
        self._button3.TabIndex = 14
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Indigo
        self.ClientSize = System.Drawing.Size(498, 533)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg269Race"
        self._groupBox1.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        name1 = str(self._textBox1.Text)
        name2 = str(self._textBox2.Text)
        name3 = str(self._textBox3.Text)
        time1 = float(self._textBox4.Text)
        time2 = float(self._textBox5.Text)
        time3 = float(self._textBox6.Text)
        
        if time1 > time2 and time3:
            return self._label9.Text = str(name1)