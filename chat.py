# importar o flet
import flet as ft



# criar a função principal do app
def main(pagina):
    # cria o elemento
    titulo = ft.Text("Penke ZAP")
    titulo_janela = ft.Text("Bem vindo ao Penke Zap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no site")

    chat = ft.Column()
    campo_mensagem = ft.TextField(label="Digite sua mensagem")

    def enviar_mensagem(evento):
        print("Mensagem enviada")

    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem,botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)

        pagina.update()
        print("Entrei no char")

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        
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