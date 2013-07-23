import wx

class Example(wx.Frame):
	def __init__(self, parent, title):
		super(Example,self).__init__(parent,title=title,size=(260,180))

		self.InitUI()
		self.Centre()
		self.Show()
	
	def InitUI(self):
		panel=wx.Panel(self)
		panel.SetBackgroundColour('#4f5049')
		vbox=wx.BoxSizer(wx.VERTICAL)
	
		st1=wx.StaticText(panel,label='Your Name')
		vbox.Add(st1,1)
		tc=wx.TextCtrl(panel,size=(100,50))
	 	vbox.Add(tc,1)	

		
		st2=wx.StaticText(panel,label='Your Email')
		vbox.Add(st2,1)
		tc2=wx.TextCtrl(panel,size=(100,20))
		vbox.Add(tc2,0)
		
		panel.SetSizer(vbox)

if __name__ == '__main__':
	app=wx.App()
	Example(None,title='Border')
	app.MainLoop()
