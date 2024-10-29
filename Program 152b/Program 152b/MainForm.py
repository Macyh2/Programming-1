import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 29
        self._listBox1.Location = System.Drawing.Point(22, 56)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(713, 323)
        self._listBox1.TabIndex = 0
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
        self._button1.Location = System.Drawing.Point(755, 28)
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
        self._button2.Location = System.Drawing.Point(755, 145)
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
        self._button3.Location = System.Drawing.Point(755, 264)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(163, 102)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
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
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.NavajoWhite
        self.ClientSize = System.Drawing.Size(947, 403)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Program 152b"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()
       
    def Button1Click(self, sender, e):
        numb = self._textBox1.Text
        heading = "Even Integer\t\tSum"
        self._listBox1.Items.Add(heading)
        
        while num < numb:
            num + num-1
            