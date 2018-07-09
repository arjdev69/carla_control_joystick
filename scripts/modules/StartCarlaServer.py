import subprocess

SystemController = ImportModules.SystemController
subprocess.Popen(['/bin/sh', '-c', os.getcwd() +"/scripts/StartServer.sh "+ os.getcwd() +"/CARLA_0.8.4/CarlaUE4.sh"+ " " +"CARLA_0.8.4/Example.CarlaSettings.ini"])