import wx

class Example(wx.Frame):
	def __init__(self, parent, title):
		super(Example,self).__init__(parent,title=title,size=(260,180))

		self.InitUI()
		self.Centre()
		self.Show()
	
	def InitUI(self):
		#panel=wx.Panel(self, -1)

		menubar=wx.MenuBar()
		filem=wx.Menu()
		editm=wx.Menu()
		helpm=wx.Menu()

		menubar.Append(filem,'&File')
		menubar.Append(editm,'&Edit')
		menubar.Append(helpm,'&Help')
		self.SetMenuBar(menubar)

		#wx.TextCtrl(panel, pos=(3,3),size=(250,150))
		wx.TextCtrl(self)

if __name__ == '__main__':
	app=wx.App()
	Example(None,title='hah')
	app.MainLoop()
