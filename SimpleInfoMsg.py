import wx

class Example(wx.Frame):
	def __init__(self,*arg,**args):
		super(Example,self).__init__(*arg,**args)

		self.InitUI()
	
	def InitUI(self):
		wx.FutureCall(5000,self.ShowMsg)

		self.SetSize((200,200))
		self.SetTitle('Show Msg')
		self.Centre()
		self.Show()
	
	def ShowMsg(self):
		wx.MessageBox('Downlaod Complete','Info',wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
	app=wx.App()
	Example(None)
	app.MainLoop()
	
