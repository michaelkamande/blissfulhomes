from django import forms

from .models import Properties, Messages


class PropertyForm(forms.ModelForm):
	class Meta:
		model = Properties
		fields = ['titre', 'category', 'mode', 'salon', 'chambres', 'salle_de_bain', 'cuisine', 'parking', 'description', 'prix', 'zone', 'ville', 'est_disponible', 'publicateur', 'contact', 'image', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9']

class MessagesForm(forms.ModelForm):
	class Meta:
		model = Messages
		fields = ('nom', 'email', 'mobile', 'sujet', 'message')