# -*- coding: gbk -*-
import wx
import Dialog
import Fun
import wx.lib.dialogs

class PyMemo(wx.Frame):
    def __init__(self, parent, id, title, size):
        wx.Frame.__init__(self, parent, id, title=title, size=size)
        self.icon = wx.Icon('images/32/PyMemo_logo_white.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(self.icon)

        self.createSplitterWindow()
        self.createMenuBar()
        self.createToolBar()
        self.Centre()
        self.Show(True)

    def createMenuBar(self):
        menubar = wx.MenuBar()

        # �˵�
        fileMenu = wx.Menu()
        # editMenu = wx.Menu()
        viewMenu = wx.Menu()
        toolMenu = wx.Menu()
        helpMenu = wx.Menu()

        # ���˵���ӵ��˵���
        menubar.Append(fileMenu, '�ļ�')
        menubar.Append(viewMenu, '�鿴')
        menubar.Append(toolMenu, '����')
        menubar.Append(helpMenu, '����')

        # ��˵������ѡ��
        # fileMenu
        newLibItem = fileMenu.Append(-1, '�½������', '�½�����⣬ָ������')
        newCardItem = fileMenu.Append(-1, '�½���Ƭ', '�½���Ƭ���������')
        inputItem = fileMenu.Append(-1, '����...', '�ӱ���PC��PyAnki��������')
        outputItem = fileMenu.Append(-1, '����...', '��PyAnki�򱾵�PC���������')
        fileMenu.AppendSeparator()
        setItem = fileMenu.Append(-1, 'ƫ������', '����PyAnki��ʹ֮���ӷ����Ϊ�����')
        fileMenu.AppendSeparator()
        quitItem = fileMenu.Append(wx.ID_EXIT, '�˳�', '�뿪��Ӧ�ó���')

        # viewMenu
        # cardItem = viewMenu.Append(-1, '��Ƭ')
        # LibItem = viewMenu.Append(-1, '�����')
        # tagItem = viewMenu.Append(-1, '��ǩ')
        # viewMenu.AppendSeparator()
        # self.showLeftSideBarItem = viewMenu.AppendCheckItem(-1, '��ʾ������')
        # self.showCardListItem = viewMenu.AppendCheckItem(-1, '��ʾ��Ƭ�б�')
        self.showCardEditItem = viewMenu.AppendCheckItem(-1, '��ʾ��Ƭ�༭����')

        # self.showLeftSideBarItem.Check(True)
        # self.showCardListItem.Check(True)
        self.showCardEditItem.Check(True)



        # toolMenu
        studyItem = toolMenu.Append(-1, 'ѧϰ�����')
        # checkItem = toolMenu.Append(-1, '���տ�Ƭ')
        # optimizeItem = toolMenu.Append(-1, '�Ż����ݿ�')
        # kindItem = toolMenu.Append(-1, '����Ƭ����')


        # helpMenu
        guideItem = helpMenu.Append(wx.ID_HELP, '�û��ֲ�')
        aboutItem = helpMenu.Append(wx.ID_ABOUT, '����PyAnki')

        self.Bind(wx.EVT_MENU, self.OnStartMemo, studyItem)
        self.Bind(wx.EVT_MENU, self.OnSetting, setItem)
        self.Bind(wx.EVT_MENU, self.CloseWindow, quitItem)
        self.Bind(wx.EVT_MENU, self.OpenAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnGuide, guideItem)
        self.Bind(wx.EVT_MENU, self.OnNewLib, newLibItem)
        self.Bind(wx.EVT_MENU, self.OnExport, outputItem)
        self.Bind(wx.EVT_MENU, self.OnImport, inputItem)
        self.Bind(wx.EVT_MENU, self.OnNewCard, newCardItem)


        self.SetMenuBar(menubar)

    def createToolBar(self):
        toolId = {'import':wx.NewId(),
              'new_lib':wx.NewId(),
              'new_card':wx.NewId(),
              'setting':wx.NewId(),
              'learn':wx.NewId()}
        toolBar = self.CreateToolBar( wx.TB_HORIZONTAL
                          |wx.TB_FLAT
                          |wx.TB_TEXT
                          |wx.TB_HORZ_LAYOUT)
        quit = toolBar.AddLabelTool(wx.ID_EXIT, '�˳�', wx.Bitmap('images/32/quit.png'))
        toolBar.AddSeparator()
        importLib = toolBar.AddLabelTool(toolId['import'], '����ʿ�', wx.Bitmap('images/32/import.png'))
        newLib = toolBar.AddLabelTool(toolId['new_lib'], '�½��ʿ�', wx.Bitmap('images/32/library_add.png'))
        newCard = toolBar.AddLabelTool(toolId['new_card'], '�½���Ƭ', wx.Bitmap('images/32/card_add.png'))
        setting = toolBar.AddLabelTool(toolId['setting'], '����', wx.Bitmap('images/32/setting.png'))
        toolBar.AddSeparator()
        wordsLearn = toolBar.AddLabelTool(toolId['learn'], '��ʼѧϰ', wx.Bitmap('images/32/words_learn.png'))

        self.Bind(wx.EVT_TOOL, self.CloseWindow, quit)
        self.Bind(wx.EVT_TOOL, self.OnSetting, setting)
        self.Bind(wx.EVT_TOOL, self.OnNewLib, newLib)
        self.Bind(wx.EVT_TOOL, self.OnImport, importLib)
        self.Bind(wx.EVT_TOOL, self.OnNewCard, newCard)
        self.Bind(wx.EVT_TOOL, self.OnStartMemo, wordsLearn)

        toolBar.Realize()
        return 0

    def createSplitterWindow(self):
        splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        splitter.SetMinimumPaneSize(250)

        # ������
        panelContain = wx.Panel(splitter, -1)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        leftPanel = LeftPanel(panelContain, -1)
        vbox1.Add(leftPanel, 1, wx.EXPAND)
        panelContain.SetSizer(vbox1)

        # �зָ���
        splitter1 = wx.SplitterWindow(splitter, -1, style=wx.SP_LIVE_UPDATE)
        splitter1.SetMinimumPaneSize(480)
        # �м����
        middlePanelContain = wx.Panel(splitter1, -1)
        vboxMiddle = wx.BoxSizer(wx.VERTICAL)
        middlePanel = MiddlePanel(middlePanelContain, -1)
        vboxMiddle.Add(middlePanel, 1, wx.EXPAND)
        middlePanelContain.SetSizer(vboxMiddle)

        # �Ҳ����
        rightPanelContain = wx.Panel(splitter1, -1)
        vboxRight = wx.BoxSizer(wx.VERTICAL)
        rightPanel = RightPanel(rightPanelContain, -1)
        vboxRight.Add(rightPanel, 1, wx.EXPAND)
        rightPanelContain.SetSizer(vboxRight)

        # ���÷ָ�������
        splitter.SplitVertically(panelContain, splitter1, 250)
        splitter1.SplitVertically(middlePanelContain, rightPanelContain,-300)

        # splitter1.Unsplit()
        # splitter.Unsplit()

        self.Centre()

    def CloseWindow(self, evt):
        self.Close()
        return 0

    def OpenAbout(self, evt):
        dlg = Dialog.AboutDialog()
        return 0

    def OnSetting(self, evt):
        settingDlg = Dialog.SettingDialog()
        settingDlg.ShowModal()
        settingDlg.Destroy()

    def OnGuide(self, evt):
        f = open("Dialog.py", "r")
        msg = f.read()
        f.close()
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "�û��ֲ�")
        dlg.ShowModal()

    def OnNewLib(self, evt):
        newLibDlg = Dialog.AddNewLib(None, -1, "�½��ʿ�", (400, 200))
        newLibDlg.ShowModal()
        newLibDlg.Destroy()

    def OnExport(self, evt):
        exportDlg = Dialog.Export(None)
        exportDlg.ShowModal()
        exportDlg.Destroy()

    def OnImport(self, evt):
        importDlg = Dialog.Import(None)
        importDlg.ShowModal()
        importDlg.Destroy()

    def OnNewCard(self, evt):
        newCardDlg = Dialog.AddNewCard(None, -1, "�½����ʿ�Ƭ", (500, 500))
        newCardDlg.ShowModal()
        newCardDlg.Destroy()

    def OnStartMemo(self, evt):
        startMemoDlg = Dialog.StartMemo()
        startMemoDlg.ShowModal()
        startMemoDlg.Destroy()



# Left Section
class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        libraryDic = {'0':['��Ƶ�ּ��ʻ�һ','100/0/100', ''],
                  '1':['��Ƶ�ּ��ʻ��','0/0/17'],
                  '2':['��Ƶ�ּ��ʻ���','100/0/100'],
                  '3':['��Ƶ�ּ��ʻ���','74/0/100'],
                  '4':['CET-4��Ƶ�ʻ�','0/0/100']}
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
        vbox = wx.BoxSizer(wx.VERTICAL)
        for i in range(len(libraryDic)):
            vbox.Add(wx.Button(self, -1, label=libraryDic[str(i)][0]+"    "+libraryDic[str(i)][1], size=(-1, 40)),
                     0,
                     wx.EXPAND|wx.ALL,
                     border=10)
        self.SetSizer(vbox)
        self.Show(True)

# Middle Section
class MiddlePanel(wx.Panel):
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
		Lib_Items=['��ѡ��ɸѡ����', '��ǰ�ʿ����е�', '����ѧϰ��', '�ѵ��ڵ�', '�Ѽ�ס��', '������ѧϰ��', 'ʼ�ռǲ�ס��', '������ӵ�']
		panelHeader = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		LibComboBox = wx.ComboBox(panelHeader,
		                          pos=(0, 5),
		                          choices=Lib_Items,
		                          style=wx.CB_READONLY)
		LibComboBox.SetSelection(0)
		LibComboBox.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		go = wx.BitmapButton(panelHeader, -1, wx.Bitmap('images/other-size/search26.png'), style=wx.NO_BORDER)
		search = wx.TextCtrl(panelHeader, -1)

		hbox.Add(LibComboBox, 5, wx.TOP, border=6)
		hbox.Add(search, 5, wx.TOP|wx.LEFT, border=6)
		hbox.Add(go, 1, wx.TOP, border=6)
		panelHeader.SetSizer(hbox)


		panelContent = wx.Panel(self, -1)
		Fun.createListCtrl(self, panelContent)
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(panelHeader, 1, wx.EXPAND)
		vbox.Add(panelContent, 11, wx.EXPAND)

		self.SetSizer(vbox)

		self.Centre()
		self.Show(True)

	def OnSelect(self, e):
		selectedLib = e.GetString()
		print selectedLib

# Right Section
class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # ��Ƭ��Ϣ���
        infoPanelContain = wx.Panel(self, -1)
        infoPanel = Fun.createInfoPanel(self,infoPanelContain)
        vbox.Add(infoPanelContain, 0, wx.EXPAND)

        # ���ı��������
        richTextContain = wx.Panel(self, -1)
        richText = Fun.createRichText(self, richTextContain)
        line = wx.StaticLine(richTextContain, -1, style=wx.LI_HORIZONTAL)
        vbox.Add(richTextContain, 0, wx.EXPAND)
        vbox.Add(line, 0, wx.EXPAND)

        # ��Ƭ�������
        positiveSideCardContain = wx.Panel(self, -1)
        positiveSide = Fun.createEditCard(self, positiveSideCardContain, '�༭��Ƭ�����棺')
        vbox.Add(positiveSideCardContain, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)

        # ��Ƭ�������
        negativeSideCardContain = wx.Panel(self, -1)
        negativeSide = Fun.createEditCard(self, negativeSideCardContain, '�༭��Ƭ�ķ��棺')
        vbox.Add(negativeSideCardContain, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)


        operationPanel = wx.Panel(self, -1)
        operationCol = Fun.createOperationCol(self, operationPanel)
        vbox.Add(operationPanel, 1, wx.EXPAND|wx.TOP, border=5)

        self.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def OnCardInfo(self, evt):
	    cardInfoDlg = Dialog.CardInfoDialog()
	    cardInfoDlg.ShowModal()
	    cardInfoDlg.Destroy()
