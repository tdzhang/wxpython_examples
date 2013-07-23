'''
This is a simple example to show a simple menu
'''
import wx

APP_EXIT=1

class Example(wx.Frame):
	def __init__(self,*args,**kargs):
		super(Example,self).__init__(*args,**kargs)
		self.InitUI()

	def InitUI(self):
		menubar=wx.MenuBar()
		fileMenu=wx.Menu()
		qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
		fileMenu.AppendItem(qmi)
		menubar.Append(fileMenu,'&File')

		self.Bind(wx.EVT_MENU,self.OnQuit,id=APP_EXIT)
		self.SetMenuBar(menubar)

		self.SetSize((300,200))
		self.SetTitle('Simple Menu')
		self.Centre()
		self.Show()
	
	def OnQuit(self,e):
		self.Close()


def main():
	ex=wx.App()
	Example(None)
	ex.MainLoop()
	
if __name__ =='__main__':
	main()
