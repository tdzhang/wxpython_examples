'''
This is simple program to show a Popup menu when user right click the panel
'''

import wx

class MyPopUpMenu(wx.Menu):
	def __init__(self,parent):
		super(MyPopUpMenu,self).__init__()
		self.parent=parent
		
		mmi=wx.MenuItem(self,wx.NewId(),'Minimize')
		cmi=wx.MenuItem(self,wx.NewId(),'Close')

		self.AppendItem(mmi)
		self.AppendItem(cmi)

		self.Bind(wx.EVT_MENU,self.OnMinimize,mmi)
		self.Bind(wx.EVT_MENU,self.OnClose,cmi)
	
	def OnMinimize(self,e):
		self.parent.Iconize()
	
	def OnClose(self,e):
		self.parent.Close()


class Example(wx.Frame):
	def __init__(self,*arg,**args):
		super(Example,self).__init__(*arg,**args)

		self.InitUI()

	def InitUI(self):
		self.Bind(wx.EVT_RIGHT_DOWN,self.OnRightDown)
		
		self.SetSize((300,200))
		self.SetTitle('Popup Menu')
		self.Centre()
		self.Show()

	def OnRightDown(self,e):
		self.PopupMenu(MyPopUpMenu(self), e.GetPosition())


def main():
	app=wx.App()
	Example(None)
	app.MainLoop()

if __name__ == '__main__':
	main()
