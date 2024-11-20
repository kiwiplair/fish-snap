import flet as ft

def IndexView(page:ft.Page, params):
    def CreateAppBar():
        app_bar = ft.AppBar(
            leading=ft.Image("images/csc_logo_100.png"),
            leading_width=40,
            title=ft.Text("Fish Snap"),
            #center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.RESTART_ALT, on_click=restart_clicked),
                ft.IconButton(ft.icons.FILTER_3),

            ],
        )
        return app_bar

    def restart_clicked(e):
         dlg = ft.AlertDialog(title=ft.Text("You clicked restart"))
         page.open(dlg)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")




    #create controls
    submit_button = ft.OutlinedButton("submit")
    img_1 = ft.Image(src="images/m1.jpg", width=300)
    user_input=ft.TextField(label="enter a word:")
    txt=ft.Text("right")
    left_column= ft.Column(controls = [img_1, user_input,submit_button])
    right_column=ft.Column(controls=[txt])
    main_row=ft.Row(controls=[left_column,right_column])
    appbar = CreateAppBar()


    page.views.append(ft.View(
        "/",
        [appbar, main_row],

    )
    )
    page.update()
