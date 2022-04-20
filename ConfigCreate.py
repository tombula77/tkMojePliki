from configparser import ConfigParser
parser = ConfigParser()
cfgfile = "config.ini"

def cfgWrite():
    parser.add_section('main')
    parser.set('main', 'x_init', '100')
    parser.set('main', 'y_init', '100')
    parser.set('main', 'width', '600')
    parser.set('main', 'height', '400')
    with open('config.ini', 'w') as f:
        parser.write(f)