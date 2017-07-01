FROM ubuntu
ENV DISPLAY :99.0
ENV DBUS_SESSION_BUS_ADDRESS /dev/null


#================================================
# Google Chrome
#================================================
# Specify version by CHROME_VERSION;
# ex. google-chrome-stable=53.0.2785.101-1
#     google-chrome-beta=53.0.2785.92-1
#     google-chrome-unstable=54.0.2840.14-1
#     latest (equivalent to google-chrome-stable)
#     google-chrome-beta (pulls latest beta)
#=================================================
ARG CHROME_VERSION="google-chrome-stable"
RUN apt-get update -y \
    && apt-get install -y wget \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get install -y ${CHROME_VERSION:-google-chrome-stable} \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*


#=========================
# ChromeDriver
#=========================
ARG CHROME_DRIVER_VERSION=2.30
RUN apt-get update \
    && apt-get install unzip \
    && wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv -f chromedriver /usr/local/share/chromedriver \
    && ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver \
    && ln -s /usr/local/share/chromedriver /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip


#================
# Python and Pip
#================
RUN apt-get install -y python \
    && apt-get install -y python-pip \
    && apt-get install -y python3.5 \
    && apt-get install -y python3-pip \
    && rm -f /usr/bin/python \
    && ln -s /usr/bin/python3.5 /usr/bin/python \
    && pip install pytest pytest-xdist selenium requests


#==============
# SocketServer
#==============
RUN cd /root \
    && wget https://bitbucket.org/hpk42/execnet/raw/2af991418160/execnet/script/socketserver.py
COPY ./docker_scripts/testrunner.py /root/testrunner.py


#==========================
# Xvfb and tightvncserver
#==========================
RUN apt-get install -y xvfb \
    && apt-get install -y x11vnc
