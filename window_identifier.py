import wx

class Example(wx.Frame):
	def __init__(self, *arg, **args):
		super(Example,self).__init__(*arg,**args)

		self.InitUI()

	def InitUI(self):

		panel=wx.Panel(self)

		exit_Btn=wx.Button(panel, wx.ID_ANY,'Exit')

		self.Bind(wx.EVT_BUTTON, self.OnExit, id=exit_Btn.GetId())

		self.SetTitle('Window Identifier')
		self.Centre()
		self.Show()
	
	def OnExit(self,e):
		self.Close()

if __name__ == '__main__':
	app=wx.App()
	Example(None)
	app.MainLoop()
	
