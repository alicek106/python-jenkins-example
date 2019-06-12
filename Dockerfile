FROM alicek106/python-vim-devel:0.1
ADD app.py /
ADD requirements.txt /
RUN pip3 install -r requirements.txt
CMD python3 app.py
