'''
This is an example to show a simple window that has been set with 250,200 height and width, and the location has been moved to (800,250)
'''
import wx

class Example(wx.Frame):
	def __init__(self, parent,title):
		super(Example,self).__init__(parent,title=title,size=(250,200))
		self.Show()
		self.Move((800,250))


if __name__ == '__main__':
	app=wx.App()

	Example(None,title='Move')
	
	app.MainLoop()
