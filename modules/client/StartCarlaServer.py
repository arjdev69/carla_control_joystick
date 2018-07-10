import subprocess

subprocess.Popen(['/bin/sh', '-c', os.getcwd() +"/StartServer.sh "+ os.getcwd() +"/CARLA_0.8.4/CarlaUE4.sh"+ " " +"CARLA_0.8.4/Example.CarlaSettings.ini"])