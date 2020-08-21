import PySimpleGUI as sg
import json

def atualizarmensagemaosseguidores():
	
	with open('/Program Files/Instagram/config.json', 'r') as file:
		data = json.load(file)

		# sg.theme('LightGreen')
		layout4 = [
		[sg.Text('Type the message here')],
		[sg.Multiline(default_text=data['mensagem_a_lista'], key='mensagem_a_lista', size=(60,17))],
		[sg.Button('Save'), sg.Button('Close')],
		[sg.Text('          ', key='Output-Welcome')]
		]
		janela4 = sg.Window('Configuration', layout4, modal=True)

		while True:
			button4, values4 = janela4.read()

			if button4 == sg.WIN_CLOSED or button4 == 'Close':
				break

			if button4 == 'Save':
				janela4['Output-Welcome'].update(value='Saved')
				data['mensagem_a_lista'] = values4['mensagem_a_lista'].replace('\n', '')

				with open('/Program Files/Instagram/config.json', 'w') as file:
					json.dump(data, file, indent=2)

		janela4.close()

# atualizarmensagemaosseguidores()