# weixin-api 
#需要申请微信企业号

1.安装
pip install flask

2.下载
weixin.py

4.添加变量
export FLASK_APP=weixin.py 

5.运行
python -m flask run --host=0.0.0.0



# 测试：

curl -d "content=test&mobile=1358171xxxx" "http://127.0.0.1:5000/send"
