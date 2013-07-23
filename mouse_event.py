import wx

class Example(wx.Frame):
	def __init__(self,*arg,**args):
		super(Example,self).__init__(*arg,**args)

		self.InitUI()

	def InitUI(self):
		wx.StaticText(self,label='x',pos=(10,10))
		wx.StaticText(self,label='y',pos=(10,30))

		self.t1=wx.StaticText(self,label='',pos=(30,10))
		self.t2=wx.StaticText(self,label='',pos=(30,30))
				
		self.Bind(wx.EVT_MOTION,self.OnMove)

		self.SetSize((200,200))
		self.SetTitle('mouse Event')
		self.Centre()
		self.Show()
	
	def OnMove(self,e):
		x,y = e.GetPosition()
		self.t1.SetLabel(str(x))
		self.t2.SetLabel(str(y))

if __name__ == '__main__':
	app=wx.App()
	Example(None)
	app.MainLoop()
