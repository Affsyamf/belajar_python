import tkinter  as tk
from tkinter import ttk
from tkinter.messagebox import showinfo 


window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Afif Syam Fauzi")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# frame input
input_frame = ttk.Frame(window)
# penempatan grid
input_frame.pack(padx=10, pady=10,fill="x", expand=True)

# komponen - komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan : ")
nama_depan_label.pack(fill="x", expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(fill="x", expand=True)


# ==================

 
# 1. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang : ")
nama_belakang_label.pack(pady=10, fill="x", expand=True)

# 2. entry nama belakang
nama_belakang_entry = ttk.Entry( input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack( fill="x", expand=True)


# 3. Button
def tombol_click():
    '''Fungsi akan dipanggil oleh tombol'''
    print(NAMA_DEPAN.get())
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="P", message=pesan)
    
tombol = ttk.Button(input_frame, text="Pencet", command=tombol_click)
tombol.pack(fill="x", expand=False, padx=15, pady=15)

window.mainloop()