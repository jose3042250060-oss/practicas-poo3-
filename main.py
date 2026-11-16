from coches import cochesbd
import tkinter as tk
from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox
from tkinter import ttk


class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="#2CF288")
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # menu principal
    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="::: MENU PRINCIPAL:::", bg="#33F22C").pack(pady=20)
        Button(self.ventana, text='1.- Coches', bg="#2CF2EB", command=self.menuAcciones).pack(pady=10)
        Button(self.ventana, text='2.- salir', bg="#2CF2EB", command=self.ventana.quit).pack(pady=10)

    def menuAcciones(self):
        self.borrarPantalla()
        tipo = "Coches"
        Label(self.ventana, text=f':::: menu de {tipo}:::: ', bg="#33F22C").pack(pady=10)

        Button(self.ventana, text="1.-agregar", bg="#2CF2EB",
               command=self.InsertarCochesView).pack(pady=10)
        Button(self.ventana, text="2.-borrar", bg="#2CF2EB",
               command=self.eliminar_coches_view).pack(pady=10)
        Button(self.ventana, text="3.- modificar", bg="#2CF2EB",
               command=self.actualizarCochesView).pack(pady=10)
        Button(self.ventana, text="4.- mostrar", bg="#2CF2EB",
               command=self.mostrarCochesView).pack(pady=10)
        Button(self.ventana, text="5.-salir", bg="#2CF2EB",
               command=self.main).pack(pady=10)

    # -vistas
    def InsertarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar datos del Coche").pack(pady=10)
        Label(self.ventana, text="Marca").pack(pady=10)
        self.marca = Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        Label(self.ventana, text="Color").pack(pady=10)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)
        Label(self.ventana, text="Modelo").pack(pady=10)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)
        Label(self.ventana, text="Velocidad").pack(pady=10)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)
        Label(self.ventana, text="Potencia").pack(pady=10)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)
        Label(self.ventana, text="asientos").pack(pady=10)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana, text='agregar', command=self.insertarCochesController).pack(pady=5)
        Button(self.ventana, text='::Regresar::', command=self.menuAcciones).pack(pady=5)

    def eliminar_coches_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar el id del coche que deseas borrar").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        self.btn_buscar = Button(self.ventana, text='Buscar',
            command=lambda: self.buscar_controller("eliminar"))
        self.btn_buscar.pack(pady=5)

        # El boton eliminar empieza deshabilitado hasta que se encuentre el registro
        self.btn_eliminar = Button(self.ventana, text='eliminar', state="disabled",
            command=self.eliminar_coches_controller)
        self.btn_eliminar.pack(pady=5)
        Button(self.ventana, text='::Regresar::', command=self.menuAcciones).pack(pady=5)

    def actualizarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="ingresar el id del coche que deseas actualizar").pack(pady=10)
        self.idActualizar = Entry(self.ventana)
        self.idActualizar.focus()
        self.idActualizar.pack(pady=5)
        Label(self.ventana, text="Marca").pack(pady=10)
        self.marcaAct = Entry(self.ventana)
        self.marcaAct.pack(pady=5)
        Label(self.ventana, text="Color").pack(pady=10)
        self.colorAct = Entry(self.ventana)
        self.colorAct.pack(pady=5)
        Label(self.ventana, text="Modelo").pack(pady=10)
        self.modeloAct = Entry(self.ventana)
        self.modeloAct.pack(pady=5)
        Label(self.ventana, text="Velocidad").pack(pady=10)
        self.velocidadAct = Entry(self.ventana)
        self.velocidadAct.pack(pady=5)
        Label(self.ventana, text="Potencia").pack(pady=10)
        self.potenciaAct = Entry(self.ventana)
        self.potenciaAct.pack(pady=5)
        Label(self.ventana, text="asientos").pack(pady=10)
        self.asientosAct = Entry(self.ventana)
        self.asientosAct.pack(pady=5)
        Button(self.ventana, text='Actualizar', command=self.actualizarCochesController).pack(pady=5)
        Button(self.ventana, text='::Regresar::', command=self.menuAcciones).pack(pady=5)

    def mostrarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text="Lista de Coches", bg="#33EB92").pack(pady=10)
        datos = self.mostrarCochescontroller()
        columnas = ("id", "marca", "color", "modelo", "velocidad", "potencia", "asientos")
        tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=60)
        for coche in datos:
            tabla.insert("", tk.END, values=coche)
        tabla.pack(pady=10)
        Button(self.ventana, text="Volver", command=self.menuAcciones, bg="#33E8EB").pack(pady=10)

    def consultarCochesView(self):
        self.borrarPantalla()
        Label(self.ventana, text=".....::::Consultar coches:::::...").pack(pady=10)
        filas = self.consultar_coche_controller("")
        Label(self.ventana, text=filas).pack(pady=10)
        Button(self.ventana, text='::Regresar::', command=self.menuAcciones).pack(pady=5)

    # ------------------------------------------------------------- CONTROLADORES
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::", message="La accion se realizo con exito ")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")

    def insertarCochesController(self):
        coche1 = cochesbd.Cochesbd(self.marca.get(), self.color.get(), self.modelo.get(),
                                   self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def confirmar_eliminar(self):
        return messagebox.askyesno(title="Confirmar", message="¿Seguro que deseas eliminar este registro?")

    def eliminar_coches_controller(self):
        id = self.id.get()
        if self.confirmar_eliminar():
            respuesta = cochesbd.Cochesbd.eliminar(id)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)

    def actualizarCochesController(self):
        id = self.idActualizar.get()
        coche1 = cochesbd.Cochesbd(self.marcaAct.get(), self.colorAct.get(), self.modeloAct.get(),
                                   self.velocidadAct.get(), self.potenciaAct.get(), self.asientosAct.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1

    def mostrarCochescontroller(self):
        return cochesbd.Cochesbd.consultar()

    def consultar_coche_controller(self, filas):
        registros = cochesbd.Cochesbd.consultar()
        num_coche = 1
        if len(registros) > 0:
            for fila in registros:
                filas += (f"coche {num_coche}\nID {fila[0]}\nMarca {fila[1]}\nColor {fila[2]}\n"
                          f"Modelo {fila[3]}\nVelocidad {fila[4]}\nPotencia {fila[5]}\n"
                          f"Asientos {fila[6]}\n\n")
                num_coche += 1
        else:
            filas = "! NO SE ENCONTRARON REGISTROS !"
        return filas

    def cambiar_estado_btn(self, estado, tipo_accion):
        if tipo_accion == "eliminar":
            self.btn_eliminar.config(state="normal" if estado else "disabled")

    def buscar_controller(self, tipo_accion):
        id = self.id.get()
        coche1 = cochesbd.Cochesbd.buscar(id)
        if coche1 and len(coche1) > 0:
            messagebox.showinfo(title="....Registro encontrado....",
                                message=f"....El registro fue encontrado con exito... puedes {tipo_accion} ahora")
            self.cambiar_estado_btn(True, tipo_accion)
        else:
            messagebox.showerror(title="...! Verifica por favor..!",
                                 message=f"...El registro no fue encontrado, no es posible {tipo_accion} el registro...")
            self.cambiar_estado_btn(False, tipo_accion)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()