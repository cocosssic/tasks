import json

class Model:

	title = "The Captain's Daughter"
	text = 'Historical novel'
	author = 'Alexander Pushkin'

	def save(self):
		atr = list(filter(lambda x: not x.startswith('_') and x != 'save', dir(Model)))
		d = {}
		for i in atr:
			d[i] = getattr(self, i)
		with open('model.json', 'w') as f:
			json.dump(d, f)

book = Model()
book.save()