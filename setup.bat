@ECHO OFF
cd beautifulsoup4-4.3.2/
echo "正在安装 beautifulsoup..."
python setup.py install

cd ..

cd xlwt-0.7.5/
echo "正在安装 xlwt..."
python setup.py install

cd ..
echo "安装完成"

pause