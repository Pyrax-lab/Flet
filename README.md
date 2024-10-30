# Flet — это инструмент для быстрого создания веб-интерфейсов с использованием Python. Он упрощает создание интерактивных элементов без необходимости глубоко погружаться в HTML, CSS или JavaScript. Идеально подходит для быстрого прототипирования и создания административных панелей. Легок и удобен в использовании.


## В данном репозитории будут лежать примеры использования flet с подробным описанием **типа документации но на русском с разными примерами**



1. Реализация To Do приложения 


`def main(page: ft.Page):`
   

   `def add_cliked(e):`
      `page.add(ft.Checkbox(label=new_task.value))`
      `new_task.value = ""`
      `new_task.focus()`
      `new_task.update()`


   `new_task = ft.TextField(hint_text="Задача", width=300)`
   `page.add(ft.Row([new_task, ft.ElevatedButton("Добавить задачу", on_click=add_cliked)]))`1

    
`ft.app(main)`