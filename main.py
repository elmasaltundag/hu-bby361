from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class EserUygulamasi:
    def __init__(self):
        self.baglanti = sqlite3.connect("ElmasAltundag.db")
        self.sorgu = self.baglanti.cursor()

        self.pencere = Tk()
        self.pencere.title('Katalog: Eser Uygulaması')
        self.pencere.geometry('1000x400')
        self.pencere.resizable = True
        self.pencere['bg'] = '#65B741'

        self.eser_tablo_cercevesi = ttk.Frame(self.pencere, padding=25)
        self.eser_tablo_cercevesi.pack()

        self.eser_tablosu = ttk.Treeview(self.eser_tablo_cercevesi)
        self.eser_tablosu['columns'] = ('id', 'EserAdı', 'EserTürü', 'YayınTarihi', 'ISBN', 'SayfaSayısı', 'EserYayınyeri', 'Dil')

        self.eser_tablosu.column("#0", width=0, stretch=NO)
        self.eser_tablosu.column("id", anchor=CENTER, width=50)
        self.eser_tablosu.column("EserAdı", anchor=CENTER, width=150)
        self.eser_tablosu.column("EserTürü", anchor=CENTER, width=150)
        self.eser_tablosu.column("YayınTarihi", anchor=CENTER, width=100)
        self.eser_tablosu.column("ISBN", anchor=CENTER, width=100)
        self.eser_tablosu.column("SayfaSayısı", anchor=CENTER, width=100)
        self.eser_tablosu.column("EserYayınyeri", anchor=CENTER, width=150)
        self.eser_tablosu.column("Dil", anchor=CENTER, width=150)

        self.eser_tablosu.heading("#0", text="", anchor=CENTER)
        self.eser_tablosu.heading("id", text="ID", anchor=CENTER)
        self.eser_tablosu.heading("EserAdı", text="Eser Adı", anchor=CENTER)
        self.eser_tablosu.heading("EserTürü", text="Eser Türü", anchor=CENTER)
        self.eser_tablosu.heading("YayınTarihi", text="Yayın Tarihi", anchor=CENTER)
        self.eser_tablosu.heading("ISBN", text="ISBN", anchor=CENTER)
        self.eser_tablosu.heading("SayfaSayısı", text="Sayfa Sayısı", anchor=CENTER)
        self.eser_tablosu.heading("EserYayınyeri", text="Eser Yayın Yeri", anchor=CENTER)
        self.eser_tablosu.heading("Dil", text="Dil", anchor=CENTER)
        self.eser_tablosu.pack()

        self.arama_baslik = Label(self.eser_tablo_cercevesi, text="Aramak İstediğiniz Eser Adını Giriniz :")
        self.arama = Entry(self.eser_tablo_cercevesi, width=25)
        self.ara = Button(self.eser_tablo_cercevesi, text="Arama Yap!", command=self.arama_yap)
        self.arama_baslik.pack(side=LEFT, padx=5, pady=5)
        self.arama.pack(side=LEFT, padx=5, pady=5)
        self.ara.pack(side=LEFT, padx=5, pady=5)

        self.ekle_button = Button(self.eser_tablo_cercevesi, text="Yeni Eser Ekle", command=self.eser_ekle_pencere)
        self.ekle_button.pack(side=LEFT, padx=5, pady=5)

        self.sil_button = Button(self.eser_tablo_cercevesi, text="Seçili Eseri Sil", command=self.eseri_sil)
        self.sil_button.pack(side=LEFT, padx=5, pady=5)

        self.listele_button = Button(self.eser_tablo_cercevesi, text="Eserleri Listele", command=self.eserleri_listele)
        self.listele_button.pack(side=LEFT, padx=5, pady=5)

        self.pencere.mainloop()

    def arama_yap(self):
        anahtar = self.arama.get()
        arama_sonuc = self.sorgu.execute(
            "SELECT * FROM Eser WHERE \"EserAdı\" LIKE ? OR \"EserTürü\" LIKE ? OR \"YayınTarihi\" LIKE ? OR \"ISBN\" LIKE ? OR \"SayfaSayısı\" LIKE ? OR \"EserYayınyeri\" LIKE ? OR \"Dil\" LIKE ? ORDER BY EserAdı DESC",
            ('%' + anahtar + '%', '%' + anahtar + '%', '%' + anahtar + '%', '%' + anahtar + '%', '%' + anahtar + '%', '%' + anahtar + '%', '%' + anahtar + '%')
        )

        for row in self.eser_tablosu.get_children():
            self.eser_tablosu.delete(row)

        for index, eser in enumerate(arama_sonuc.fetchall()):
            self.eser_tablosu.insert(parent='', index='end', iid=index, text='',
                                     values=(eser[0], eser[1], eser[2], eser[3], eser[4], eser[5], eser[6], eser[7]))

    def eser_ekle_pencere(self):
        self.pencere_ekle = Tk()
        self.pencere_ekle.title('Katalog: Eser Ekle')
        self.pencere_ekle.geometry('300x300')
        self.pencere_ekle.resizable = True
        self.pencere_ekle['bg'] = '#65B741'

        self.eser_cercevesi = ttk.Frame(self.pencere_ekle, padding=10)
        self.eser_cercevesi.pack()

        l1 = Label(self.eser_cercevesi, text="Eser Adı")
        l2 = Label(self.eser_cercevesi, text="Eser Türü")
        l3 = Label(self.eser_cercevesi, text="Yayın Tarihi")
        l4 = Label(self.eser_cercevesi, text="ISBN")
        l5 = Label(self.eser_cercevesi, text="Sayfa Sayısı")
        l6 = Label(self.eser_cercevesi, text="Eser Yayın Yeri")
        l7 = Label(self.eser_cercevesi, text="Dil")
        self.e1 = Entry(self.eser_cercevesi, width=25)
        self.e2 = Entry(self.eser_cercevesi, width=25)
        self.e3 = Entry(self.eser_cercevesi, width=25)
        self.e4 = Entry(self.eser_cercevesi, width=25)
        self.e5 = Entry(self.eser_cercevesi, width=25)
        self.e6 = Entry(self.eser_cercevesi, width=25)
        self.e7 = Entry(self.eser_cercevesi, width=25)
        b1 = Button(self.eser_cercevesi, text="Yeni Eser Ekle", command=self.eser_ekle)
        b2 = Button(self.eser_cercevesi, text="Temizle", command=self.form_temizle)

        l1.grid(row=0, column=0, sticky=W, pady=2)
        self.e1.grid(row=0, column=1, pady=2)
        l2.grid(row=1, column=0, sticky=W, pady=2)
        self.e2.grid(row=1, column=1, pady=2)
        l3.grid(row=2, column=0, sticky=W, pady=2)
        self.e3.grid(row=2, column=1, pady=2)
        l4.grid(row=3, column=0, sticky=W, pady=2)
        self.e4.grid(row=3, column=1, pady=2)
        l5.grid(row=4, column=0, sticky=W, pady=2)
        self.e5.grid(row=4, column=1, pady=2)
        l6.grid(row=5, column=0, sticky=W, pady=2)
        self.e6.grid(row=5, column=1, pady=2)
        l7.grid(row=6, column=0, sticky=W, pady=2)
        self.e7.grid(row=6, column=1, pady=2)

        b1.grid(row=7, column=1, pady=2)
        b2.grid(row=7, column=0, pady=2)

        self.pencere_ekle.mainloop()

    def eser_ekle(self):
        form_veri = (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get(), self.e7.get())
        self.sorgu.execute("INSERT INTO Eser VALUES(NULL,?,?,?,?,?,?,?)", form_veri)
        self.baglanti.commit()
        messagebox.showinfo(title="Katalog Bilgi", message="Eser başarıyla eklendi..!")
        self.pencere_ekle.destroy()
        self.eserleri_listele()

    def form_temizle(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')

    def eseri_sil(self):
        # Seçili olanı silme işlemi
        secili_item = self.eser_tablosu.selection()
        if not secili_item:
            messagebox.showwarning("Uyarı", "Lütfen bir eser seçin.")
            return

        EserId = self.eser_tablosu.item(secili_item, "values")[0]
        self.sorgu.execute("DELETE FROM Eser WHERE EserId=?", (EserId,))
        self.baglanti.commit()
        messagebox.showinfo("Başarı", "Eser başarıyla silindi.")
        self.eserleri_listele()

    def eserleri_listele(self):
        for row in self.eser_tablosu.get_children():
            self.eser_tablosu.delete(row)

        sonuc = self.sorgu.execute("SELECT * FROM Eser")
        for index, eser in enumerate(sonuc.fetchall()):
            self.eser_tablosu.insert(parent='', index='end', iid=index, text='',
                                     values=(eser[0], eser[1], eser[2], eser[3], eser[4], eser[5], eser[6], eser[7]))

uygulama = EserUygulamasi()
