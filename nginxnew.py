#! /usr/bin/python

import docker,sys,os
import time
input_var = raw_input("Enter the username :")
temp= "/"+input_var

print "Your development details"
print "Folder location:"
path = "/home/neethu/dokku"+temp
print path
filepath=path+"/index.html"
os.mkdir( path, 0755 );
a=open (filepath , 'w')
a.write('<html>\n<body>\n<h1>Welcome ')
a.write(input_var)
a.write('</h1>\n<a href=')
a.write('\"test.html\"')
a.write('>heloo</a>\n</body>\n</html>\n') 
a.close()
client = docker.Client(base_url='unix://var/run/docker.sock',version='1.6',timeout=10)
container = client.create_container('panch',command='nginxservice',volumes=['/mysite'],ports=[80],detach=True)

if container: print "successfully created container"
print "container id: " , container["Id"]


client.start(container,port_bindings={80:('127.0.0.1',)},binds={path : '/mysite'}, publish_all_ports=True)
info = client.inspect_container(container)
host_port = info["NetworkSettings"]["Ports"]["80/tcp"][0]["HostPort"]

print "Port is :"+host_port
a = client.logs(container)
print "log is " ,a
print "executed program"




