import PySimpleGUI as sg
from time import time

def create_window():
	sg.theme('black')
	layout = [
		[sg.Push(),sg.Image('cancel.png', enable_events = True, key = '-CLOSE-')],
		[sg.VPush()],
		[sg.Text('Timer', font = 'Young 50', key = '-TIME-')],
		[	
			sg.Button('Start', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-STARTSTOP-'), 
			sg.Button('Lap', button_color = ('#FFFFFF','#FF0000'), border_width = 0, key = '-LAP-', visible = False)
		],
		[sg.Column([[]], key = '-LAPS-')],
		[sg.VPush()]
	]
	return sg.Window(
		'Stopwatch', 
		layout,
		size = (300,300),
		no_titlebar = True,
		element_justification = 'center')


window = create_window()

start_time = 0
active = False
lap_number = 0
while True:
	event, values = window.read(timeout = 10)
	if event in (sg.WIN_CLOSED, '-CLOSE-'):
		break

	if event == '-STARTSTOP-':
		if active:
			# from active to stop
			active = False
			window['-STARTSTOP-'].update('Reset')
			window['-LAP-'].update(visible = False)
			
		else:
			# from stop to reset
			if start_time > 0:
				window.close()
				window = create_window()
				start_time = 0
				lap_number = 0

			# from start to activd
			else:
				start_time = time()
				active = True
				window['-STARTSTOP-'].update('stop')
				window['-LAP-'].update(visible = True)

	if active:
		elapsed_time = round(time() - start_time,1)
		window['-TIME-'].update(elapsed_time)

	if event == '-LAP-':
		lap_number += 1
		window.extend_layout(window['-LAPS-'],[[sg.Text(lap_number), sg.VSeparator(), sg.Text(elapsed_time)]])

window.close()












