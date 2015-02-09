from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

from PyQt5 import QtCore, QtGui
from Messaging import stdMsg, dbgMsg, errMsg, setDebugging
(ORGANIZATION, APPLICATION) = ("SwatInternationalProductions", "Twedit++")

class Configuration:
    def __init__(self):

        #default settings
        self.defaultConfigs={}
        self.defaultConfigs["TabSpaces"]=4
        self.defaultConfigs["UseTabSpaces"]=True
        self.defaultConfigs["DisplayLineNumbers"]=True
        self.defaultConfigs["FoldText"]=True
        self.defaultConfigs["TabGuidelines"]=True
        self.defaultConfigs["DisplayWhitespace"]=False
        self.defaultConfigs["DisplayEOL"]=False
        self.defaultConfigs["WrapLines"]=False
        self.defaultConfigs["ShowWrapSymbol"]=False
        self.defaultConfigs["DontShowWrapLinesWarning"]=False
        self.defaultConfigs["RestoreTabsOnStartup"]=True
        self.defaultConfigs["EnableAutocompletion"]=False
        self.defaultConfigs["EnableQuickTextDecoding"]=True
        self.defaultConfigs["AutocompletionThreshold"]=2
        self.defaultConfigs["PanelSplitterState"]=QByteArray()
        self.defaultConfigs["InitialSize"]=QSize(600,600)
        self.defaultConfigs["InitialPosition"]=QPoint(0,0)
        # self.defaultConfigs["RecentDocuments"]=QStringList()
        # self.defaultConfigs["RecentDirectories"]=QStringList()
        # self.defaultConfigs["ListOfOpenFiles"]=QStringList()
        # self.defaultConfigs["ListOfOpenFilesAndPanels"]=QStringList()
        # self.defaultConfigs["FRFindHistory"]=QStringList() #FR stands for Find & Replace
        # self.defaultConfigs["FRReplaceHistory"]=QStringList()
        # self.defaultConfigs["FRFiltersHistory"]=QStringList()
        # self.defaultConfigs["FRDirectoryHistory"]=QStringList()
        
        self.defaultConfigs["RecentDocuments"]=[]
        self.defaultConfigs["RecentDirectories"]=[]
        self.defaultConfigs["ListOfOpenFiles"]=[]        
        self.defaultConfigs["ListOfOpenFilesAndPanels"]=[]
        self.defaultConfigs["FRFindHistory"]=[] #FR stands for Find & Replace
        self.defaultConfigs["FRReplaceHistory"]=[]
        self.defaultConfigs["FRFiltersHistory"]=[]
        self.defaultConfigs["FRDirectoryHistory"]=[]
        
        self.defaultConfigs["FRInSelection"]=False
        self.defaultConfigs["FRInAllSubfolders"]=False
        self.defaultConfigs["FRSyntaxIndex"]=0
        self.defaultConfigs["FRTransparencyEnable"]=True
        self.defaultConfigs["FROnLosingFocus"]=True        
        self.defaultConfigs["FRAlways"]=False
        self.defaultConfigs["FROpacity"]=75
        self.defaultConfigs["ZoomRange"]=0
        self.defaultConfigs["ZoomRangeFindDisplayWidget"]=0
        self.defaultConfigs["CurrentTabIndex"]=-1 # index of the current tab  - 1 means we should make last open tab current
        self.defaultConfigs["CurrentPanelIndex"]=0 # index of the current panel  - 1 means we should make last open tab current        
        # self.defaultConfigs["KeyboardShortcuts"]=QStringList()
        # self.defaultConfigs["PluginAutoloadData"]=QStringList()
        # self.defaultConfigs["BaseFontName"]=QString("Courier New")
        # self.defaultConfigs["BaseFontSize"]=QString("10")
        # self.defaultConfigs["Theme"]=QString("Default")
        self.defaultConfigs["KeyboardShortcuts"]=[]
        self.defaultConfigs["PluginAutoloadData"]=[]
                
        self.defaultConfigs["BaseFontName"]="Courier New"
        self.defaultConfigs["BaseFontSize"]="10"
        self.defaultConfigs["Theme"]="Default"
        
        self.modifiedKeyboardShortcuts = {} # dictionary actionName->shortcut for modified keyboard shortcuts - only reassinged shortcuts are stored
        self.modifiedPluginsAutoloadData = {} # dictionary pluginName->autoLoad for modified plugin autoload data - only reassinged data are stored
        
        self.settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, ORGANIZATION, APPLICATION)
        self.initSyncSettings()
        self.updatedConfigs={}
        

        

        
    # def configuration(self,_key):
        # return self.configs[_key]

    def setting(self,_key):
        if _key in ["UseTabSpaces","DisplayLineNumbers","FoldText","TabGuidelines","DisplayWhitespace","DisplayEOL","WrapLines","ShowWrapSymbol","DontShowWrapLinesWarning",\
        "RestoreTabsOnStartup","EnableAutocompletion","EnableQuickTextDecoding","FRInSelection","FRInAllSubfolders","FRTransparencyEnable","FROnLosingFocus","FRAlways"]: # Boolean values
            val = self.settings.value(_key)
            if val:
                return val
            else:
                return self.defaultConfigs[_key]
                
        elif _key in ["BaseFontSize","BaseFontName","Theme"]:
            val = self.settings.value(_key)

            
            if val:
                return val
            else:
                return self.defaultConfigs[_key]
            
        elif _key in ["TabSpaces","ZoomRange","ZoomRangeFindDisplayWidget","AutocompletionThreshold","FRSyntaxIndex","FROpacity","CurrentTabIndex","CurrentPanelIndex"]: # integer values
            val = self.settings.value(_key)
            
            # if val.isValid():
            if val:            
                return val # toInt returns tuple and first element of if is the integer the second one is flag
            else:
                return self.defaultConfigs[_key]
                
        elif _key in ["InitialSize"]: # QSize values
            val = self.settings.value(_key)
            if val.isValid():
                return val
            else:
                return self.defaultConfigs[_key]                             

        elif _key in ["InitialPosition"]: # QPoint values
            val = self.settings.value(_key)
            if val:
                return val 
            else:
                return self.defaultConfigs[_key]
                
        elif _key in ["RecentDocuments","RecentDirectories","ListOfOpenFiles","ListOfOpenFilesAndPanels","FRFindHistory","FRReplaceHistory","FRFiltersHistory","FRDirectoryHistory","KeyboardShortcuts","PluginAutoloadData"]: # QStringList values

            val = self.settings.value(_key)
            if val:
                return val
            else:
                return self.defaultConfigs[_key]
                
        elif _key in ["PanelSplitterState"]: # QByteArray values
            val = self.settings.value(_key)
            if val:
                return val
            else:
                return self.defaultConfigs[_key]

                
    def setSetting(self,_key,_value):
        if _key in ["UseTabSpaces","DisplayLineNumbers","FoldText","TabGuidelines","DisplayWhitespace","DisplayEOL","WrapLines","ShowWrapSymbol","DontShowWrapLinesWarning",\
        "RestoreTabsOnStartup","EnableAutocompletion","EnableQuickTextDecoding","FRInSelection","FRInAllSubfolders","FRTransparencyEnable","FROnLosingFocus","FRAlways"]: # Boolean values
            self.settings.setValue(_key,QVariant(_value))
            
        elif _key in ["TabSpaces","ZoomRange","ZoomRangeFindDisplayWidget","AutocompletionThreshold","FRSyntaxIndex","FROpacity","CurrentTabIndex","CurrentPanelIndex"]: # integer values
            self.settings.setValue(_key,_value)

            
        elif _key in ["BaseFontName","BaseFontSize","Theme"]: # string values
            self.settings.setValue(_key,QVariant(_value))
            
        elif _key in ["RecentDocuments","RecentDirectories","InitialSize","InitialPosition","ListOfOpenFiles","ListOfOpenFilesAndPanels","FRSyntax","FRFindHistory","FRReplaceHistory","FRFiltersHistory","FRDirectoryHistory","KeyboardShortcuts","PluginAutoloadData"]: # QSize, QPoint,QStringList , QString values
            self.settings.setValue(_key,QVariant(_value))
        elif _key in ["PanelSplitterState"]: # QByteArray
            self.settings.setValue(_key,QVariant(_value))
            
        else:
            dbgMsg("Wrong format of configuration option:",_key,":",_value)
    
    def setPluginAutoloadData(self,_pluginName,_autoloadFlag):
        self.modifiedPluginsAutoloadData[_pluginName]=_autoloadFlag
        
    def pluginAutoloadData(self):
        return self.modifiedPluginsAutoloadData

    def preparePluginAutoloadDataForStorage(self):
        self.modifiedPluginsDataStringList=[]
        for pluginName in self.modifiedPluginsAutoloadData.keys():
            self.modifiedPluginsDataStringList.append(pluginName)
            self.modifiedPluginsDataStringList.append(str(self.modifiedPluginsAutoloadData[pluginName])) # converting bool to string
        print 'STORING ',self.modifiedPluginsAutoloadData    
        for i in range(0,len(self.modifiedPluginsDataStringList),2): 
            print (str(self.modifiedPluginsDataStringList[i]),str(self.modifiedPluginsDataStringList[i+1]))
        self.setSetting("PluginAutoloadData",self.modifiedPluginsDataStringList)    

        
    def setKeyboardShortcut(self,_actionName,_keyboardshortcut):
        self.modifiedKeyboardShortcuts[_actionName]=_keyboardshortcut    
        
    def keyboardShortcuts(self):
        return self.modifiedKeyboardShortcuts
    
    def prepareKeyboardShortcutsForStorage(self):
        self.modifiedKeyboardShortcutsStringList=[]
        for actionName in self.modifiedKeyboardShortcuts.keys():
            self.modifiedKeyboardShortcutsStringList.append(actionName)
            self.modifiedKeyboardShortcutsStringList.append(self.modifiedKeyboardShortcuts[actionName])
            
        self.setSetting("KeyboardShortcuts",self.modifiedKeyboardShortcutsStringList)    
            
        
    
    def initSyncSettings(self):
        for key in self.defaultConfigs.keys():
            
            val = self.settings.value(key)
            # if not val.isValid():
            if not val:                
                self.setSetting(key,self.defaultConfigs[key])
                
        # initialize self.modifiedKeyboardShortcuts
        self.modifiedKeyboardShortcutsStringList=self.setting("KeyboardShortcuts")
        for i in range(0,len(self.modifiedKeyboardShortcutsStringList),2): 
            self.modifiedKeyboardShortcuts[str(self.modifiedKeyboardShortcutsStringList[i])]=str(self.modifiedKeyboardShortcutsStringList[i+1])        
            
        self.modifiedPluginsDataStringList=self.setting("PluginAutoloadData")
        print 'INIT SYNC self.modifiedPluginsDataStringList=',self.modifiedPluginsDataStringList
        
        for i in range(0,len(self.modifiedPluginsDataStringList),2): 
            print (str(self.modifiedPluginsDataStringList[i]),str(self.modifiedPluginsDataStringList[i+1]))   
            self.modifiedPluginsAutoloadData[str(self.modifiedPluginsDataStringList[i])] = (str(self.modifiedPluginsDataStringList[i+1]).rstrip()=='True') #converting string to bool 
            # bool(str(self.modifiedPluginsDataStringList[i+1]))        
        # sys.exit()
            