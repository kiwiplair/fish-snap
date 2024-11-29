import flet as ft
import data.questions as questions
import random


def IndexView(page:ft.Page, params):
    def update_score(s):
        nonlocal score
        score+=s
        score_text.value="Score: " + str(score)

    def submit_clicked(e):
        nonlocal  score

        user_answer=user_input.value.strip().upper()
        if user_answer in lst_user_answers:
            return
        print(user_answer)
        answers= questions.get_answers(question_index)
        i=0
        valid = False
        for ans,point in answers:
            ans=ans.upper()
            if user_answer == ans:
                valid = True


                for j in range( len(ans)):
                    lst_answer_boxes[i][j].content.value = ans[j].upper()
                    lst_answer_boxes[i][j].bgcolor = ft.colors.SURFACE


                break
            i+=1

        if valid:
            lst_user_answers.append(user_answer)
            update_score(point)
            user_input.value= ""
            user_input.focus()
        page.update()

        print(answers)

    def new_round(index):
       question_image.src = "game_images\\" + questions.get_image_url(index)
       question_image.width=750
       question_image.height = 450

       answers = questions.get_answers(index)
       answers_column.controls.clear()
       for answer_text, point in answers:
               row= ft.Row()
               L1 =[]
               #go to each alphabet of the answer
               counter=0
               for x in answer_text:
                   if counter==0:
                       txt=x
                   else:
                       txt=" "
                   letter = ft.Text(txt.upper())
                   con=ft.Container(content=letter,bgcolor=ft.colors.PRIMARY_CONTAINER, width=30,height=30,
                                    alignment=ft.alignment.center, animate=ft.Animation(2000))
                   row.controls.append(con)
                   L1.append(con)
                   counter+=1
               lst_answer_boxes.append(L1)
               score_box=ft.Text("+" + str(point))
               row.controls.append(score_box)
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

        i= random.randrange(0,len(questions.all_questions))
        new_round(i)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")


    #Game variables
    question_index =3
    score = 0


    lst_answer_boxes = []
    #create controls
    lst_user_answers=[]
    submit_button = ft.OutlinedButton("submit",on_click=submit_clicked )
    question_image = ft.Image(src="game_images/beach.jpg", width=600)
    user_input=ft.TextField(label="enter a word:", on_submit= submit_clicked)
    txt=ft.Text("right")
    answers_column=ft.Column()
    left_column= ft.Column(controls = [question_image, user_input,submit_button], alignment=ft.alignment.top_center)
    right_column=ft.Column(controls=[answers_column])
    score_text = ft.Text("Score: 0",size=30,color=ft.colors.TERTIARY)
    score_row=ft.Row(controls=[score_text])
    line_1 = ft.Divider(height=1, color=ft.colors.SECONDARY_CONTAINER)

    main_row=ft.Row(controls=[left_column,right_column], vertical_alignment=ft.CrossAxisAlignment.START)
    appbar = CreateAppBar()

    new_round(question_index)
    page.views.append(ft.View(
        "/",
        [appbar,score_row, line_1, main_row
],

    )
    )
    page.update()
