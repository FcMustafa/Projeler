import os
from time import * 
from kivy.app import App
from pytube import YouTube
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '1600')

class Donustur(GridLayout):
    def __init__(self, **kwargs):
        super(Donustur,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="Url "))
        self.url=TextInput(multiline=False,width=300)
        self.add_widget(self.url)
        self.add_widget(Label(text="İsim Gir "))
        self.isim=TextInput(multiline=False,width=300)
        self.add_widget(self.isim)
        #-------------------------------------------------------------------
        self.add_widget(Label(text ='mp3=aktif\nmp4=pasif'))
        self.aktif = CheckBox(active = True)
        self.add_widget(self.aktif)
        #-------------------------------------------------------------------
        self.buton=Button(text="Dönüştür",background_color =(.3, .6, .7, 1))
        self.buton.bind(on_press=self.tıklandı)
        self.add_widget(self.buton)
        self.son=Label(text ='',color=(0, 1, 0, 1),markup=True)
        self.add_widget(self.son)
    def tıklandı(self,instance):
        if os.path.exists("/download")==True: 
            os.mkdir('download')
        url=self.url.text
        isim=self.isim.text
        if url != "":
            if isim != "":
                if self.aktif.active:
                    yt = YouTube(str(url))
                    yt=yt.streams.filter(only_audio=True).first().download('download',filename=isim+'.mp3')
                    # mesaj
                    self.son.text='[b]' + str(isim) + '.mp3[/b] indirildi'
                else:
                    yt=YouTube(str(url))
                    yt=yt.streams.get_highest_resolution()
                    yt.download('download',filename=str(isim)+'.mp4')
                    self.son.text='[b]' + str(isim) + '.mp4[/b] indirildi'

class Dönüştürücü(App):
    def build(self):
        return Donustur()

if __name__=='__main__':
    Dönüştürücü().run()
