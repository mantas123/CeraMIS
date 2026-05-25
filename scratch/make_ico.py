from PIL import Image
import os
base = r'C:\Users\bigma\antigravity\CeraMIS'
img = Image.open(os.path.join(base, 'logo.png'))
img.save(os.path.join(base, 'logo.ico'), format='ICO', sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("logo.ico updated successfully with sizes up to 256x256.")
