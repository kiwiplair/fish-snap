import flet as ft
import data.questions as questions
def IndexView(page:ft.Page, params):
    def new_round(question):
       question_image.src = "game_images\\" + question[0]
       for i in range(1,len(question)):
               row= ft.Row()
               #go to each alphabet of the answe
               for x in question[i]:
                   letter = ft.Text(x.upper())
                   row.controls.append(letter)
               answers_column.controls.append(row)
       page.update()
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
    question_image = ft.Image(src="game_images/beach.jpg", width=600)
    user_input=ft.TextField(label="enter a word:")
    txt=ft.Text("right")
    answers_column=ft.Column()
    left_column= ft.Column(controls = [question_image, user_input,submit_button])
    right_column=ft.Column(controls=[answers_column])
    main_row=ft.Row(controls=[left_column,right_column])
    appbar = CreateAppBar()
    new_round(questions.all_questions[0])
    page.views.append(ft.View(
        "/",
        [appbar, main_row,
],

    )
    )
    page.update()
