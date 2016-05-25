run:
	python daemon.py conf.json
verbose:
	python daemon.py conf.json -d
setup:
	pip install -r requirements.txt
	cp res/conf.json conf.json
	echo "Please edit conf.json with your Twitter and Dota details"
test:
	nosetests
py3:
	python3 daemon.py conf.json
py3v:
	python3 daemon.py conf.json -d
py3setup:
	pip3 install -r requirements.txt
	cp res/conf.json conf.json
	echo "Please edit conf.json with your Twitter and Dota details"

