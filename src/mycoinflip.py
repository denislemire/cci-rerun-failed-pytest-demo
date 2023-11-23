import random

class MyCoinFlip:
	# Should always return heads, I'm running a scam!
	def get_heads_flip():
		return random.choice(["Heads", "Tails"])
