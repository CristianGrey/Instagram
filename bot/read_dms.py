import PySimpleGUI as sg
import json

def read():
	# sg.theme('LightGreen')

	layout_messages = [
					[sg.Button('Read')],
					[sg.Multiline(size=(80,25), key=('messages-output'))]
					]

	janela_messages = sg.Window('DMs Sent', layout_messages, modal=True)

	while True:
		message_buttons, messages_values = janela_messages.read()

		if message_buttons == sg.WIN_CLOSED:
			break

		if message_buttons == 'Read':
			with open('/Program Files/Instagram/mensagens_enviadas.json') as mensagens_enviadas:
				mensagens = json.load(mensagens_enviadas)
				janela_messages['messages-output'].update(value=mensagens)

	janela_messages.close()
	
# read()