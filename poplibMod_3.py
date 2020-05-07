##import getpass, poplib
##user = 'serdar.sezgin52@gmail.com' 
##Mailbox = poplib.POP3_SSL('pop.googlemail.com', '995') 
##Mailbox.user(user) 
##Mailbox.pass_('dovuskulubu') 
##numMessages = len(Mailbox.list()[1])
##for i in range(numMessages):
##    for msg in Mailbox.retr(i+1)[1]:
##        print (msg)
##Mailbox.quit()

##from pyOutlook import OutlookAccount
##account_one = OutlookAccount('serdar.sezgin@outlook.com')
##account_two = OutlookAccount('token 2')
from tkinter import Tk
from time import sleep
from Message import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)

def outlook():
    app = 'Outlook'
    olook = win32.gencache.EnsureDispatch('%s.Application' % app)

    mail = olook.CreateItem(win32.constants.olMailItem)
    recip = mail.Recipients.Add('you@127.0.0.1')
    subj = mail.Subject = 'Python-to-%s Demo' % app
    body = ["Line %d" % i for i in RANGE]
    body.insert(0, '%s\r\n' % subj)
    body.append("\r\nTh-th-th-that's all folks!")
    mail.Body = '\r\n'.join(body)
    mail.Send()

    ns = olook.GetNamespace("MAPI")
    obox = ns.GetDefaultFolder(win32.constants.olFolderOutbox)
    obox.Display()
    obox.Items.Item(1).Display()

    warn(app)
    olook.Quit()

Tk().withdraw()
outlook()
