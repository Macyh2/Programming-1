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
        self._label5.Size = System.Drawing.Size(140, 28)
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
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Indigo
        self.ClientSize = System.Drawing.Size(475, 533)
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
        self.ResumeLayout(False)
        self.PerformLayout()

