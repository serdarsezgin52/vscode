from tkinter import Tk
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

if messagebox.askokcancel('Question', 'do you have brown hair', icon='error') == True:
    print('Yes')
else:
    print('No')

window.deiconify()
window.destroy()
window.quit()
