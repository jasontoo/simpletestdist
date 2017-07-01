import os
import subprocess

if __name__ == '__main__':
    subprocess.Popen(['Xvfb', ':99', '-nolisten', 'tcp', '-screen', '0', '800x600x24'])
    subprocess.Popen(['x11vnc', '-display', ':99', '-rfbport', '5904'])
    os.chdir('/root')
    subprocess.call(['python', 'socketserver.py', ':8888'])