"""Generate gallery thumbnails without modifying original images.
Run from the repository root: python -m pip install Pillow
Then: python create_thumbnails.py
"""
import json
from pathlib import Path
from PIL import Image, ImageOps
ROOT = Path(__file__).resolve().parent
cards = json.loads((ROOT / 'cards.json').read_text(encoding='utf-8'))
for card in cards:
    source = ROOT / card['img']
    target = ROOT / card.get('thumbnail', 'thumbnails/' + source.stem + '.webp')
    if not source.is_file():
        print('MISSING:', source)
        continue
    if target.resolve() == source.resolve() or target.suffix.lower() != '.webp':
        print('INVALID THUMBNAIL PATH:', target)
        continue
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert('RGB')
        image.thumbnail((800, 1200), Image.Resampling.LANCZOS)
        for quality in (86, 82, 78, 74, 70):
            image.save(target, 'WEBP', quality=quality, method=6)
            if target.stat().st_size <= 200_000:
                break
    print(f'{target.relative_to(ROOT)}: {target.stat().st_size / 1000:.1f} kB')
