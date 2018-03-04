from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from bs4 import *
import requests
import re



class MainScreen(Screen):
	pass

class SongChoose(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

def EnglishScrap(e1,e2):
	#entry1=input('Enter Artist')
	#entry2=input('Enter Song')
	url='http://www.lyrster.com/lyrics/'+e2+'-lyrics-'+e1+'.html'
	data=requests.get(url)
	soup=BeautifulSoup(data.text,'html.parser')
	#print(soup)   #It contains all the code of the website.
	data2=soup.find_all(id='lyrics')
	#print(data2)
	data3=re.sub('<br/>',' ',str(data2))
	data4=re.sub('<div id="lyrics">',' ',str(data3))
	data5=re.sub('</div>',' ',str(data4))
	#data6=re.sub('[',' ',str(data5)) #THESE WONT
	#data7=re.sub(']',' ',str(data6))    #WORK

	#print(data5)    #This owns final parsed data.
	#print(data3.replace('<br/>','\n'))
	#data3=data2.children
	#for i in data2.children:
		#print(i)
	#got_data(data5)
	mainString=''  #using a new string to store data5 after removing '[' and ']' 
	for i in data5:
		if (i=='[' or i==']'):
			mainString=mainString+' '
		else: mainString=mainString+i

presentation=Builder.load_file('lyric.kv')

class MainApp(App):
	def build(self):
		return presentation
	EnglishScrap



if __name__=="__main__":
	MainApp().run()
