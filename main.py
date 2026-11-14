from tkinter import Tk, Label, Entry, Button, messagebox, ttk
from estudiantes import estudiante

 
class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Estudiantes")
        self.ventana.geometry("700x700")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="lightblue")
        self.main()
    
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="::: MENÚ ESTUDIANTES :::", font=("Calibri", 14, "italic", "bold"), bg="#1b4f72", fg="#ffffff").pack(pady=20)
        Button(self.ventana, text="1- Estudiantes", command=self.menu_acciones, width=20, bg="#2e86c1", fg="#ffffff").pack(pady=10)
        Button(self.ventana, text="2- Salir", command=self.ventana.quit, width=20, bg="#c0392b", fg="#ffffff").pack(pady=10)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo = "Estudiante"
        Label(self.ventana, text=f"...::: Menú de {tipo} :::..." ,font=("Calibri", 14, "italic", "bold"), bg="#1b4f72", fg="#ffffff").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_estudiante_view, width=20, bg="#2e86c1", fg="#ffffff").pack(pady=5)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_estudiante_view, width=20, bg="#2e86c1", fg="#ffffff").pack(pady=5)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_estudiante_view, width=20, bg="#2e86c1", fg="#ffffff").pack(pady=5)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_estudiante_view, width=20, bg="#2e86c1", fg="#ffffff").pack(pady=5)
        Button(self.ventana, text="5.- Regresar", command=self.main, width=20, bg="#c0392b", fg="#ffffff").pack(pady=5)

    def insertar_estudiante_view(self,):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese los datos del estudiante...",font=("Arial", 12), bg="#1b4f72", fg="#ffffff").pack(pady=10)
        
        Label(self.ventana, text="Nombre: ", bg="#2e86c1", fg="#ffffff").pack(pady=2)
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=2)
        
        Label(self.ventana, text="Nota (Calificación): ", bg="#2e86c1", fg="#ffffff").pack(pady=2)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=2)

        Button(self.ventana, text="Agregar", command=self.insertar_estudiante_controller, bg="#27ae60", fg="#ffffff").pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones, bg="#c0392b", fg="#ffffff").pack(pady=5)

    def eliminar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="Ingresar el ID del estudiante a borrar:",font=("Calibri", 14, "italic", "bold"), bg="#1b4f72", fg="#ffffff").pack(pady=10)
        self.idBorrar = Entry(self.ventana)
        self.idBorrar.focus()
        self.idBorrar.pack(pady=5)

        Button(self.ventana, text="Borrar", command=self.eliminar_estudiante_controller, bg="#e67e22", fg="#ffffff").pack(pady=5)
        Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones, bg ="#c0392b", fg="#ffffff").pack(pady=5)

    def consultar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::: Consultar Estudiantes :::...", font=("Arial", 12), bg="#1b4f72", fg="#ffffff").pack(pady=10)
        columnas = ("num", "id", "nombre", "nota")
        tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=15)
        tabla.heading("num", text="#")
        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("nota", text="Nota")

        tabla.column("num", width=50, anchor="center")
        tabla.column("id", width=50, anchor="center")
        tabla.column("nombre", width=200, anchor="center")
        tabla.column("nota", width=100, anchor="center")

        scroll = ttk.Scrollbar(self.ventana, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=scroll.set)
        registros = self.consultar_estudiante_controller()
        for num, fila in enumerate(registros, 1):
            tabla.insert("", "end", values=(num, fila[0], fila[1], fila[2]))
        tabla.pack(pady=10)
        scroll.pack(side="right", fill="y")
        
        if not registros:
            Label(self.ventana, text="...¡No se encontró información en la base de datos!...", fg="#ffffff", bg="#e67e22").pack(pady=5)
        Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones, bg ="#c0392b", fg="#ffffff").pack(pady=10)

    def modificar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese el ID y los nuevos datos...", font=("Calibri", 14, "italic", "bold"), bg="#1b4f72", fg="#ffffff").pack(pady=5)
                
        Label(self.ventana, text="ID a Modificar: ", bg="#1b4f72", fg="#ffffff").pack(pady=2)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=2)
                
        Label(self.ventana, text="Nombre: ", bg="#1b4f72", fg="#ffffff").pack(pady=2)
        self.nombre = Entry(self.ventana)
        self.nombre.pack(pady=2)
                
        Label(self.ventana, text="Nota (Calificación): ", bg="#1b4f72", fg="#ffffff").pack(pady=2)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=2)

        Button(self.ventana, text="Modificar", command=self.modificar_estudiante_controller, bg="#27ae60", fg="#ffffff").pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones, bg ="#c0392b", fg="#ffffff").pack(pady=5)

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::", message="...¡Acción Realizada con Éxito!...")
        else:
            messagebox.showerror(title=":: Error ::", message="...¡Esta Acción no pudo realizarse!...")

    def insertar_estudiante_controller(self):
        estudiante1 = estudiante.Estudiantes(self.nombre.get().upper().strip(), self.nota.get().strip())
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)
        self.nombre.focus()
        if respuesta:
            self.nombre.delete(0, 'end')
            self.nota.delete(0, 'end')

    def eliminar_estudiante_controller(self):
        id_estudiante = self.idBorrar.get().strip()
        estudiante1 = estudiante.Estudiantes()
        respuesta = estudiante1.eliminar(id_estudiante)
        self.respuesta_sql(respuesta)
        if respuesta:
            self.idBorrar.delete(0, 'end')
            self.idBorrar.focus()

    def consultar_estudiante_controller(self):
     
        estudiante1 = estudiante.Estudiantes()
        return estudiante1.consultar() or []

    def modificar_estudiante_controller(self):
        id_estudiante = self.id.get().strip()
        estudiante1 = estudiante.Estudiantes(self.nombre.get().upper().strip(), self.nota.get().strip())
        respuesta = estudiante1.actualizar(id_estudiante)
        self.respuesta_sql(respuesta)
        if respuesta:
            self.id.delete(0, 'end')
            self.nombre.delete(0, 'end')
            self.nota.delete(0, 'end')
            self.id.focus()

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()