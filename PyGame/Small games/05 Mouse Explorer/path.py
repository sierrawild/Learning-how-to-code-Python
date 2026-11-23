from pathlib import Path

files_dir = Path(__file__).parent/'assets'
sprites_round_dir = files_dir/'sprites'/'Round'
sprites_square_dir = files_dir/'sprites'/'Square'


x = list(sprites_round_dir.iterdir())
y = list(sprites_square_dir.iterdir())

character_sprites = x + y


