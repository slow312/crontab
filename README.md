# crontab

**Pull data down once a day<br />**
0 0 * * * /user/bin/python3 /home/stephanie_low_1/crontab/file1.py > log.txt 2<&1 &

**Pull data every Sunday night at 10:00pm<br />**
0 22 * * SUN /user/bin/python3 /home/stephanie_low_1/crontab/file1.py > log.txt 2<&1 &

**Pull data at the end of every quarter<br />**
0 0 1 */3 * /user/bin/python3 /home/stephanie_low_1/crontab/file1.py > log.txt 2<&1 &

