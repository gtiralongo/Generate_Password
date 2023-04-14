import flet as ft
import random as r

def main(page: ft.Page):
    page.window_center()
    page.window_height = 550
    page.window_width = 1000
    

    page.update()

    def generate_password(lc,uc,n,s,l):
        lower_case = "abcdefghijklmnñopqrstuvwxyz"
        upper_case = lower_case.upper()
        numbers = "0123456789"
        symbol = "!#$%&/\*+-?¡¿@"
        use_for = ""
        if lc :
            use_for += lower_case
        if uc :
            use_for += upper_case
        if n:
            use_for += numbers
        if s :
            use_for += symbol
        password = "".join(r.sample(use_for,int(l)))
        return password

    page.title = "Generador de Contraseña"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Elementos del layout 
    title_gp = ft.Row(
                [   
                    ft.Text("Generador de Contraseña",size=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
    h1_gp = ft.Row(
                [   
                    ft.Text("Selecciona las catacteristicas de la Contraseña y el largo",size=20),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ) 
    
    # Parametros para el Check box
    c1 = ft.Checkbox(label="Minuscula", value=True)
    c2 = ft.Checkbox(label="Mayusculas", value=False)
    c3 = ft.Checkbox(label="Simbolos", value=False)
    c4 = ft.Checkbox(label="Numeros", value=False)
    check_box = ft.Row(
                [   
                    c1,c2,c3,c4
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ) 
    
    # Parametros para el largo de la clave
    length_password = ft.TextField(value="8", text_align=ft.TextAlign.RIGHT, width=50)
    
    def minus_click(e):
        length_password.value = str(int(length_password.value) - 1)
        page.update()

    def plus_click(e):
        length_password.value = str(int(length_password.value) + 1)
        page.update()
    row = ft.Row(
            [   
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                length_password,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    #Boton para generar clave
    def btn_clean(e):
        page.clean()
        page.add(
                title_gp,
                h1_gp,
                check_box,
                row,
                btn_password 
            )

    # clean_btn = ft.ElevatedButton("Limpiar Contraseña", on_click=btn_clean)

    def btn_generate(e):
        password = generate_password(c1.value,c2.value,c3.value,c4.value,length_password.value)
        password_gp_response = ft.Row(
                [
                ft.Text("Tu contraseña es:"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        password_gp = ft.Row(
                [
                ft.Text(f"{password}",size=30,color=ft.colors.RED,),
                ft.IconButton(icon=ft.icons.COPY, on_click=page.set_clipboard(password),icon_size=20,icon_color=ft.colors.RED_900),
                ],
                alignment=ft.MainAxisAlignment.CENTER,               
            )
        page.add(password_gp_response,password_gp)
    # generate_btn = ft.ElevatedButton("Crear", on_click=btn_generate)
    
    btn_password = ft.Row(
            [   
                ft.ElevatedButton("Crear", on_click=btn_generate),
                ft.ElevatedButton("Limpiar Contraseña", on_click=btn_clean)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    page.add(
        title_gp,
        h1_gp,
        check_box,
        row,
        btn_password 
    )

ft.app(target=main)
