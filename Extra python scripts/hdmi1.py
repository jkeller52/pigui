def hdmi1():
	import subprocess
	import pyinfra

	client = SSHClient()
	client.load_system_host_keys()
	client.connect('jacobkeller@mbp.wowway.com”', username='jacobkeller', password='1943')

	# Run a command (execute PHP interpreter)
	stdin, stdout, stderr = client.exec_command(
	bashCommand = "ddcctl -d 1 -i 17"

	
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate

	if __name__ == '__main__':
	hdmi1())

	# Because they are file objects, they need to be closed
	stdin.close()
	stdout.close()
	stderr.close()

	# Close the client itself
	client.close()
	
	#bashCommand = "ddcctl -d 1 -i 17"

	#import subprocess
	#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate

	#if __name__ == '__main__':
	#hdmi1()





# Connect
