import webbrowser
   
"""doc string explains that the class is named Movie"""
class Movie():  #Class declaration


	"""In this the constructors is being initialized that is instance variables
	are being initilized"""

	def __init__(self,movie_name,Storyline,poster_url,trailer_youtube_url):#Constructor
		self.title=movie_name 											   #instance variable1
		self.storyline=Storyline 										   #instance variable2
		self.poster_image_url=poster_url                                   #instance variable3
		self.trailer_youtube_url=trailer_youtube_url                       #instance variable4

	def show_trailer(self):                                                #instance method
		webbrowser.open(self.trailer_youtube_url)