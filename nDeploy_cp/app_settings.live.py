#!/usr/bin/python
import os
import socket
import yaml
import cgi
import cgitb
import sys


__author__ = "Anoop P Alias"
__copyright__ = "Copyright Anoop P Alias"
__license__ = "GPL"
__email__ = "anoopalias01@gmail.com"


installation_path = "/opt/nDeploy"  # Absolute Installation Path
app_template_file = installation_path+"/conf/apptemplates.yaml"
backend_config_file = installation_path+"/conf/backends.yaml"


cgitb.enable()


def close_cpanel_liveapisock():
    """We close the cpanel LiveAPI socket here as we dont need those"""
    cp_socket = os.environ["CPANEL_CONNECT_SOCKET"]
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(cp_socket)
    sock.sendall('<cpanelxml shutdown="1" />')
    sock.close()


close_cpanel_liveapisock()
form = cgi.FieldStorage()


print('Content-Type: text/html')
print('')
print('<html>')
print('<head>')
print('<title>nDeploy</title>')
print(('<link rel="stylesheet" href="styles.css">'))
print('</head>')
print('<body>')
print('<a href="xtendweb.live.py"><img border="0" src="xtendweb.png" alt="nDeploy"></a>')
print('<HR>')
if form.getvalue('domain'):
    # Get the domain name from form data
    mydomain = form.getvalue('domain')
    profileyaml = installation_path + "/domain-data/" + mydomain
    # Get data about the backends available
    if os.path.isfile(backend_config_file):
        with open(backend_config_file, 'r') as backend_data_yaml:
            backend_data_yaml_parsed = yaml.safe_load(backend_data_yaml)
    if os.path.isfile(profileyaml):
        # Get all config settings from the domains domain-data config file
        with open(profileyaml, 'r') as profileyaml_data_stream:
            yaml_parsed_profileyaml = yaml.safe_load(profileyaml_data_stream)
        # App settings
        backend_category = yaml_parsed_profileyaml.get('backend_category')
        backend_version = yaml_parsed_profileyaml.get('backend_version')
        backend_path = yaml_parsed_profileyaml.get('backend_path')
        apptemplate_code = yaml_parsed_profileyaml.get('apptemplate_code')
        # get the human friendly name of the app template
        if os.path.isfile(app_template_file):
            with open(app_template_file, 'r') as apptemplate_data_yaml:
                apptemplate_data_yaml_parsed = yaml.safe_load(apptemplate_data_yaml)
            apptemplate_dict = apptemplate_data_yaml_parsed.get(backend_category)
            apptemplate_description = apptemplate_dict.get(apptemplate_code)
        else:
            print('ERROR : app template data file error')
            sys.exit(0)
        # Ok we are done with getting the settings,now lets present it to the user
        print(('<p style="background-color:LightGrey">APPLICATION SETTINGS:  '+mydomain+'</p>'))
        print('<HR>')
        print('<form action="select_app_settings.live.py" method="post">')
        print('<div class="boxedyellow">')
        if backend_category == 'PROXY':
            print(('<p style="background-color:LightGrey">NGINX is proxying to: '+backend_version+' using === '+apptemplate_description+' === as template</p>'))
        else:
            print(('<p style="background-color:LightGrey">NGINX is directly serving content using '+backend_category+' as application server(version: '+backend_version+') and === '+apptemplate_description+' === as template</p>'))
        print('To change application settings select a BACKEND from the drop down below :<br>')
        print('<select name="backend">')
        for backends_defined in backend_data_yaml_parsed.keys():
            if backends_defined == backend_category:
                print(('<option selected value="'+backends_defined+'">'+backends_defined+'</option>'))
            else:
                print(('<option value="'+backends_defined+'">'+backends_defined+'</option>'))
        print('</select>')
        # Pass on the domain name to the next stage
        print(('<input style="display:none" name="domain" value="'+mydomain+'">'))
        print('<HR>')
        print('<center><input type="submit" value="Submit"></center>')
        print('</div>')
        print('</form>')
    else:
        print('ERROR : domain-data file i/o error')
else:
    print('ERROR : Forbidden')
print('</body>')
print('</html>')