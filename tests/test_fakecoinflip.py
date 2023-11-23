from mycoinflip import MyCoinFlip

class TestMyCoinFlip:
	def test_get_heads_flip(self):
		result = MyCoinFlip.get_heads_flip()
		assert result in ["Heads"]
