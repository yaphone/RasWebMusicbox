#coding=utf-8
import web
import json
from netease import RasWxMusicbox

urls = ('/', 'index',
        '/search', 'search',
        )

app = web.application(urls, globals())

class index:
    def GET(self):
        return 'Hello'

class search:
    def GET(self):
        usr_input = web.input()
        song_name = usr_input['song']
        netease = RasWxMusicbox(song_name)
        mp3_data = netease.mp3_data
        print mp3_data
        print "OK"
        
        return mp3_data
#        return 'Hello, World'

    
if __name__ == '__main__':
    app.run()