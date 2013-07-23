
'''
This is a simple example to show a simple menu and Sub menu with Seperator
'''
import wx

#define some constants
APP_OPEN=1
APP_SAVE=2
APP_QUIT=3

class Example(wx.Frame):
	#over write the inital function
	def __init__(self,*args,**kargs):
		super(Example,self).__init__(*args,**kargs)
		self.InitUI()

	#initial the UI
	def InitUI(self):
		#add menubar, menu and menuitems
		menubar=wx.MenuBar()
		fileMenu=wx.Menu()
		openi=wx.MenuItem(fileMenu,APP_OPEN,'&Open')
		savei=wx.MenuItem(fileMenu,APP_SAVE,'&Save')
		qmi = wx.MenuItem(fileMenu, APP_QUIT, '&Quit\tCtrl+Q')
		fileMenu.AppendItem(openi)
		fileMenu.AppendItem(savei)
		fileMenu.AppendSeparator()
		fileMenu.AppendItem(qmi)
		menubar.Append(fileMenu,'&File')
		
		#bind event with menuites
		self.Bind(wx.EVT_MENU,self.OnQuit,id=APP_QUIT)

		self.SetMenuBar(menubar)

		#adjust the size of the Frame, and show the Frame
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
