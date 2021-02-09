def dp1():	
	bashCommand = "ddcctl -d 1 -i 15"

	import subprocess
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate

	
if __name__ == '__main__':
	dp1()