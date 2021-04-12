# Tserver

Ubuntu 20.04<br>
python3 3.8.5<br>
OpenSSH<br>
pip 20.0.2<br>
nginx<br>
uwsgi<br>
uwsgi-plugin-python<br>
python3-venv<br>
git 2.25.1<br>
<br><br><br>

<br>
혹여나 import 경로가 맞지 않을 시<br>
export PYTHONPATH="${PYTHONPATH}:/home/~"<br>
app.py의 경로까지 입력<br>
<br>

app.py 경로 까지 이동 후 다음 행동<br>
 ㄴ export FLASK_APP=app<br>
 ㄴ export FLASK_ENV=development<br>
 ㄴ flask run<br>
