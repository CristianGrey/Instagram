import PySimpleGUI as sg
import json

def atualizarmensagemboasvindas():
	
	with open('/Program Files/Instagram/config.json', 'r') as file:
		data = json.load(file)

		# sg.theme('LightGreen')
		layout3 = [
		[sg.Text('Type the message here')],
		[sg.Multiline(default_text=data['mensagem_a_enviar'], key='mensagem_a_enviar', size=(60,17))],
		[sg.Button('Save'), sg.Button('Close')],
		[sg.Text('          ', key='Output-Welcome')]
		]
		janela3 = sg.Window('Configuration', layout3, modal=True)

		while True:
			button3, values3 = janela3.read()

			if button3 == sg.WIN_CLOSED or button3 == 'Close':
				break

			if button3 == 'Save':
				janela3['Output-Welcome'].update(value='Saved')
				data['mensagem_a_enviar'] = values3['mensagem_a_enviar'].replace('\n', '')

				with open('/Program Files/Instagram/config.json', 'w') as file:
					json.dump(data, file, indent=2)

		janela3.close()

# atualizarmensagemboasvindas()