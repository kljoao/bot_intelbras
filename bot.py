from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import customtkinter

janela = customtkinter.CTk()
janela.geometry("400x200")

# Configurações de e-mail
email_user = ''
email_password = ''

# Definindo as variáveis como globais
global email_alerta
global nome_usuario
global email_enviado  # Adicione esta linha

email_enviado = False  # Inicialize a variável email_enviado como False

def click():
    global email_alerta
    global nome_usuario

    # Atribuir os valores dos campos de entrada às variáveis globais
    email_alerta = email_alerta_entry.get()
    nome_usuario = nome_usuario_entry.get()

    # Fechar a janela
    janela.destroy()

    # Imprimir os valores preenchidos
    print("E-mail Receptivo:", email_alerta)
    print("Usuário em Alerta:", nome_usuario)

texto = customtkinter.CTkLabel(janela, text="Inserir Usuário Alerta")
texto.pack(padx=10, pady=10)

email_alerta_entry = customtkinter.CTkEntry(janela, placeholder_text="E-mail para receber o alerta", width=250)
email_alerta_entry.pack(padx=10, pady=10)

nome_usuario_entry = customtkinter.CTkEntry(janela, placeholder_text="Nome do usuário cadastrado", width=250)
nome_usuario_entry.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Cadastrar", command=click)
botao.pack(padx=10, pady=10)

janela.mainloop()

email_destinatario = email_alerta

usuarioAlerta = nome_usuario

def enviar_email():
    global email_enviado

    # Se o e-mail já foi enviado, saia da função
    if email_enviado:
        return

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_destinatario
    msg['Subject'] = 'ALERTA DE USUÁRIO - SERVIÇO FACIAL'

    corpo_email = f"""
    <html>
    <body>
        <p>Olá, FULANO</p>
        <p>Verificamos que o usuário {usuarioAlerta} teve acesso o serviço de biometria</p>
    </body>
    <html>
    """

    msg.attach(MIMEText(corpo_email, 'html'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_destinatario, msg.as_string())

    email_enviado = True  # Defina email_enviado como True após o envio do e-mail

# Configurações do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximizar a janela do navegador
driver = webdriver.Chrome(options=options)

url = "https://localhost:4445/"

# Acessar a página
driver.get(url)

# Esperar até que o elemento de login esteja presente
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input_login_usuario"]')))

# Preencher o formulário de login
driver.find_element(By.XPATH, '//*[@id="input_login_usuario"]').send_keys('admin')
driver.find_element(By.XPATH, '//*[@id="input_login_senha"]').send_keys('admin')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/mat-sidenav-container/mat-sidenav-content/div/div/div/form/div[5]/div/button').click()

# Esperar até que a div principal seja carregada
modal = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/app-popup-primeiros-passos/p-dialog/div/div[1]/a')))
modal.click()


while True:
    try:
        # Verificar se o nome do usuário está presente
        nome_xpath = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[3]/div/span[1]')))
        nome = nome_xpath.text
        if nome == nome_usuario and not email_enviado:  # Adicione esta linha
            enviar_email()
        
        # Aguardar um intervalo de tempo antes de recarregar a página
        time.sleep(10)  # Aguardar 10 segundos antes de verificar novamente
    except Exception as e:
        print("Erro:", e)
        print("Reiniciando o WebDriver...")
        driver.quit()
        driver = webdriver.Chrome(options=options)
        continue
