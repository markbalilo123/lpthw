
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy Birthday to you", "I dont want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


apology = Song(["Sweat dreams in my eyes",
	"Screams of lost we cry",
	"Tonight you are everything"])

hiling = Song(["Na minsan pa sana akoy Mahalin"])

apology.sing_me_a_song()
hiling.sing_me_a_song()

voltes_five = "Voletes 5 lima kajsjsjsksksksksjskskskskzkskzksksksksksksksksksksksksksskme"
lalala = "La lala lala lalaa"

new_song = Song(voltes_five, lalala)
new_song.sing_me_a_song()
