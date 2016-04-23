from tkinter import Tk, Frame, Label, Entry, StringVar, Button
from tkinter import messagebox


class MeuFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self._nome = StringVar()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.create_label()
        self.create_entry()
        self.create_button()

    def create_label(self):
        label = Label(self, text="Digite seu nome:")
        label.pack()

    def create_entry(self):
        entry = Entry(self, textvariable=self._nome)
        entry.pack()
        entry.focus()
        entry.bind("<Return>", self.click)

        def to_upper(event):
            self._nome.set(self._nome.get().upper())

        entry.bind("<KeyRelease>", to_upper)

    def create_button(self):
        button = Button(self, text="Click", command=self.alert)
        button.bind("<Return>", self.click)
        button.pack()

    def click(self, event=None):
        print("Seu nome: {0}".format(self._nome.get()))

    def alert(self):
        name = self._nome.get().title()
        messagebox.showinfo('Título', 'Olá {}'.format(name))


class MeuApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Meu App")
        MeuFrame(self)

    def center_window(self):
        self.eval('tk::PlaceWindow {} center'.format(
            self.winfo_pathname(self.winfo_id())))

    def show(self):
        self.center_window()
        self.mainloop()


if __name__ == '__main__':
    meu_app = MeuApp()
    meu_app.show()
