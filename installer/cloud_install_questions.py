from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
import gdown

console = Console()
console.print('Which server do you want to download FlyOS rootfs from?')
console.print('''

1. Google Server (Recommended & Fast)
2. FlyOS Server (Unstable, In development)
3. Custom Server (Input URL)
4. Download rootfs from Google Drive in Browser (Open in Browser & Download)
5. Choose rootfs file from local (Type rootfs path)
''')
ask = input('Enter an option: ')
if ask == '1':
    print('Downloading from Google Server...')
    url = "https://drive.google.com/file/d/1bHi4PSllJKfPYsCen0C9vECbjCDXNmM_/view?usp=drive_link"
    output = "rootfs.tar.gz"
    gdown.download(url, output, quiet=False, fuzzy=True)
    rootfs_filename = output
