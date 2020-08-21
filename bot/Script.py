from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import json
import datetime

class Bot:
	today = datetime.date.today()
	final_date = datetime.date(2020, 9, 23)

	if today < final_date:
		print(f'Today: {today}')
		with open('/Program Files/Instagram/config.json', 'r') as config:
			data = json.load(config)

		usuario = data['email']
		senha = data['senha']
		pesquisar = data['seguir_seguidores']
		mensagem_a_enviar = data['mensagem_a_enviar']
		meuperfil = data['meu_perfil']
		#Booleans
		seguir = data['seguir'] 
		desseguir = data['desseguir']
		mensagem_boas_vindas = data['mensagem_boas_vindas']
		mensagem_aos_seguidores = data['mensagem_aos_seguidores']


		# autentic_2_fact = data['codigos_autenticacao_2_factores']

		def type_like_a_person(sentence, single_input_field):
			print("going to start typing message into message share text area...")
			for letter in sentence:
			    single_input_field.send_keys(letter)
			    sleep(randint(1, 5) / 12)

		navegador = webdriver.Firefox(executable_path=r'./geckodriver.exe')
		navegador.get('https://www.instagram.com')
		print('entered in the site')

		def login():
			global navegador
			global usuario
			global senha
			sleep(15)
			if usuario != '' and senha != '':
				campo_email = navegador.find_elements_by_tag_name('input')[0]
				campo_email.click()
				type_like_a_person(usuario, campo_email)

				campo_senha = navegador.find_elements_by_tag_name('input')[1]
				campo_email.click()
				type_like_a_person(senha, campo_senha)

				sleep(1)
				botao_login = navegador.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
				botao_login.click()
				print('login done.')
				# sleep(randint(10,20))
				# campo_autenticacao = navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input')
				# type_like_a_person(autentic_2_fact, campo_autenticacao)
				# sleep(randint(20,30) / 3)
				# botao_enviar_2fact = navegador.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
				# botao_enviar_2fact.click()
				sleep(randint(100,140) /2)
				print('Waiting 90-120 seconds to you to type your two-step authentication if required.')
			else:
				print('Cant login, you did not gave me valid login passwords and email.')


		def seguir():
			global seguir

			if seguir != False:
				global navegador
				global pesquisar
				resultado = navegador.get(f'https://www.instagram.com/{pesquisar}')
				print(f"entered in {pesquisar}'s page. ")

				sleep(randint(15,30) / 3)
				seguidores = navegador.find_element_by_xpath("//a[@class='-nal3 ']")
				seguidores.click()
				print(f"clicked {pesquisar}'s followers. ")

				sleep(randint(12,30) / 3)
				popup = navegador.find_element_by_xpath("//div[@class='isgrP']")
				numeros_de_scrolls = 0
				for i in range(randint(4,6)):
					navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
					numeros_de_scrolls += 1
					print(f'scrolled down {numeros_de_scrolls} times')
					sleep(randint(3,9) / 2)

				sleep(randint(15,30) / 3)
				botoes_seguir = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
				# botoes_seguindo = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")

				seguidos = 0
				for i in range(0, randint(15,25)):
					botoes_seguir[i].click()
					seguidos += 1
					print(f'{seguidos} people followed')
					sleep(randint(3,30) / 5)

				navegador.execute_script('window.history.go(-1)')
				print(f"Returned to {pesquisar}'s page.")
				sleep(randint(5,10) / 2)

			else:
				print('I will not follow anyone because you said me to not.')


		def mensagem():
			global mensagem_boas_vindas
			if mensagem_boas_vindas == True:
				global navegador
				global mensagem_a_enviar

				navegador.get('https://www.instagram.com/accounts/activity/')
				print('Going to your recent activities.')
				sleep(randint(40, 60) / 4) #para dar tempo para carregar

				xpath = "*//div[@class='YFq-A']"
				# condicoes_ignoradas = (NoSuchElementException, StaleElementReferenceException)
				# actividades = WebDriverWait(navegador, 30, ignored_exceptions=condicoes_ignoradas).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
				# print(f'Achei {len(actividades)} actividades no seu feed e dessas, {len(comecaram_a_seguir)} comecaram a seguir-lhe')
				
				usuarios = []
				usuario_enviado = {}
				sleep(2)

				for i in range(0,5):
					usuario_enviado.clear()
					try:
						print(f'Executing the number {i}')
						sleep(8)
						actividades = navegador.find_elements_by_xpath("//div[@class='YFq-A']")
						comecaram_a_seguir = []
						sleep(2)
						for elem in actividades:
							if 'seguir-te' in elem.text:
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

						with open('mensagens_enviadas.json', 'r') as file:
							data = json.load(file)

						if usuario_enviado in data:
							print('I have alredy sent this message to this person!')
						else:
							try:
								data.append(usuario_enviado)
								with open('mensagens_enviadas.json', 'w') as ficheiro:
									json.dump(data, ficheiro, indent=2)
							except:
								pass
								# ficheiro.write(usuario)
								# ficheiro.write('\n')
							print(f'Sending {mensagem_a_enviar} a {usuario}')

							print(f'O lenght of people if loaded now is {len(comecaram_a_seguir)}')

							sleep(8)
							comecaram_a_seguir[i].click()
							print('Clicked in a new followers page.')

							sleep(randint(20, 40) / 3)
							try:
								perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
								perfil_enviar_mensagem.click()
								print("Entered in a person's page.")

							except NoSuchElementException:
								print('Oh the account is private!')
								navegador.execute_script('window.history.go(-1)')
								print('returning to the previous page.')

							except:
								perfil_seguir = navegador.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
								perfil_seguir.click()
								print('Followed the person.')
								sleep(randint(15, 25) / 3)
								perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
								perfil_enviar_mensagem.click()
								print("Entered in the person's chat.")
								
							sleep(randint(25, 40) / 3)
							try:
								text_area = navegador.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
							except:
								pass
								text_area = navegador.find_element_by_xpath("div[class='                    Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ']")

							type_like_a_person(mensagem_a_enviar, text_area)
							sleep(randint(10, 20) / 2)

							text_area_botao = navegador.find_elements_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
							
							botao_enviar = navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
							botao_enviar.click()
							print('message sent.')
							
							sleep(randint(8, 20) / 2)
							navegador.execute_script('window.history.go(-1)')
							print("Retorned to person's page.")

							sleep(randint(8, 16) / 2)
							navegador.execute_script('window.history.go(-1)') # retornou a pagina de atividades para repetir o loop!
							sleep(randint(16, 24) / 2)
							print('Returned to your activities.')

					except:
						pass

			else:
				print('Not going to send any message to incoming followers because you said me to not or you didnt gave me a message to send.')

		def desseguir():
			global desseguir

			if desseguir != False:
				global navegador
				meu_perfil = navegador.get(f'https://www.instagram.com/{meuperfil}')
				print('entering in your main page.')
				sleep(randint(50, 100) / 7)

				a_seguir = navegador.find_elements_by_xpath("//a[@class='-nal3 ']")[1]
				a_seguir.click()
				print('entered in the list of people that you are following.')

				sleep(randint(30, 60) / 5)
				popup = navegador.find_element_by_xpath("//div[@class='isgrP']")
				numeros_de_scrolls = 0
				for i in range(randint(2,6)):
					navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
					numeros_de_scrolls += 1
					print(f'scrolled down {numeros_de_scrolls} times')
					sleep(randint(5,9) / 3)

				sleep(randint(50, 100) / 15)
				botoes_seguindo = navegador.find_elements_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")

				desseguidos = 0
				try:
					for i in range(0, randint(15,25)): #cuidado para nao quebrar o script
						botoes_seguindo[i].click()
						sleep(randint(10, 15) / 3)
						desseguir_confirmar = navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
						desseguir_confirmar.click()
						desseguidos += 1
						print(f'Unfollowed {desseguidos} persons.')
						sleep(randint(20,30) / 4)

					navegador.execute_script('window.history.go(-1)')
					navegador.execute_script('window.history.go(-1)')

				except:
					pass
					navegador.execute_script('window.history.go(-1)')
					navegador.execute_script('window.history.go(-1)')

			else:
				print('I am not going to unfollow anyone today because you said me not do it.')



		def mensagem_seguidores():
			global mensagem_aos_seguidores
			global navegador
			global mensagem_a_enviar
			global rotina
			if mensagem_aos_seguidores == True and mensagem_a_enviar !='\n':
				usuario = []
				navegador.get(f'https://www.instagram.com/mentalidade_de_homem/')
				print('entering in your main page...')
				sleep(randint(20, 35) / 3)
				meus_seguidores = navegador.find_element_by_xpath("//a[@class='-nal3 ']")
				sleep(randint(25, 35) / 3)
				meus_seguidores.click()
				print('clicked in your followers.')
				sleep(randint(25, 35) / 3)
				popup = navegador.find_element_by_xpath("//div[@class='isgrP']")

				numeros_de_scrolls = 0
				for i in range(randint(4,6)):
					try:
						navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
						numeros_de_scrolls += 1
						print(f'scrolei down {numeros_de_scrolls} times')
						sleep(randint(9,15) / 3)
					except:
						pass

				usuario_enviado = {}
				for i in range(0,5):
					usuario_enviado.clear()
					print(f'Executing the number {i}')
					sleep(randint(4,40) / 4)
					try:
						seguidores_perfis = navegador.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
						print(f'Loaded {len(seguidores_perfis)} pages.')
						sleep(2)

						usuario = seguidores_perfis[i].text
						usuario_enviado['nome'] = usuario
						usuario_enviado['mensagem'] = mensagem_a_enviar

						with open('mensagens_enviadas.json', 'r') as file:
							data = json.load(file)

						if usuario_enviado in data:
							print('Oh I already have sent this message to this same follower.')
						else:
							try:
								data.append(usuario_enviado)
								with open('mensagens_enviadas.json', 'w') as ficheiro:
									json.dump(data, ficheiro, indent=2)
							except:
								pass
								# ficheiro.write(usuario)
								# ficheiro.write('\n')
							print(f'Sending {mensagem_a_enviar} to {usuario}')			

							seguidores_perfis[i].click()
							print('entered in your main page.')
							sleep(randint(20,40) / 4)

							try:
								perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
								perfil_enviar_mensagem.click()
								print('entered in your chat.')

							except NoSuchElementException:
								print('Oh this account is private')
								navegador.execute_script('window.history.go(-1)')
								print('retured to previous page.')

							except:
								perfil_seguir = navegador.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
								perfil_seguir.click()
								print('Followed the person.')
								sleep(randint(15, 25) / 3)
								perfil_enviar_mensagem = navegador.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']")
								perfil_enviar_mensagem.click()
								print("Entered in the person's chat.")
							
							sleep(randint(25, 40) / 3)
							try:
								text_area = navegador.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
							except:
								pass
								text_area = navegador.find_element_by_xpath("div[class='                    Igw0E     IwRSH      eGOV_        vwCYk                                        ItkAi                                                                       ']")


							type_like_a_person(mensagem_a_enviar, text_area)
							sleep(randint(10, 20) / 2)

							text_area_botao = navegador.find_elements_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
							
							botao_enviar = navegador.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
							botao_enviar.click()
							print('message sent.')
							
							sleep(randint(8, 20) / 2)
							navegador.execute_script('window.history.go(-1)')
							print('Returned to previous page.')

							sleep(randint(8, 16) / 2)
							navegador.execute_script('window.history.go(-1)')
							sleep(randint(16, 24) / 2)
							print('Retorned to your activities.')

					except:
						pass

			else:
				print('I am not going send message to your followers cause you said me not to, or didnt gave anything to send.')

		times = 0
		while times < 5:
			login()
			seguir()
			desseguir()
			mensagem()
			mensagem_seguidores()
			navegador.quit()
			print('Sleeping... if you do not close this window i will wake up and login again in one hour to repeat automation.')
			sleep(randint(4000, 6000))

	else:
		print('Sorry, your free trial is over. If you want to keep using this bot, please contact @mentalidade_de_homem. Thank you!')

