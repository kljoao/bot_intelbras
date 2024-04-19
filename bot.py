from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.common.exceptions import StaleElementReferenceException
import smtplib
import time
import customtkinter

janela = customtkinter.CTk()
janela.geometry("400x350")

# Configurações de e-mail
email_user = ''
email_password = ''

# Definindo as variáveis como globais
global email_alerta
global nome_usuario

def click():
    global email_alerta
    global nome_usuario

    # Atribuir os valores dos campos de entrada às variáveis globais
    email_alerta = email_alerta_entry.get()
    nome_usuario = nome_usuario_entry.get().split(", ")

    # Fechar a janela
    janela.destroy()

    # Imprimir os valores preenchidos
    print("E-mail Receptivo:", email_alerta)
    print("Usuário em Alerta:", nome_usuario)

# Configurações E-mail remetente - INICIO
configuracoes = customtkinter.CTkLabel(janela, text="Configurações E-mail Remetente")
configuracoes.pack(padx=10, pady=10)

email_remetente_entry = customtkinter.CTkEntry(janela, placeholder_text="E-mail remetente", width=250)
email_remetente_entry.pack(padx=10, pady=10)

email_remetente_senha_entry = customtkinter.CTkEntry(janela, placeholder_text="Senha do E-mail Remetente", width=250)
email_remetente_senha_entry.pack(padx=10, pady=10)
# Configurações E-mail remetente - FIM

# Configurações Destinatário - INICIO

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

def enviar_email(nome_acesso):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_destinatario
    msg['Subject'] = 'ALERTA DE USUÁRIO - SERVIÇO FACIAL'

    corpo_email = f"""
    <html>
    <body>
        <p>Olá, FULANO</p>
        <p>Verificamos que o usuário {nome_acesso} teve acesso o serviço de biometria</p>
    </body>
    <html>
    """

    msg.attach(MIMEText(corpo_email, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email_destinatario, msg.as_string())
    except smtplib.SMTPException as e:
        print("Erro ao enviar o e-mail:", e)
        return  # Se ocorrer um erro, saia da função


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

time.sleep(20)

# Armazenar os valores iniciais da data, hora e nome do card
data_anterior = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[1]').text
hora_anterior = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[2]').text
nome_anterior = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[3]/div/span[1]').text


while True:
    try:
        # Verificar se os elementos ainda estão presentes na página
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[1]')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[2]')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[3]/div/span[1]')))
        
        # Capturar os novos valores da data, hora e nome do card
        nova_data = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[1]').text
        nova_hora = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[1]/div[2]').text
        novo_nome = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div/app-menu/div/mat-sidenav-container/mat-sidenav[2]/div/app-sidebar/div/mat-sidenav-container/mat-sidenav/div/div/div[1]/div/div[3]/div/span[1]').text
        
        # Dividir a string de novo_nome em uma lista de nomes
        novo_usuario_lista = novo_nome.split(", ")
        
        # Verificar se algum nome na lista corresponde ao nome específico
        if any(nome in novo_usuario_lista for nome in nome_usuario):
            # Verificar se houve alguma alteração na data ou na hora do card
            if nova_data != data_anterior or nova_hora != hora_anterior:
                for nome in novo_usuario_lista:
                    if nome in nome_usuario:
                        enviar_email(nome)  # Se houver alteração, enviar o e-mail de alerta
                        break
                
                # Atualizar os valores anteriores para os novos valores
                data_anterior = nova_data
                hora_anterior = nova_hora
        
        # Aguardar um intervalo de tempo antes de recarregar a página
        time.sleep(3)  # Aguardar 3 segundos antes de verificar novamente
    except StaleElementReferenceException:
        # Se um elemento se tornou obsoleto, atualize os valores anteriores e continue
        data_anterior = nova_data
        hora_anterior = nova_hora
        continue
    except Exception as e:
        print("Erro:", e)
        print("Reiniciando o WebDriver...")
        driver.quit()
        driver = webdriver.Chrome(options=options)
        continue