import flet as ft
import PyPDF2


def main(page: ft.Page):
    page.window_center()
    page.window_height = 500
    page.window_width = 500
    # page.bgcolor = ft.colors.BLUE_900

    page.update()
    page.title = "Manage PDF Documents"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # upload_url = page.get_upload_url("dir/filename.ext", 60)
    files_update = []
    
    name_new_file = ft.TextField(label='Nombre del pdf nuevo',
                                border_color=ft.colors.BLUE_900,
                                )
    def merge_pdf(e):
        cantidad = len(files_update[0])
        pdf_merger = PyPDF2.PdfWriter()
        for i in files_update[0]:
            print(files_update[0][0].path)
            f = open(str(i.path),'rb')
            pdf_merger.append(f)
            
        pdf_merger.write(f'{name_new_file.value}.pdf')
        for i in files_update[0]:
            print(files_update[0][0].path)
            f = open(str(i.path),'rb')
            f.close()
            
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        files_update.append(e.files)
        

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    def button_clicked(e):
        if cg.value == '1':
            page.clean()
            h1_unir = ft.Row(
                [
                    ft.Text("Sube los pdf que quieras unir", size=20),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
            btn_files = ft.Row(
            [
                ft.ElevatedButton(
                    "Subir archivos",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
            btn_sleec = ft.ResponsiveRow(
        [
            selected_files,
            name_new_file,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
            btn_merge = ft.Row(
        [
            ft.ElevatedButton(
                    "Unir",
                    icon=ft.icons.MERGE,
                    on_click=merge_pdf
                ),],alignment=ft.MainAxisAlignment.CENTER,
        )
            page.add(ft.IconButton(icon=ft.icons.ARROW_BACK,
                    icon_color="blue400",
                    tooltip="Back",
                    on_click="Back",),
                    h1_unir,
                    btn_files,
                    btn_sleec,
                    btn_merge)
            
        elif cg.value == '2':
            page.clean()
            page.add(ft.Text('Dividir'))
        elif cg.value == '3':
            page.clean()
            page.add(ft.Text('Texto'))
        page.update()

    title_gp = ft.Row(
        [
            ft.Text("Documents PDF", size=50),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    h1_gp = ft.Row(
        [
            ft.Text("Que quisieras hacer con los pdf? ", size=20),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    t = ft.Text()
    b = ft.Row(
        [
            ft.ElevatedButton(text='Enter', on_click=button_clicked)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    cg = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="1", label="Unir"),
        ft.Radio(value="2", label="Dividir",disabled=True),
        ft.Radio(value="3", label="Texto",disabled=True),
    ],
        alignment=ft.MainAxisAlignment.CENTER,)
    )

    page.add(title_gp, h1_gp, cg, b, t)

ft.app(target=main, upload_dir="uploads")
