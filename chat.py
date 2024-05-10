# importar o flet
import flet as ft



# criar a função principal do app
def main(pagina):
    # cria o elemento
    titulo = ft.Text("Penke ZAP")

    def iniciar_chat(evento):
        titulo_janela = ft.Text("Bem vindo ao Penke Zap")
        campo_nome_usuario = ft.TextField(label="Escreva seu nome no site")
        botao_entrar = ft.ElevatedButton("Entrar no chat")
        janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])
        pagina.dialog = janela
        janela.open = True
        pagina.update()        
        print("Iniciar Chat")

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    # adiciona o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)
# rodar app
ft.app(main, view=ft.WEB_BROWSER)