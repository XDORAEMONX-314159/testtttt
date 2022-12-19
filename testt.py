import Tkinter as tk

window = tk.Tk()
window.title('股票回測程式')
window.geometry('400x400+800+350')
window.resizable(False,False)

stockname_get = tk.StringVar()
begining_get = tk.StringVar()
ending_get = tk.StringVar()
high_get = tk.StringVar()
low_get = tk.StringVar()
period_get = tk.StringVar()
allmoney_get = tk.StringVar()

name_label = tk.Label(window, text='請輸入股票名稱(代號):')
name_label.place(x=40,y=10)
name_entry = tk.Entry(window,textvariable=stockname_get)
name_entry.place(x=200,y=10)

start_label = tk.Label(window,text='請輸入起始時間:')
start_label.place(x=40,y=40)
start_entry = tk.Entry(window,textvariable=begining_get)
start_entry.place(x=200,y=40)

end_label = tk.Label(window,text='請輸入終止時間:')
end_label.place(x=40,y=70)
end_entry = tk.Entry(window,textvariable=ending_get)
end_entry.place(x=200,y=70)

big_label = tk.Label(window,text='請輸入最大值:')
big_label.place(x=40,y=100)
big_entry = tk.Entry(window,textvariable=high_get)
big_entry.place(x=200,y=100)

small_label = tk.Label(window,text='請輸入最小值:')
small_label.place(x=40,y=130)
small_entry = tk.Entry(window,textvariable=low_get)
small_entry.place(x=200,y=130)

period_label = tk.Label(window,text='請輸入週期:')
period_label.place(x=40,y=160)
period_entry = tk.Entry(window,textvariable=period_get)
period_entry.place(x=200,y=160)

allmoney_label = tk.Label(window,text='請輸入全部金錢:')
allmoney_label.place(x=40,y=190)
allmoney_entry = tk.Entry(window,textvariable=allmoney_get)
allmoney_entry.place(x=200,y=190)

window.mainloop()
