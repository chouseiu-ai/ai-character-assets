from pathlib import Path
from PIL import Image
import json,hashlib

ROOT=Path(__file__).resolve().parent
DEST=ROOT/'recomposed'
DEST.mkdir(exist_ok=True)
def pixels_same(a,b):return a.size==b.size and a.mode==b.mode and a.tobytes()==b.tobytes()
def register(im,params):
    s=params['uniform_scale'];dx,dy=params['translation'];pad=128
    im=im.convert('RGB');padded=Image.new('RGB',(im.width+2*pad,im.height+2*pad),'white');padded.paste(im,(pad,pad))
    box=(pad-dx/s,pad-dy/s,pad+(1254-dx)/s,pad+(1254-dy)/s)
    return padded.resize((1254,1254),Image.Resampling.LANCZOS,box=box)
checks={}
for char,asset_folder,base_name,layer_name in [
    ('Claude','embroidery','front-without-emblem.png','emblem-layer-original.png'),
    ('GPT','necklace','front-without-necklace.png','necklace-layer-original.png')
]:
    folder=ROOT/char
    front=Image.alpha_composite(Image.open(folder/'source-artwork'/base_name).convert('RGBA'),Image.open(folder/'assets'/asset_folder/layer_name).convert('RGBA')).convert('RGB')
    assert pixels_same(front,Image.open(folder/'source-artwork/front-original.png').convert('RGB'))
    front=register(front,json.loads((folder/'provenance/front-registration.json').read_text(encoding='utf-8')))
    assert pixels_same(front,Image.open(folder/'front.png'))
    front.save(DEST/(char.lower()+'-front.png'))
    layers=folder/'assets/back-layers'
    transparent=Image.alpha_composite(Image.open(layers/'body-layer.png').convert('RGBA'),Image.open(layers/'hair-layer.png').convert('RGBA'))
    assert pixels_same(transparent,Image.open(layers/'back-transparent.png').convert('RGBA'))
    back=Image.alpha_composite(Image.new('RGBA',(1254,1254),'white'),transparent).convert('RGB')
    assert pixels_same(back,Image.open(folder/'back.png'))
    back.save(DEST/(char.lower()+'-back.png'))
    checks[char]={'original_front_reproduced':True,'standard_front_pixels_match':True,'back_layer_pixels_match':True,'standard_back_pixels_match':True}
(DEST/'recomposition-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False))
