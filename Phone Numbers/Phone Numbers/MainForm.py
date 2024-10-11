import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Wheat
        self._label1.Font = System.Drawing.Font("Cooper Black", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(150, 55)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(207, 116)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Wheat
        self._button1.Font = System.Drawing.Font("Cooper Black", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(50, 360)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(284, 101)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Wheat
        self._button2.Font = System.Drawing.Font("Cooper Black", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(349, 360)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(284, 101)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Wheat
        self._button3.Font = System.Drawing.Font("Cooper Black", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(639, 360)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(284, 101)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Wheat
        self._label2.Font = System.Drawing.Font("Cooper Black", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(393, 55)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(207, 116)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Wheat
        self._label3.Font = System.Drawing.Font("Cooper Black", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(639, 55)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(207, 116)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Wheat
        self._label4.Font = System.Drawing.Font("Cooper Black", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(256, 203)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(207, 116)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Wheat
        self._label5.Font = System.Drawing.Font("Cooper Black", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(548, 203)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(207, 116)
        self._label5.TabIndex = 7
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self.ClientSize = System.Drawing.Size(966, 543)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Phone Numbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Sweet Aroma Restaurant - (252)728-6878"
        self._label2.Text = "Cheescake Factory - (608)824-2370"
        self._label3.Text = "Old Fashioned Bakery - (608)365-6461"
        self._label4.Text = "Beef-A-Roo - (815)633-6585"
        self._label5.Text = "The Butterfly Club - (608)362-8577"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()