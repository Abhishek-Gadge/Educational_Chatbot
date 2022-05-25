import subprocess


cmd='python notes.py'
p=subprocess.Popen(cmd,shell=True)
out, err=p.communicate()
print(err)
print('hi')