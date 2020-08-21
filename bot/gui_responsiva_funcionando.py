from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import os
import json
import datetime
import PySimpleGUI as sg
from config import definicoes
from read_dms import read
from download_gecko import baixardriver
import queue
import threading
import pickle

if os.path.isdir('/Program Files/Instagram') == False:
	os.mkdir('/Program Files/Instagram')

baixardriver()

try:
	with open('/Program Files/Instagram/mensagens_enviadas.json', 'r') as file:
		data = json.load(file)
except:
	usuarios = []
	usuario_enviado = {}

	usuario_enviado['nome'] = 'Example1'
	usuario_enviado['mensagem'] = 'example1'
	usuarios.append(usuario_enviado.copy())

	usuario_enviado['nome'] = 'Example2'
	usuario_enviado['mensagem'] = 'example2'
	usuarios.append(usuario_enviado.copy())

	with open('/Program Files/Instagram/mensagens_enviadas.json', 'w') as file:
		json.dump(usuarios, file, indent=2)

	with open('/Program Files/Instagram/mensagens_enviadas.json', 'r') as file:
		data = json.load(file)

try:
	with open('/Program Files/Instagram/config.json', 'r') as config:
		data = json.load(config)
except FileNotFoundError:
	dicionario = {}
	dicionario['email'] = 'myemail@mail.com'
	dicionario['senha'] = 'secretpassword'
	dicionario['seguir_seguidores'] = 'influencer_username'
	dicionario['meu_perfil'] = 'my_account_username'
	dicionario['seguir'] = True
	dicionario['desseguir'] = False
	dicionario['mensagem_boas_vindas'] = False
	dicionario['mensagem_aos_seguidores'] = False
	dicionario['mensagem_a_enviar'] = '\n'
	dicionario['mensagem_a_lista'] = '\n'

	with open('/Program Files/Instagram/config.json', 'w') as config:
		json.dump(dicionario, config, indent=2)

	with open('/Program Files/Instagram/config.json', 'r') as config:
		data = json.load(config)

usuario = data['email']
senha = data['senha']
pesquisar = data['seguir_seguidores']
mensagem_a_enviar = data['mensagem_a_enviar']
meuperfil = data['meu_perfil']
seguir = data['seguir'] 
desseguir = data['desseguir']
mensagem_boas_vindas = data['mensagem_boas_vindas']
mensagem_aos_seguidores = data['mensagem_aos_seguidores']
mensagem_a_lista = data['mensagem_a_lista']
profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'pt') #pt-BR
navegador = webdriver.Firefox(executable_path=r'/Program Files/Instagram/geckodriver.exe',firefox_profile=profile)
login_feito = False

# def load_cookie(navegador, path):
# 	with open(path, 'rb') as cookiesfile:
# 		cookies = pickle.load(cookiesfile)
# 		for cookie in cookies:
# 			navegador.add_cookie(cookie)

# load_cookie(navegador, '/Program Files/Instagram/cookies.pkl')

def long_operation_thread():
	global navegador

	try:
		today = datetime.date.today()
		agora = datetime.datetime.now()

		try:
			with open('/Program Files/Instagram/datas.json', 'r') as file:
				hoje = json.load(file)
		except:
			hoje = False

		if hoje == '' or hoje == False:
			hoje = datetime.date.today()

			# datetime to strings
			hoje = datetime.datetime.strftime(hoje, '%Y-%m-%d')

			nasceu = {}
			nasceu['dia'] = hoje

			with open('/Program Files/Instagram/datas.json', 'w') as file:
				json.dump(nasceu, file)

			with open('/Program Files/Instagram/datas.json', 'r') as file:
				a =  json.load(file)
				# print(a['dia'])

			# string to datetime
			dia = datetime.datetime.strptime(a['dia'], '%Y-%m-%d')

		else:
			pass
			# print('Ficheiro datas.json ja existe')

		with open('/Program Files/Instagram/datas.json', 'r') as file:
			a =  json.load(file)

		# string to datetime
		dia = datetime.datetime.strptime(a['dia'], '%Y-%m-%d')

		semana = datetime.timedelta(days=7)
		final_date =  dia + semana

		if agora < final_date:
			print('Bot is starting...')
			print(f'Today: {agora}')
			print('Please, do not press any button in this window or browser during automation...')

			def type_like_a_person(sentence, single_input_field):
				print("going to start typing message into message share text area...")
				for letter in sentence:
				    single_input_field.send_keys(letter)
				    sleep(randint(1, 5) / 12)

			def dormir(minimo, maximo):
				for i in range(randint(minimo, maximo)):
					sleep(0.1)

			def printar(texto):
				print(texto)

			def passarpopus():
				# piCib -> CLASSE DA DIV DO POPUP SEM ESPACOS:)
				global navegador
				try:
					sleep(8)
					print('Looking for popus')
					botaopop = navegador.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')
					botaopop.click()
					print('Clicked in a popup')
				except:
					print('No popup found')

			def login():
				global login_feito
				global navegador
				global usuario
				global senha
				dormir(30,80)
				navegador.get('https://www.instagram.com')
				dormir(140,160)

				if login_feito == False:
					printar('entered in the site')
					dormir(140,160)
					if usuario != '' and senha != '':
						campo_email = navegador.find_elements_by_tag_name('input')[0]
						campo_email.click()
						type_like_a_person(usuario, campo_email)

						campo_senha = navegador.find_elements_by_tag_name('input')[1]
						campo_email.click()
						type_like_a_person(senha, campo_senha)
						
						dormir(10,30)
						botao_login = navegador.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
						botao_login.click()
						printar('login done.')
						printar('Waiting 60-90 seconds to you to type your two-step authentication if required.')
						# sleep(randint(10,20))
						# campo_autenticacao = navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input')
						# type_like_a_person(autentic_2_fact, campo_autenticacao)
						# sleep(randint(20,30) / 3)
						# botao_enviar_2fact = navegador.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
						# botao_enviar_2fact.click()
						dormir(100,150)
						login_feito = True

						# def save_cookie(navegador, path):
						# 	with open(path, 'wb') as filehandler:
						# 		pickle.dump(navegador.get_cookies(), filehandler)
						# 		print('Cookies saved...')

						# save_cookie(navegador, '/Program Files/Instagram/cookies.pkl')
						
					else:
						printar('Cant login, you did not gave me valid login passwords and email.')
				else:
					printar('login already done')
					passarpopus()

			def seguir():
				global seguir

				if seguir != False:
					global navegador
					global pesquisar
					resultado = navegador.get(f'https://www.instagram.com/{pesquisar}')
					printar(f"entered in {pesquisar}'s page. ")

					dormir(50, 150)
					seguidores = navegador.find_element_by_xpath("//a[@class='-nal3 ']")
					seguidores.click()
					printar(f"clicked {pesquisar}'s followers. ")
					passarpopus()
				
					dormir(40, 100)
					popup = navegador.find_element_by_xpath("//div[@class='isgrP']")
					numeros_de_scrolls = 0
					for i in range(randint(4,6)):
						navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
						numeros_de_scrolls += 1
						print(f'scrolled down {numeros_de_scrolls} times')
						dormir(20,40)

					dormir(50,100)
					botoes_seguir = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
					# botoes_seguindo = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")

					seguidos = 0
					for i in range(0, randint(10,12)):
						botoes_seguir[i].click()
						passarpopus()
						seguidos += 1
						print(f'{seguidos} people followed')
						dormir(10,60)

					navegador.execute_script('window.history.go(-1)')
					print(f"Returned to {pesquisar}'s page.")
					dormir(20,50)

				else:
					printar('I will not follow anyone because you said me to not.')


			def mensagem():
				global mensagem_boas_vindas

				with open('/Program Files/Instagram/config.json') as config_file:
					d = json.load(config_file)
					mensagem = d['mensagem_a_enviar']

				abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
				mensagem_lista = []

				for item in mensagem:
					mensagem_lista.append(item)

				match = False
				for elem in mensagem_lista:
					if elem in abecedario:
						match = True
						
				if mensagem_boas_vindas == True:
					if match == True:
						global navegador
						global mensagem_a_enviar

						navegador.get('https://www.instagram.com/accounts/activity/')
						printar('Going to your recent activities.')
						dormir(100,150)

						xpath = "*//div[@class='YFq-A']"
						# condicoes_ignoradas = (NoSuchElementException, StaleElementReferenceException)
						# actividades = WebDriverWait(navegador, 30, ignored_exceptions=condicoes_ignoradas).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
						# print(f'Achei {len(actividades)} actividades no seu feed e dessas, {len(comecaram_a_seguir)} comecaram a seguir-lhe')
						
						usuarios = []
						usuario_enviado = {}
						sleep(2)

						i = 0
						enviados = 0
						while i < 500:
							if enviados == 15:
								break

							usuario_enviado.clear()
							try:
								printar(f'Executing {i+1} time')
								dormir(80,90)
								actividades = navegador.find_elements_by_xpath("//div[@class='YFq-A']")
								comecaram_a_seguir = []
								dormir(20,30)
								for elem in actividades:
									if 'seguir' or 'started' in elem.text:
										comecaram_a_seguir.append(elem)
								try:
									texto = comecaram_a_seguir[i].text
									texto_em_lista = texto.split(' ')
									usuario_com_comecou = texto_em_lista[0]
									usuario_com_comecou_lista = usuario_com_comecou.split('\n')
									usuario = usuario_com_comecou_lista[0]
									usuario_enviado['nome'] = usuario
									usuario_enviado['mensagem'] = mensagem_a_enviar
									usuarios.append(usuario_enviado.copy())
								except:
									pass

								with open('/Program Files/Instagram/mensagens_enviadas.json', 'r') as file:
									data = json.load(file)

								if usuario_enviado in data:
									printar(f'I have alredy sent {mensagem_a_enviar} to {usuario}')

								else:
									try:
										data.append(usuario_enviado)
										with open('/Program Files/Instagram/mensagens_enviadas.json', 'w') as ficheiro:
											json.dump(data, ficheiro, indent=2)
									except:
										pass

									printar(f'Sending {mensagem_a_enviar} a {usuario}')

									printar(f'I loaded {len(comecaram_a_seguir)} that started following you recently.')

									dormir(80,90)
									comecaram_a_seguir[i].click()
									printar('Clicked in a new followers account.')
									dormir(70,140)
									try:
										try:
											perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
											perfil_enviar_mensagem.click()
											printar("Entered in a person's chat.")
											passarpopus()
										except NoSuchElementException:
											# //button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   '   
											perfil_enviar_mensagem = navegador.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button")
											perfil_enviar_mensagem.click()
											passarpopus()
											printar("Entered in a person's chat.")
									except NoSuchElementException:
										printar('Oh the account is private!')
										navegador.execute_script('window.history.go(-1)')
										printar('returning to the previous page.')

									except:
										perfil_seguir = navegador.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
										perfil_seguir.click()
										passarpopus()
										printar('Followed the person.')
										dormir(50,70)
										perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
										perfil_enviar_mensagem.click()
										passarpopus()
										printar("Entered in the person's chat.")
										
									dormir(70,120)
									try:
										text_area = navegador.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
									except:
										pass
										text_area = navegador.find_element_by_xpath("div[class='                    Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ']")

									type_like_a_person(mensagem_a_enviar, text_area)
									dormir(50,100)

									text_area_botao = navegador.find_elements_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
									
									botao_enviar = navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
									botao_enviar.click()
									printar('message sent.')
									
									dormir(40,100)
									navegador.execute_script('window.history.go(-1)')
									printar("Retorned to person's page.")

									dormir(40,80)
									navegador.execute_script('window.history.go(-1)') # retornou a pagina de atividades para repetir o loop!
									dormir(80,160)
									printar('Returned to your activities.')

									enviados += 1
							except:
								pass

							i += 1

					else:
						printar('Not going to send any welcome message because you did not give me welcome message to send.')
				else:
					printar('Not going to send any welcome message to incoming followers because you said me to not.')

			def desseguir():
				global desseguir

				if desseguir == True:
					global navegador
					meu_perfil = navegador.get(f'https://www.instagram.com/{meuperfil}')
					printar('entering in your main page.')
					dormir(120,180)
					passarpopus()

					a_seguir = navegador.find_elements_by_xpath("//a[@class='-nal3 ']")[1]
					a_seguir.click()
					printar('entered in the list of people that you are following.')
					passarpopus()
					dormir(15,45)
					popup = navegador.find_element_by_xpath("//div[@class='isgrP']")
					numeros_de_scrolls = 0
					for i in range(randint(2,6)):
						navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
						numeros_de_scrolls += 1
						printar(f'scrolled down {numeros_de_scrolls} times')
						dormir(20,40)

					dormir(50,200)
					botoes_seguindo = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")

					desseguidos = 0
					try:
						for i in range(0, randint(10,12)): #cuidado para nao quebrar o script
							botoes_seguindo[i].click()
							passarpopus()
							dormir(30,50)
							desseguir_confirmar = navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
							desseguir_confirmar.click()
							desseguidos += 1
							printar(f'Unfollowed {desseguidos} persons.')
							dormir(40,60)

						navegador.execute_script('window.history.go(-1)')
						navegador.execute_script('window.history.go(-1)')

					except:
						navegador.execute_script('window.history.go(-1)')
						navegador.execute_script('window.history.go(-1)')

				else:
					printar('I am not going to unfollow anyone today because you said me not do it.')


			def mensagem_seguidores():
				global mensagem_aos_seguidores
				global navegador
				global mensagem_a_lista
				global rotina

				with open('/Program Files/Instagram/config.json') as config_file:
					d = json.load(config_file)
					mensagem = d['mensagem_a_lista']

				abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
				mensagem_lista = []

				for item in mensagem:
					mensagem_lista.append(item)

				match = False
				for elem in mensagem_lista:
					if elem in abecedario:
						match = True

				if mensagem_aos_seguidores == True:
					if match == True:
						usuario = []
						navegador.get(f'https://www.instagram.com/{meuperfil}/')
						printar('entering in your main page...')
						dormir(70, 120)
						meus_seguidores = navegador.find_element_by_xpath("//a[@class='-nal3 ']")
						dormir(70, 120)
						meus_seguidores.click()
						printar('clicked in your followers.')
						passarpopus()
						# dormir(70, 120)
						popup = navegador.find_element_by_xpath("//div[@class='isgrP']")

						numeros_de_scrolls = 0

						scrolls = 0
						while scrolls < randint(6,9):
							try:
								navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
								numeros_de_scrolls += 1
								printar(f'scrolei down {numeros_de_scrolls} times')
								dormir(30, 50)
								scrolls += 1
							except:
								pass

						usuario_enviado = {}
						enviados = 0
						i = 0
						while i < 500:
							if enviados == 15:
								break
							usuario_enviado.clear()
							printar(f'Executing the number {i}')
							dormir(80,120)
							try:
								seguidores_perfis = navegador.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
								printar(f'Loaded {len(seguidores_perfis)} pages.')
								dormir(10,30)

								usuario = seguidores_perfis[i].text
								usuario_enviado['nome'] = usuario
								usuario_enviado['mensagem'] = mensagem_a_lista

								with open('/Program Files/Instagram/mensagens_enviadas.json', 'r') as file:
									data = json.load(file)

								if usuario_enviado in data:
									printar('Oh I already have sent this message to this same follower.')
								else:
									try:
										data.append(usuario_enviado)
										with open('/Program Files/Instagram/mensagens_enviadas.json', 'w') as ficheiro:
											json.dump(data, ficheiro, indent=2)
									except:
										pass
										
									printar(f'Sending {mensagem_a_lista} to {usuario}')

									seguidores_perfis[i].click()
									printar('entered in your main page.')
									# dormir(50, 100)
									passarpopus()

									try:
										perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
										perfil_enviar_mensagem.click()
										printar('entered in your chat.')
										passarpopus()

									except NoSuchElementException:
										printar('Oh this account is private')
										navegador.execute_script('window.history.go(-1)')
										printar('retured to previous page.')

									except:
										perfil_seguir = navegador.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
										perfil_seguir.click()
										printar('Followed the person.')
										dormir(50, 70)
										perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
										perfil_enviar_mensagem.click()
										printar("Entered in the person's chat.")
										passarpopus()
									
									dormir(70, 120)
									try:
										text_area = navegador.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
									except:
										pass
										text_area = navegador.find_element_by_xpath("div[class='                    Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ']")


									type_like_a_person(mensagem_a_lista, text_area)
									dormir(50, 100)

									text_area_botao = navegador.find_elements_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
									
									botao_enviar = navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
									botao_enviar.click()
									printar('message sent.')
									
									dormir(40, 100)
									navegador.execute_script('window.history.go(-1)')
									printar('Returned to previous page.')

									dormir(40, 80)
									navegador.execute_script('window.history.go(-1)')
									dormir(80, 120)
									printar('Retorned to your activities.')
									enviados += 1
							except:
								pass

							i += 1

					else:
						printar('I am not going to send any messages to your followers because you did not gave any message to send.')
				else:
					printar('I am not going send any message to your followers because you said me not to.')

			times = 0
			while times < 8:
				login()
				seguir()
				desseguir()
				mensagem()
				mensagem_seguidores()
				# navegador.quit()
				printar('Sleeping... if you do not close this window i will wake up and login again in one hour to repeat automation.')
				a = 0
				dormindo = randint(4000,8000) # * 0.1
				printar(f'Sleeping for {int((dormindo / 10) / 60)} minutes...')
				while a < dormindo:
					sleep(0.1)
					a += 1

		else:
			sleep(1.25)
			print('Sorry, your 7 days free trial is over. If you want to use this bot please contact us.')
			# image = interruptor_cinza
			# janela['botao'].update(image_data=image)
	except Exception as e:
		# image = interruptor_cinza
		# janela['botao'].update(image_data=image)
		printar(e)
		printar('Sorry, an unexpected error ocurred, check your network connection.')
		# continue


def the_gui():

	gui_queue = queue.Queue() #ESTA LINHA E IMPORTANTE
	
	sg.ChangeLookAndFeel('LightGrey1')      
	sg.SetOptions(element_padding=(0, 0))      

	menu_def = [['Bot', ['Login Settings']],      
            ['Messages', ['Read']],      
            ['Help', ['About...', 'Users Manual', 'Subscription Status']]]

	interruptor_roxo = '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'
	interruptor_cinza = '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'
	message = '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'
	settings = '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'
	
	image = interruptor_cinza
	image_settings = settings 
	image_messages = message      

	layout = [      
    [sg.Menu(menu_def, )],
    [sg.Button(image_data=image, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='botao'), sg.Button(image_data=image_settings, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='Settings', pad=((375,0), (0,0)), tooltip='settings'),sg.Button(image_data=image_messages, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='messages_sent', pad=((0,0), (0,0)), tooltip='DMs Sent')],      
    [sg.Output(size=(80,20))]
         ]      

	janela = sg.Window("InstagramBot", layout, default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,      
                   default_button_element_size=(12, 1))

	while True:
		button, values = janela.read()

		if button == 'botao':
			if image == interruptor_cinza:
				image = interruptor_roxo
				janela['botao'].update(image_data=image)
			elif image == interruptor_roxo:
				image = interruptor_cinza
				janela['botao'].update(image_data=image)


		if button == sg.WIN_CLOSED:
			break

		if button == 'Settings' or button == 'Login Settings':
			definicoes()

			layout48 = [[sg.Text('Program has to restart in order to load your settings')],
						[sg.Button('Yes, Restart'), sg.Button("No, Don't Save")]
			]

			janela48 = sg.Window('Alert', layout48, modal=True)

			buttons48, values48 = janela48.read()

			if buttons48 == 'Yes, Restart':
				janela48.close()
				janela.close()
				the_gui() #break

			if buttons48 == "No, Don't Save":
				janela48.close()

		if button == 'messages_sent' or button == 'Read':
			read()

		if button == 'Subscription Status':
			sg.Popup('Free Trial')

		if button == 'About...':
			sg.Popup('AutoMarketing.com\n@mentalidade_de_homem\nWe love creating automation tools...')

		if button == 'Users Manual':
			sg.Popup('Please visit our site to read our detailed user manual. If you have some question feel free to contact us.')

		if button == 'botao':
			if image == interruptor_roxo:
				try:
					threading.Thread(target=long_operation_thread, daemon=True).start()
				except Exception as e:
					print('Error starting work thread.')
        
		try:
		    message = gui_queue.get_nowait()
		except queue.Empty:
		    message = None 
		if message:
		    print('Got a message back from the thread: ', message)
			
	janela.close()


if __name__ == '__main__':
    the_gui()
    print('Exiting Program')