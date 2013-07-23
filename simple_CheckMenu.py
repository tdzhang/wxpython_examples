'''
This is a simple example to show a menu with checkable items 
'''
import wx

#define some constants
APP_OPEN=1
APP_SAVE=2
APP_QUIT=3
APP_OK=4
APP_READY=5

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
		

		#create check item in the menu
		statusMenu=wx.Menu()
		self.oki=wx.MenuItem(statusMenu,APP_OK,'OK',kind=wx.ITEM_CHECK)
		self.readyi=wx.MenuItem(statusMenu,APP_READY,'Ready',kind=wx.ITEM_CHECK)
		statusMenu.AppendItem(self.oki)
		statusMenu.AppendItem(self.readyi)
		menubar.Append(statusMenu,'&View')

		#bind events with menuites
		self.Bind(wx.EVT_MENU,self.OnQuit,id=APP_QUIT)
		self.Bind(wx.EVT_MENU,self.ChangeOk,id=APP_OK)
		self.Bind(wx.EVT_MENU,self.ChangeReady,id=APP_READY)
		self.SetMenuBar(menubar)

		#config status bar
		self.statusbar=self.CreateStatusBar()
		self.statusbar.SetStatusText('Unchecked')

		#adjust the size of the Frame, and show the Frame
		self.SetSize((300,200))
		self.SetTitle('Simple Menu')
		self.Centre()
		self.Show()
	
	def OnQuit(self,e):
		self.Close()

	def ChangeOk(self,e):
		if self.oki.IsChecked():
			self.statusbar.SetStatusText('OK checked')
		else:
			self.statusbar.SetStatusText('OK Unchecked')

	def ChangeReady(self,e):
		if self.readyi.IsChecked():
			self.statusbar.SetStatusText('READY checked')
		else:
			self.statusbar.SetStatusText('READY Unchecked')

def main():
	ex=wx.App()
	Example(None)
	ex.MainLoop()
	
	
if __name__ =='__main__':
	main()
