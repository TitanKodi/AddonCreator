# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
# Thanks to Jesus from Pelisalacarta
#------------------------------------------------------------

import os
import sys
import plugintools

# Entry point
def run():
    plugintools.log("tvalacarta.run")
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec (action+"(params)")
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("tvalacarta.main_list "+repr(params))

    plugintools.add_item( action="play" , title="Big Buck Bunny" , plot="El conejo que vive en un paraíso bucólico de bonitas praderas, árboles fruteros, pájaros y mariposas, es llevado al límite por la destrucción y crueldad de tres pequeños roedores." , url="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" ,thumbnail="https://upload.wikimedia.org/wikipedia/commons/c/c5/Big_buck_bunny_poster_big.jpg" , isPlayable=True, folder=False )
    plugintools.add_item( action="folder" , title="Folder #1" , plot="My First Folder/ Mi primera carpeta" , url="https://raw.githubusercontent.com/TitanKodi/AddonCreator/master/Regex-1.txt" ,thumbnail="https://winaero.com/blog/wp-content/uploads/2018/11/folder-icon-big-256.png" , folder=True )
def folder(params):
    pattern = r'title = "(.*?)"\s*url = "(.*?)"\s*thumbnail = "(.*?)"\s*description = "(.*?)"' # Si hay un backlash ( \ ) se pone una r delante de las comillas
    read_url = plugintools.read(params.get("url")) # Leemos el contenido del url que hemos puesto en el add_item anterior
    matches = plugintools.find_multiple_matches(read_url, pattern)
    for title, url, thumb, description in matches:
        plugintools.add_item( action="play" , title=title, plot=description, url=url,thumbnail=thumb, isPlayable=True, folder=False )
def play(params):
    plugintools.play_resolved_url( params.get("url") )
run()