from song import Song
from playlist import Playlist
import PySimpleGUI as sg

"""
To install PySimpleGUI, run the following lines in your Python Shell:

import pip
pip.main(['install', 'pysimplegui'])

or from your command line:
pip install pysimplegui

For documentation, start with: https://www.pysimplegui.org/en/latest/cookbook/
"""

playlist = Playlist()
playlist.load_from_file('playlist.csv')

"""
The layout is defined as a list of lists.

row1 = row1_col1, row1_col2
row2 = row2_col1
row3 = row3_col1, row3_col2, row3_col3

where rowX_colX is one of the elements found in: 
https://www.pysimplegui.org/en/latest/call%20reference/

layout = [ row1, row2, row3 ]
"""

layout = [ 
    [
        sg.Table(playlist.get_playlist_as_list_of_lists(), 
                 ['Title', 'Artist', 'Length'],
                 size=(None, 20), expand_x=True, key='playlist_table')
    ],
    [
        sg.Text('Total Playlist Length:'), 
        sg.Text(f'{playlist.get_playlist_length()} seconds', key='total_length')
    ],
    [
        sg.Frame('Add a new song', [
            [
                sg.Text('Title:'),
                sg.Push(),
                sg.InputText(key='title')
            ], 
            [
                sg.Text('Artist:'),
                sg.Push(),
                sg.InputText(key='artist')
            ],
            [
                sg.Text('Length:'), 
                sg.Push(),
                sg.InputText(key='length')
            ],            
            [
                sg.Push(),
                sg.Button('OK')
            ]
        ])
    ],
]


window = sg.Window('Your Playlist', layout)

application_running = True

while application_running:   
    event, values = window.read()  
    # When the user clicks the 'OK' button or closes the window, the event and 
    # values will be updated.
    
    if event == sg.WIN_CLOSED or event == 'Cancel':  
        # if user closes window or clicks cancel
        application_running = False
        
    if application_running:
        # Read in values entered by making use of the InputText keys.
        title = values['title']
        artist = values['artist']
        length = values['length']
        
        # If the user enters something other than digits for the length, then
        # nothing will happen.
        if length.isdigit():
            # Update the playlist
            playlist.append_song(Song(title, artist, int(length)))
            
            # Reset the inputs to blank strings
            window['title'].update('')
            window['artist'].update('')
            window['length'].update('')
            
            # Update the displayed values in the table and the total length
            window['playlist_table'].update(playlist.get_playlist_as_list_of_lists())
            window['total_length'].update(playlist.get_playlist_length())    

# If we leave the while loop, then close the window
window.close()

"""
Possible enhancements:
 - Add the ability to save the playlist to a file.
 - Add the ability to remove songs from the playlist.
 - Add the ability to move songs up or down within the playlist (think back to 
   the swap function you did during your lab).
 - Add the ability to specify the name of the file to load from and then
   add a button to load in the playlist.
 - Add the ability to filter the playlist to only show a particular artist.
 - Show an error message if the user doesn't enter a valid integer for length.
"""
