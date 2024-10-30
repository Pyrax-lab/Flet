import flet as ft
import time




def main(page: ft.Page):
   

   def add_cliked(e):
      page.add(ft.Checkbox(label=new_task.value))
      new_task.value = ""
      new_task.focus()
      new_task.update()


   new_task = ft.TextField(hint_text="Задача", width=300)
   page.add(ft.Row([new_task, ft.ElevatedButton("Добавить задачу", on_click=add_cliked, visible=False)]))

    
ft.app(main)
