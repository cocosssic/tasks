import random

class Warrior:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.armor = 100
		self.stamina = 100
		self.block = 0

	def attack(self, other):
		if self.stamina > 0:
			if other.block == 1 and other.armor > 0:
				other.health -= random.randint(0,20)
				other.armor -= random.randint(0,10)
			else:
				other.health -= random.randint(10,30)
		else:
				other.health -= random.randint(0,10)
		if other.health < 0:
			other.health = 0
		print(f'{self.name} атаковал {other.name}. У {other.name} осталось {other.health} очков здоровья')
		self.stamina -= 10
		if other.health <= 10:
			print(f'{self.name} одержал победу над {other.name}')
			if other.health > 0:
				desicion = ''
				while desicion != 'yes' and desicion != 'no':
					desicion = input(f'Пощадить {other.name}? (Введите "yes" или "no"): ')
					if desicion == 'yes':
						print(f'{other.name} пощадили')
					if desicion == 'no':
						print(f'{other.name} был убит')

	def defend(self):
		self.block = 1
		print(f'{self.name} блокирует')

def action(w1, w2):
	options = (1, 2)
	w1_choice = random.choice(options)
	w2_choice = random.choice(options)
	if w1_choice == 1:
		if w2_choice == 1:
			hits_first_choice = random.choice(options)
			if hits_first_choice == 1:
				w1.attack(w2)
				if w2.health <= 10:
					return
				w2.attack(w1)
			else:
				w2.attack(w1)
				if w1.health <= 10:
					return
				w1.attack(w2)
		else:
			w2.defend()
			w1.attack(w2)
	else:
		if w2_choice == 1:
			w1.defend()
			w2.attack(w1)
		else:
			w1.defend()
			w2.defend()
	w1.block, w2.block = 0, 0

w1 = Warrior('Max')
w2 = Warrior('Jake')

print(f'{w1.name} VS {w2.name}')
while w1.health > 10 and w2.health > 10:
	print('----------------------')
	action(w1, w2)