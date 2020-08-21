import PySimpleGUI as sg
import json
from atualizarmensagemboasvindasdoconfig import atualizarmensagemboasvindas
from atualizarmensagemaosseguidores import atualizarmensagemaosseguidores


def definicoes():


	interruptor_roxo = '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'
	interruptor_cinza = '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'
	message = 'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/AP+gvaeTAAAI7ElEQVR4nO2ae3BU1RnAf9/es3lslDgqNupItcq0QxTE+BoMQmIMmAQBkYgxCQxoprQFrCKI1ZpCUQGLAxQ7aKWUAKNRqEEJEt4PbZFSS9FR0ZlaoWgLWloUCNl7vv5xNzw0d3fZhUin+5u5f+w93+t8e853zj33QooUKVKkSJEiRYr/TySWwEU/Um2PQBJl5y8lZh+iYWIJODYZ8ylSnO74zp/cwZoWOItJClXA+e0YU9wI7LZQxz5++s6LcjgRG741IK0DE1UZl3h47cIFDozXbBSYkIgB3wQ4ShUKotyw5TfyRsIhnkLyhmu+wEagmgQTEPBrMJYLjIXTtfMAW+fKJmO9WBO14TsCTGT1zx+u3TbNlW3Hto19XWcDI4ljH3GSUITZT/aQUcfezB+u3XCTM+w/BVrXf8uW3tX62LrvMJFasQAhSzrt13kAESHj6E+VGysZLS1MSdqwX8NNdx3ZASogAk2OMGzFAvlEVWXaBkYrTAXSkg0iBmFg8iX/YFJ5ubh9KvV8V5mnUNwaG8DqhYntCGNOASv0DSjzgGKUv/St1BEishSYMWu9riHMQoQrEnEeB+9ZqBxTKFsB+lZoH1XmOUoOsEcC3K2WhmQcRCuCGAsrF0qTOlxpLMuM5VwnTEPZEJ1fXKVZo3rJ9m9lcl2WZWaWRbMsnKwr5FKX3cLVYwpla+9hmlE2RGc4luXGJccoq9ItV762QJa2xpko/iPgGKNNdfJP0H4DBnOPCk8BVZmHuebWIVpR3kPeAsY836TLxBuayW6a9qhw953FshSg352aG/iSRQhdgWbg0e5dmFYbqUfJdB7iTICH6Msv8sygQfo6wiKgK7D59tv1scsvZ+KQYmlqbNRurvBr4NYE42kKCsP69pFPQGXQYEbjFbp0LO8Cdy1eLG8dO+aTTYBv4bhjkFcEX1j89eIybJhmHNjPFIFRERurpIWhzy+V3QBrGrValaeBrDjjOKgw4aYSZoqIVg3U85od5opSGmmvSwsxsq5OvjyROOMhZg1oi3nz5FD9YhnjwC3G8qmxFDkO2ypv01sBCktkfqbl6pDL1pALUS/L9swWrisqlRkiohWDtI+FbUGXUmPZG1T6v7BYqtvqfKw4k0qAY2OfBSxaLCsC0M2xLHMs5wZcGqr76/yqYs3q0U/eO3Qm14dcfpZlcdsodBqyzOxwkKt7DJDtw3prRlV/nWHCLHcsOY5ldbpLtwVLvFqQTJzRiLkMxqLud16BHNGPV1UoAarIIG94mVYUFMg2oPaDJbpClDrg0ojax2oZ2nmwrAMYXqbdCLAooHQBEKXxuVcoA4kZRbxx+pHQFDiWmiLNriljgaOURHQ+M5YuBjbXlOq9oNL5Nvm9uORluNyfodwnLl29zqvUlOq9BjYbS5eILo5SUlPGgpoizY7lv12WQT9+WKLXWVgolkuBg8CEAweYEwoxBa9APvWDEkoDRodeWi67gemtut8v1vMChrkopSgo1GWFGXnAYRABZqNUSBr5I0u18lfLZGMycUbDt3KOvsWrrjOXf7261vZW83mIh1F+gpfELTjcNfNV+aBVZtQt2k/gOaAjsEfhx+cc5IXd+5HMjtyhwvRj2kbMWi6vHPFdpp1xWQhcA4QRJp99gJ/XrpPwicSZVALu6+MZnr7ieMNji/USKywAegAWZcoXn/HoM1ul5as2HijRHNfyW5TiyK1WmWDEe5MTYOi0Rvn0q7o1eRrM6shE8Q5lAsAbCnUIN4nSHciJ2PGeRZQRLQ4vzVou/zkpCRh3s5eAqSuPJmD8zVoJzFboAOwMKNVPrPIKmT8q44qpQBkLXB65+TbCk1ObWBSr0I0r1ptRGonjBBtlPwEeP+gwfdZyaY4pT5QEPFTkJeCxVSLjizTbgaeBiojWSzaNmieWyb/icdJK7WBNA6iN8/zugd6aEzTUAz0jflcC9YEwGw8F2QUQhIuw9ATKBYoiqn8Mhxk4dZ3siuXDNwGPFEYeh5V8vCF/MfAFyphJa2VuPB1Ihod66vlOkD8AnYAdFu6ZvEY2RNN5pEB7ITwLdAb+ZuGGyWvk79F0Yi6DRllnLBcby5a0MFe1R+fn5Gkw3aHeWDoZlw2hw1wfq/MAk9bKeifI9cay0Vi+nWZ5ZU6eBqPp+CdAj1wBozyes58bHtlwtMqfSvaewVij5BtlR5rLgAmb4p9qtSvkc21mgFE+NEr3vVnRT7Z9p8CUnt4UsErBhE2xCt3JozZPQ5khPgI6qtDrwQ1t//P3v+HF94sebS9/U3ppAZY1wL+xXDT+ddnfllzMKdCenQfokEG1sXQ0lpV+nQc4w/UuP8avl7XGZbWxZDvCnX5yMadAe+NYSoyCgfpocrESAJ4NoxC0R/Yhbcn4NHxDb4WN0hUFcfDd/kLszgMElA0B79i0u68/34YYCZhz7Sn6biDiN5zBcctXXdNX/Llt368qPloTAunsMgcAb9fYJgk/Dp/q6RHec/zvMxMYkdkHCTR7cX7tGaKV2C9GfBixJbkvM/yYl6c7gM4ZmVwIvN96f0Df4/2tWub980Wl/nHYFi50BAQ+8ZOJtgrsNhYW5Wn+iXQgWYzyZ2MhPcyN0eTiKYICNxrvxOgdX3++DZb5CA/isvH5K9txOTg68sqBZ/3E4imCaUq5Kgj4Hqv5JiAQ5tFAAFSoFhJ/+5oERfVXaK/y7bK+rcZYCVjSVQutSyGwzwn4vz1qzxeccdOQqw+rMAn4q3OYa/vtkL0nol+fq2enCZuBywTG9X9bpvnJ+taAb5JgM9MM/Mkol0iQJa/l6tnx6i75np4TggajXGaUNzt8waxo8qdlAko+lGZxuc1YPjaWnlg2v/ZdLYiltyJXC0PCZmPJN5adaWEGFnwkh6LpnJZToJWVudpJXF7GOwJDYLUK9eqy0aSxE8BtphOGnijlQGFE9U0LA4vf995UReO0TgBA42WanhFgvMBY4MwY4vtUePyQy4ySD5M8EjvdWHuxnmUcygnQF+Uq4Dy8DfEuhHfF0tDi0lDwkez7hkNNkSJFihQpUqRI8T/BfwGrN4MjP+qnwgAAAABJRU5ErkJggg=='
	settings = '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'
	
	with open('/Program Files/Instagram/config.json', 'r') as file:
		data = json.load(file)

		# sg.theme('LightGreen')

		if data['seguir'] == False:
			imagem = interruptor_cinza
		else:
			imagem = interruptor_roxo

		if data['desseguir'] == False:
			imagem2 = interruptor_cinza
		else:
			imagem2 = interruptor_roxo

		if data['mensagem_aos_seguidores'] == False:
			imagem3 = interruptor_cinza
		else:
			imagem3 = interruptor_roxo

		if data['mensagem_boas_vindas'] == False:
			imagem4 = interruptor_cinza
		else:
			imagem4 = interruptor_roxo


		layout2 = [
		[sg.Text('Email or Username:',size=(10,0)), sg.Input(size=(30,0), key='email', default_text=data['email'])],
		[sg.Text('Password:',size=(10,0)), sg.Input(size=(30,0), key='senha', default_text=data['senha'])],
		[sg.Text('Follow followers of (username):', size=(10,0)),sg.Input(size=(30,0), key='seguir_seguidores', default_text=(data['seguir_seguidores']) )],
		[sg.Text('My account username:', size=(10,0)), sg.Input(size=(30,0), key='meu_perfil', default_text=data['meu_perfil'])],
		[sg.Text('Follow', size=(9,0)), sg.Button(image_data=imagem, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='botao'), sg.Text('DM followers', size=(9,0)), sg.Button(image_data=imagem3, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='botao3')],
		[sg.Text('Unfollow', size=(9,0)), sg.Button(image_data=imagem2, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='botao2'), sg.Text('Welcome DM', size=(9,0)), sg.Button(image_data=imagem4, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='botao4')],
			[sg.Button('Close')],
			[sg.Text('         ', key='Output')]
		]

		janela2 = sg.Window('Configuration', layout2, modal=True)



		while True:

			try:
				button, values = janela2.read()

				if button == sg.WIN_CLOSED or button == 'Close':
					break

				if button == 'botao':
					if imagem == interruptor_cinza:
						imagem = interruptor_roxo
						janela2['botao'].update(image_data=imagem)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['seguir'] = True
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)
					elif imagem == interruptor_roxo:
						imagem = interruptor_cinza
						janela2['botao'].update(image_data=imagem)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['seguir'] = False
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)


				if button == 'botao2':
					if imagem2 == interruptor_cinza:
						imagem2 = interruptor_roxo
						janela2['botao2'].update(image_data=imagem2)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['desseguir'] = True
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)
					elif imagem2 == interruptor_roxo:
						imagem2 = interruptor_cinza
						janela2['botao2'].update(image_data=imagem2)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['desseguir'] = False
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)


				if button == 'botao3':
					if imagem3 == interruptor_cinza:
						atualizarmensagemboasvindas()
						imagem3 = interruptor_roxo
						janela2['botao3'].update(image_data=imagem3)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['mensagem_aos_seguidores'] = True
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)
					elif imagem3 == interruptor_roxo:
						imagem3 = interruptor_cinza
						janela2['botao3'].update(image_data=imagem3)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['mensagem_aos_seguidores'] = False
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)

				if button == 'botao4':
					if imagem4 == interruptor_cinza:
						atualizarmensagemaosseguidores()
						imagem4 = interruptor_roxo
						janela2['botao4'].update(image_data=imagem4)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['mensagem_boas_vindas'] = True
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)
					elif imagem4 == interruptor_roxo:
						imagem4 = interruptor_cinza
						janela2['botao4'].update(image_data=imagem4)
						with open('/Program Files/Instagram/config.json', 'r') as file:
							data = json.load(file)
						data['mensagem_boas_vindas'] = False
						with open('/Program Files/Instagram/config.json', 'w') as file:
							json.dump(data, file, indent=2)

				# data['email'] = values['email']
				# data['senha'] = values['senha']
				# data['seguir_seguidores'] = values['seguir_seguidores']
				# data['meu_perfil'] = values['meu_perfil']

				if button == 'Close':
					with open('/Program Files/Instagram/config.json', 'w') as file:
						json.dump(data, file, indent=2)
						# print('Saved!')
						janela2['Output'].update(value='Saved')
						# print(values)
			except:
				break

		janela2.close()

# definicoes()