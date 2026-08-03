import tkinter as tk
from tkinter import messagebox
import os

        
        
def create():
    namefile = nama.get()
    h = teks.get("1.0",tk.END).strip()
    if namefile == "":
            messagebox.showwarning ("Peringatan", "Masukan nama file")
            return
    try:
        with open(namefile + '.txt',"w") as f:
            f.write(h)
            messagebox.showinfo("Sukses", f"Sukses membuat file: {namefile}.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuat file: {e}")

def append():
    namefile_a = nama.get()
    a = teks.get("1.0", tk.END).strip()
    if namefile_a == "":
        messagebox.showwarning ("Peringatan", "Masukan nama file")
        return
    if not os.path.exists(namefile_a + ".txt"):
        messagebox.showerror("Error", "File tidak ditemukan")
        return
    try:
        with open(namefile_a + '.txt', "a") as f:
            f.write(f'\n{a}')
            teks.delete('1.0', tk.END)
            messagebox.showinfo("Sukses", f"Sukses menambahkan file: {namefile_a}.txt")
    except FileNotFoundError:
         messagebox.showerror("Error", f"Gagal menambhakan file:")

def read():
    namefile_r = nama.get()
    try:
        with open (namefile_r + '.txt', "r", encoding = "utf-8") as f:
            isi = f.read()
        show.delete("1.0", tk.END)
        show.insert(tk.END, isi)
    except Exception as e:
        show.delete("1.0", tk.END)
        show.insert(tk.END, "File tidak ada")
        
def delete():
    namefile_d = deletename.get()
    if namefile_d == "":
            messagebox.showwarning ("Peringatan", "Masukan nama file")
            return
    if not os.path.exists(namefile_d +'txt'):
        show.delete("1.0", tk.END)
        show.insert(tk.END, "File tidak ditemukan")
    confirm = messagebox.askyesno(
        "Konfirmasi",
        f"yakin ingin menghapus file '{namefile_d}.txt'?"
    )
    if confirm:
        try:
            os.remove(namefile_d + ".txt")
            show.delete("1.0", tk.END)
            show.insert(tk.END, f"File '{namefile_d}.txt' berhasil dihapus")
            messagebox.showinfo("Berhasil","File berhasil dihapus")
        except Exception as e:
            messagebox.showerror ("Error", f"Gagal menghapus file {e}")

def update():
    namefile_u = deletename.get().strip()
    if namefile_u == "":
                messagebox.showwarning ("Peringatan", "Masukan nama file")
                return
    if not os.path.exists(namefile_u +'.txt'):
        messagebox.showerror("Error", "File tidak ditemukan")
        
    old = search.get().strip()
    new = baru.get().strip()
    
    if old == "":
        messagebox.showwarning ("Peringatan", "Masukan teks yang ingin dicari")
        return
    
    if new == "":
        messagebox.showwarning ("Peringatan", "Masukan teks yang ingin diganti")
        return
    try:
        with open (namefile_u + '.txt', "r") as f:
            data = f.read()
        if old not in data:
            messagebox.showwarning ("Peringatan", "Teks tidak ditemukan")
            return
        data = data.replace(old,new)
        with open(namefile_u + '.txt', "w") as f:
            f.write(data)
        show.delete("1.0", tk.END)
        show.insert(tk.END, data)
        messagebox.showinfo("Berhasil","File berhasil diupdate")
    except Exception as e:
        messagebox.showerror ("Error", f"Gagal menghapus file {e}")
        
            
root = tk.Tk()
root.title("Final Project")
root.geometry('800x400')
text_var = tk.StringVar()
text_var1 = tk.StringVar()
text_var2 = tk.StringVar()
text_var3 = tk.StringVar()


tk.Label(root,text="Nama File").place(x= 10,y=10,height = 20)
nama = tk.Entry(root, textvariable=text_var)
nama.place(x=80,y=10,height = 20)

tk.Label(root,text = "Teks").place(x=10,y=50,height = 20)
teks = tk.Text(root,width = 30)
teks.place(x = 10,y = 80,height=130)

tk.Button(root,text="Create",command = create).place(x=300,y = 80,height = 30,width= 60)
tk.Button(root,text="Append", command = append).place(x=300,y = 120,height = 30,width= 60)
tk.Button(root,text="Read", command = read).place(x=680,y = 80,height = 30,width= 60)

tk.Label(root,text = "Tampilan").place(x=400,y=50,height = 20)
show = tk.Text(root,width = 30)
show.place(x = 400,y = 80,height=130)

tk.Label(root,text = "Search Text").place(x=10,y=250,height = 20)
search = tk.Entry(root,textvariable=text_var1)
search.place(x = 10,y = 280,height=20)

tk.Label(root,text = "Update Text").place(x=150,y=250,height = 20)
baru = tk.Entry(root,textvariable=text_var2)
baru.place(x = 150,y = 280,height=20)
tk.Button(root,text="Update", command = update).place(x=300,y = 275,height = 30,width= 60)

tk.Label(root,text = "File").place(x=10,y=320,height = 20)
deletename = tk.Entry(root,textvariable=text_var3)
deletename.place(x = 10,y = 340,height=20)
tk.Button(root,text="Delete", command = delete).place(x=160,y = 340,height = 30,width= 60)
root.mainloop()