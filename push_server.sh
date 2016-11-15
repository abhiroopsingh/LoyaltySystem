rm server/*.pyc
rm server/*~
scp -r server/ root@104.236.205.162:~/loyalty
ssh root@104.236.205.162 'pkill python; cd ~/loyalty/server; python main.py &'
