# importar o flet
import flet as ft

def iniciar_chat(evento):
    print("Iniciar Chat")

# criar a função principal do app
def main(pagina):
    # cria o elemento
    titulo = ft.Text("Penke ZAP")
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    # adiciona o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)
# rodar app
ft.app(main, view=ft.WEB_BROWSER)