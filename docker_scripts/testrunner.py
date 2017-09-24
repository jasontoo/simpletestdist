"""
Test Runner

Initializes programs in Docker container for distribution mode.
Programs used:
 - Xvfb - X virtual framebuffer. Enables test runners to run graphical
 applications without a display (headless). Used for UI automation testing.
 - x11vnc - A VNC server for real X displays. Enables VNC to view
 X displays remotely.
 - SocketServer - Used with pytest-xdist plugin.
"""
import os
import subprocess

if __name__ == '__main__':
    subprocess.Popen(['Xvfb', ':99', '-nolisten', 'tcp', '-screen', '0', '800x600x24'])
    subprocess.Popen(['x11vnc', '-viewonly', '-display', ':99', '-rfbport', '5904'])
    os.chdir('/root')
    subprocess.call(['python', 'socketserver.py', ':8888'])
