### Installation  

Install Python3 if it's not yet there.  
To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3.7  
  
For more details or other OSs please follow the documentation:  
https://docs.python.org/3/using/unix.html  
https://docs.python.org/3/using/windows.html  
  
Install PIP if it's not yet there. To do this on Ubuntu, run:  
  
sudo apt-get update  
sudo apt-get -y install python3-pip  

For more details please follow the documentation:  
https://pip.pypa.io/en/stable/installing/  

Install xmltodict and shapely if they are not yet there.  

To do this, either run:  

sudo pip3 install -r requirements.txt  

Or, on Ubuntu, run:  

sudo pip3 install xmltodict  
sudo pip3 install shapely  

For more details please follow:  
https://pypi.org/project/xmltodict/  
https://pypi.org/project/Shapely/  

### Running  

From the current directory, run:  
python3 max_states.py --input locations.xml --output mapped.json --states states/*.wkt  
or  
python3 max_states.py --input example_locations.xml --output example_mapped.json --states states/*.wkt  
