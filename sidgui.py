import tkinter as tk

frame = tk.Tk()
frame.title("OUTPUT SCREEN")
frame.geometry('500x300')

import pickle

import warnings
warnings.filterwarnings("ignore")

def english():
	inp = inputtxt.get(1.0, "end-1c")
	ans = pickle.load(open(r"C:\Users\Raj Kumar Goyal\Desktop\Final GUI here\english\modelenglish.pickle", "rb"))
	temp = pickle.load(open(r"C:\Users\Raj Kumar Goyal\Desktop\Final GUI here\english\vectorizerenglish.pickle", "rb"))
	x=[]
	x.append(inp)
	bd=temp.transform(x)
	jb=ans.predict(bd)
	
	if jb == 0:
		print("Non Abusive")
		l2=tk.Label(text="Non Abusive")
		l2.config(font=("Courier", 14), bg="#141414", fg="#ffcc66")
		l2.place(relx=0.32, rely=0.9, anchor="sw")
	else:
		print("Abusive")
		l2=tk.Label(text="  Abusive  ")
		l2.config(font=("Courier", 14), bg="#141414", fg="#ffcc66")
		l2.place(relx=0.32, rely=0.9, anchor="sw")

def hindi():
	inp = inputtxt.get(1.0, "end-1c")
	ans = pickle.load(open(r"C:\Users\Raj Kumar Goyal\Desktop\Final GUI here\Hindifinal\model.pickle", "rb"))
	temp = pickle.load(open(r"C:\Users\Raj Kumar Goyal\Desktop\Final GUI here\Hindifinal\vectorizer.pickle", "rb"))
	x=[]
	x.append(inp)
	bd=temp.transform(x)
	jb=ans.predict(bd)
		
	if jb == 0:
		print("Non Abusive")
		l2=tk.Label(text="Non Abusive")
		l2.config(font=("Courier", 14), bg="#141414", fg="#ffcc66")
		l2.place(relx=0.32, rely=0.9, anchor="sw")
	else:
		print("Abusive")
		l2=tk.Label(text="  Abusive  ")
		l2.config(font=("Courier", 14), bg="#141414", fg="#ffcc66")
		l2.place(relx=0.32, rely=0.9, anchor="sw")

inputtxt = tk.Text(frame,
				height = 7,
				width = 30)

inputtxt.pack()

printButton1 = tk.Button(frame,
						text = "ENGLISH MODEL",
						command = english)
printButton2 = tk.Button(frame,
						text = "HINDI MODEL",
						command = hindi)
printButton1.pack()
printButton2.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()