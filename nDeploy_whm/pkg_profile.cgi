#!/usr/bin/python
import cgi
import cgitb
import os
import shutil
import yaml
import sys


__author__ = "Anoop P Alias"
__copyright__ = "Copyright Anoop P Alias"
__license__ = "GPL"
__email__ = "anoopalias01@gmail.com"


installation_path = "/opt/nDeploy"  # Absolute Installation Path
default_domain_data_file = installation_path+'/conf/domain_data_default.yaml'
app_template_file = installation_path+"/conf/apptemplates.yaml"
backend_config_file = installation_path+"/conf/backends.yaml"


def branding_print_logo_name():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_logo = yaml_parsed_brand.get("brand_logo", "xtendweb.png")
    else:
        brand_logo = "xtendweb.png"
    return brand_logo


def branding_print_banner():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_name = yaml_parsed_brand.get("brand", "AUTOM8N")
    else:
        brand_name = "AUTOM8N"
    return brand_name


def branding_print_footer():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_footer = yaml_parsed_brand.get("brand_footer", '<a target="_blank" href="https://autom8n.com">A U T O M 8 N</a>')
    else:
        brand_footer = '<a target="_blank" href="https://autom8n.com">A U T O M 8 N</a>'
    return brand_footer


def print_green(theoption, hint):
    print(('<div class="col-sm-6"><div class="label label-info" data-toggle="tooltip" title="'+hint+'">'+theoption+'</div></div>'))


def print_red(theoption, hint):
    print(('<div class="col-sm-6"><div class="label label-default" data-toggle="tooltip" title="'+hint+'">'+theoption+'</div></div>'))


def print_disabled():
    print(('<div class="col-sm-6"><center><div class="label label-default" data-toggle="tooltip" title="An additional nginx module is required for this functionality"><center>NO MODULE</center></div></center></div>'))


cgitb.enable()

form = cgi.FieldStorage()

print('Content-Type: text/html')
print('')
print('<html>')
print('<head>')

print('<title>')
print(branding_print_banner())
print('</title>')

print(('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'))
print(('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" crossorigin="anonymous"></script>'))
print(('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>'))
print(('<script src="js.js"></script>'))
print(('<link rel="stylesheet" href="styles.css">'))
print('</head>')
print('<body>')
print('<div id="main-container" class="container text-center">')  # marker1
print('<div class="row">')  # marker2
print('<div class="col-md-6 col-md-offset-3">')  # marker3

print('<div class="logo">')
print('<a href="xtendweb.cgi"><img border="0" src="')
print(branding_print_logo_name())
print('" width="48" height="48"></a>')
print('<h4>')
print(branding_print_banner())
print('</h4>')
print('</div>')

print('<ol class="breadcrumb">')
print('<li><a href="xtendweb.cgi"><span class="glyphicon glyphicon-repeat"></span></a></li>')
print('<li class="active">Server Config</li>')
print('</ol>')

if form.getvalue('cpanelpkg'):
    if form.getvalue('cpanelpkg') == 'default':
        pkgdomaindata = installation_path+'/conf/domain_data_default_local.yaml'
    else:
        pkgdomaindata = installation_path+'/conf/domain_data_default_local_'+form.getvalue('cpanelpkg')+'.yaml'
    if not os.path.isfile(pkgdomaindata):
        shutil.copyfile(default_domain_data_file, pkgdomaindata)
    # Get all config settings from the domains domain-data config file
    with open(pkgdomaindata, 'r') as profileyaml_data_stream:
        yaml_parsed_profileyaml = yaml.safe_load(profileyaml_data_stream)
    # App settings
    backend_category = yaml_parsed_profileyaml.get('backend_category')
    backend_version = yaml_parsed_profileyaml.get('backend_version')
    backend_path = yaml_parsed_profileyaml.get('backend_path')
    apptemplate_code = yaml_parsed_profileyaml.get('apptemplate_code')
    mod_security = yaml_parsed_profileyaml.get('mod_security', 'disabled')
    auth_basic = yaml_parsed_profileyaml.get('auth_basic', 'disabled')
    set_expire_static = yaml_parsed_profileyaml.get('set_expire_static', 'disabled')
    # Server Settings
    autoindex = yaml_parsed_profileyaml.get('autoindex', 'disabled')
    pagespeed = yaml_parsed_profileyaml.get('pagespeed', 'disabled')
    brotli = yaml_parsed_profileyaml.get('brotli', 'disabled')
    gzip = yaml_parsed_profileyaml.get('gzip', 'disabled')
    http2 = yaml_parsed_profileyaml.get('http2', 'disabled')
    access_log = yaml_parsed_profileyaml.get('access_log', 'enabled')
    open_file_cache = yaml_parsed_profileyaml.get('open_file_cache', 'disabled')
    ssl_offload = yaml_parsed_profileyaml.get('ssl_offload', 'disabled')
    wwwredirect = yaml_parsed_profileyaml.get('wwwredirect', 'none')
    redirect_to_ssl = yaml_parsed_profileyaml.get('redirect_to_ssl', 'disabled')
    proxy_to_master = yaml_parsed_profileyaml.get('proxy_to_master', 'disabled')
    redirect_aliases = yaml_parsed_profileyaml.get('redirect_aliases', 'disabled')
    clickjacking_protect = yaml_parsed_profileyaml.get('clickjacking_protect', 'disabled')
    disable_contenttype_sniffing = yaml_parsed_profileyaml.get('disable_contenttype_sniffing', 'disabled')
    xss_filter = yaml_parsed_profileyaml.get('xss_filter', 'disabled')
    hsts = yaml_parsed_profileyaml.get('hsts', 'disabled')
    dos_mitigate = yaml_parsed_profileyaml.get('dos_mitigate', 'disabled')
    pagespeed_filter = yaml_parsed_profileyaml.get('pagespeed_filter', 'CoreFilters')
    redirecturl = yaml_parsed_profileyaml.get('redirecturl', 'none')
    redirectstatus = yaml_parsed_profileyaml.get('redirectstatus', 'none')
    append_requesturi = yaml_parsed_profileyaml.get('append_requesturi', 'disabled')
    test_cookie = yaml_parsed_profileyaml.get('test_cookie', 'disabled')
    symlink_protection = yaml_parsed_profileyaml.get('symlink_protection', 'disabled')
    user_config = yaml_parsed_profileyaml.get('user_config', 'disabled')
    subdir_apps = yaml_parsed_profileyaml.get('subdir_apps', None)
    phpmaxchildren = yaml_parsed_profileyaml.get('phpmaxchildren', '16')
    settings_lock = yaml_parsed_profileyaml.get('settings_lock', 'disabled')
    # get the human friendly name of the app template
    if os.path.isfile(app_template_file):
        with open(app_template_file, 'r') as apptemplate_data_yaml:
            apptemplate_data_yaml_parsed = yaml.safe_load(apptemplate_data_yaml)
        apptemplate_dict = apptemplate_data_yaml_parsed.get(backend_category)
        apptemplate_description = apptemplate_dict.get(apptemplate_code)
    else:
        print('<div class="alert alert-danger">ERROR: app template data file error</div>')
        sys.exit(0)
    if os.path.isfile(backend_config_file):
        with open(backend_config_file, 'r') as backend_data_yaml:
            backend_data_yaml_parsed = yaml.safe_load(backend_data_yaml)
    else:
        print('<div class="alert alert-danger">ERROR: backend config file error</div>')
        sys.exit(0)

    # Ok we are done with getting the settings,now lets present it to the user
    # Next section start here
    print('<div class="alert alert-warning alert-domain"><strong>'+form.getvalue('cpanelpkg')+'</strong></div>')
    print('<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">')  # accordion
    print('<div class="panel panel-default">')  # default
    print(('<div class="panel-heading" role="tab" id="headingOne"><h3 class="panel-title"><a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">Application Server</a></h3></div>'))  # heading
    print('<div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">')  # collapse
    print('<div class="panel-body">')  # body
    print('<form id="config" class="form-inline config-save" action="pkg_app_settings.cgi" method="post">')
    print('<div class="app-status">')
    if backend_category == 'PROXY':
        if backend_version == 'httpd':
            print(('<span class="label label-primary">NGINX</span> <span class="glyphicon glyphicon-transfer" aria-hidden="true"></span> <span class="label label-warning">'+backend_version+'</span> <span class="glyphicon glyphicon-cog" aria-hidden="true"></span> <span class="label label-default">'+apptemplate_description+'</span> <br> <span class="label label-success">.htaccess</span><span class="glyphicon glyphicon-ok-circle" aria-hidden="true"></span>'))
        else:
            print(('<span class="label label-primary">NGINX</span> <span class="glyphicon glyphicon-transfer" aria-hidden="true"></span> <span class="label label-primary">'+backend_version+'</span> <span class="glyphicon glyphicon-cog" aria-hidden="true"></span> <span class="label label-default">'+apptemplate_description+'</span> <br> <span class="label label-danger">.htaccess</span><span class="glyphicon glyphicon-remove-circle" aria-hidden="true"></span>'))
    else:
        print(('<span class="label label-primary">NGINX</span> <span class="glyphicon glyphicon-transfer" aria-hidden="true"></span> <span class="label label-primary">'+backend_version+'</span> <span class="glyphicon glyphicon-cog" aria-hidden="true"></span> <span class="label label-default">'+apptemplate_description+'</span> <br> <span class="label label-danger">.htaccess</span><span class="glyphicon glyphicon-remove-circle" aria-hidden="true"></span>'))
    print('</div>')
    print(('<div class="alert alert-info alert-top">To change the application server select a new category below and hit submit</div>'))
    print('<select name="backend">')
    for backends_defined in backend_data_yaml_parsed.keys():
        if backends_defined == backend_category:
            print(('<option selected value="'+backends_defined+'">'+backends_defined+'</option>'))
        else:
            print(('<option value="'+backends_defined+'">'+backends_defined+'</option>'))
    print('</select>')
    # Pass on the domain name to the next stage
    print(('<input class="hidden" name="cpanelpkg" value="'+form.getvalue('cpanelpkg')+'">'))
    print('<input class="btn btn-primary" type="submit" value="Submit">')
    print('</form>')
    print('</div>')  # body
    print('</div>')  # collapse
    print('</div>')  # default

    # Next section start here
    print('<div class="panel panel-default">')  # default
    print(('<div class="panel-heading" role="tab" id="headingTwo"><h3 class="panel-title"><a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Application Settings</a></h3></div>'))  # heading
    print('<div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">')  # collapse
    print('<div class="panel-body">')  # body
    print('<form id="config" class="form-inline" action="save_pkg_server_settings.cgi" method="post">')

    print('<ul class="list-group">')
    print(('<h6 class="list-group-item-heading">general settings</h6>'))
    # autoindex
    print('<li class="list-group-item">')
    autoindex_hint = "enable for directory listing"
    print('<div class="row">')
    if autoindex == 'enabled':
        print_green("autoindex", autoindex_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="autoindex" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="autoindex" value="disabled"/> Disabled</label></div>')
        print('</div>')
    else:
        print_red("autoindex", autoindex_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="autoindex" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="autoindex" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # ssl_offload
    print('<li class="list-group-item">')
    ssl_offload_hint = "enable for performance, disable if redirect loop error"
    print('<div class="row">')
    if ssl_offload == 'enabled':
        print_green("ssl_offload", ssl_offload_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="ssl_offload" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="ssl_offload" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("ssl_offload", ssl_offload_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="ssl_offload" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="ssl_offload" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # proxy_to_master
    print('<li class="list-group-item">')
    print('<div class="row">')
    proxy_to_master_hint = "in cluster proxy to master instead of local server "
    if proxy_to_master == 'enabled':
        print_green("proxy_to_master", proxy_to_master_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="proxy_to_master" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="proxy_to_master" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("proxy_to_master", proxy_to_master_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="proxy_to_master" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="proxy_to_master" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # access_log
    print('<li class="list-group-item">')
    print('<div class="row">')
    access_log_hint = "disabling access_log increase performance but stats wont work"
    if access_log == 'enabled':
        print_green("access_log", access_log_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="access_log" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="access_log" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("access_log", access_log_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="access_log" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="access_log" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # open_file_cache
    print('<li class="list-group-item">')
    print('<div class="row">')
    open_file_cache_hint = "increase performance, disable on dev environment for no caching"
    if open_file_cache == 'enabled':
        print_green("open_file_cache", open_file_cache_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="open_file_cache" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="open_file_cache" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("open_file_cache", open_file_cache_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="open_file_cache" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="open_file_cache" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    print('</ul>')

    print('<ul class="list-group">')
    print(('<h6 class="list-group-item-heading">content optimization</h6>'))
    # set_expire_static
    print('<li class="list-group-item">')
    print('<div class="row">')
    set_expire_static_hint = "Set Expires/Cache-Control headers for satic content"
    if set_expire_static == 'enabled':
        print_green('set expires header', set_expire_static_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="set_expire_static" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="set_expire_static" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red('set expires header', set_expire_static_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="set_expire_static" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="set_expire_static" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # pagespeed
    print('<li class="list-group-item">')
    print('<div class="row">')
    pagespeed_hint = "delivers pagespeed optimized webpage, resource intensive"
    if os.path.isfile('/etc/nginx/modules.d/pagespeed.load'):
        if pagespeed == 'enabled':
            print_green("pagespeed", pagespeed_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="pagespeed" value="enabled" checked/> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="pagespeed" value="disabled" /> Disabled</label></div>')
            print('</div>')
        else:
            print_red("pagespeed", pagespeed_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="pagespeed" value="enabled" /> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="pagespeed" value="disabled" checked/> Disabled</label></div>')
            print('</div>')
    else:
        print_red("pagespeed", pagespeed_hint)
        print_disabled()
        print(('<input style="display:none" name="pagespeed" value="'+pagespeed+'">'))
    print('</div>')
    print('</li>')
    # pagespeed filter level
    print('<li class="list-group-item">')
    print('<div class="row">')
    pagespeed_filter_hint = "PassThrough breaks some pages.CoreFilters is mostly safe"
    if os.path.isfile('/etc/nginx/modules.d/pagespeed.load'):
        if pagespeed_filter == 'CoreFilters':
            print_red("pagespeed level", pagespeed_filter_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="pagespeed_filter" value="CoreFilters" checked/> CoreFilters</label></div>')
            print('<div class="radio"><label><input type="radio" name="pagespeed_filter" value="PassThrough" /> PassThrough</label></div>')
            print('</div>')
        else:
            print_green("pagespeed_filter", pagespeed_filter_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="pagespeed_filter" value="CoreFilters" /> CoreFilters</label></div>')
            print('<div class="radio"><label><input type="radio" name="pagespeed_filter" value="PassThrough" checked/> PassThrough</label></div>')
            print('</div>')
    else:
        print_red("pagespeed level", pagespeed_filter_hint)
        print_disabled()
        print(('<input style="display:none" name="pagespeed_filter" value="'+pagespeed_filter+'">'))
    print('</div>')
    print('</li>')
    # brotli
    print('<li class="list-group-item">')
    print('<div class="row">')
    brotli_hint = "bandwidth optimization, resource intensive, tls only"
    if os.path.isfile('/etc/nginx/modules.d/brotli.load'):
        if brotli == 'enabled':
            print_green("brotli", brotli_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="brotli" value="enabled" checked/> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="brotli" value="disabled" /> Disabled</label></div>')
            print('</div>')
        else:
            print_red("brotli", brotli_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="brotli" value="enabled" /> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="brotli" value="disabled" checked/> Disabled</label></div>')
            print('</div>')
    else:
        print_red("brotli", brotli_hint)
        print_disabled()
        print(('<input style="display:none" name="brotli" value="'+brotli+'">'))
    print('</div>')
    print('</li>')
    # gzip
    print('<li class="list-group-item">')
    print('<div class="row">')
    gzip_hint = "bandwidth optimization, resource intensive"
    if gzip == 'enabled':
        print_green("gzip", gzip_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="gzip" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="gzip" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("gzip", gzip_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="gzip" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="gzip" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # http2
    print('<li class="list-group-item">')
    print('<div class="row">')
    http2_hint = "works only with TLS"
    if http2 == 'enabled':
        print_green("http2", http2_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="http2" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="http2" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("http2", http2_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="http2" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="http2" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    print('</ul>')

    print('<ul class="list-group">')
    print(('<h6 class="list-group-item-heading">security settings</h6>'))
    # clickjacking_protect
    print('<li class="list-group-item">')
    print('<div class="row">')
    clickjacking_protect_hint = "X-Frame-Options SAMEORIGIN"
    if clickjacking_protect == 'enabled':
        print_green("clickjacking_protect", clickjacking_protect_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="clickjacking_protect" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="clickjacking_protect" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("clickjacking_protect", clickjacking_protect_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="clickjacking_protect" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="clickjacking_protect" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # disable_contenttype_sniffing
    print('<li class="list-group-item">')
    print('<div class="row">')
    disable_contenttype_sniffing_hint = "X-Content-Type-Options nosniff"
    if disable_contenttype_sniffing == 'enabled':
        print_green("disable_contenttype_sniffing", disable_contenttype_sniffing_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="disable_contenttype_sniffing" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="disable_contenttype_sniffing" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("disable_contenttype_sniffing", disable_contenttype_sniffing_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="disable_contenttype_sniffing" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="disable_contenttype_sniffing" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # xss_filter
    print('<li class="list-group-item">')
    print('<div class="row">')
    xss_filter_hint = 'X-XSS-Protection'
    if xss_filter == 'enabled':
        print_green("xss_filter", xss_filter_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="xss_filter" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="xss_filter" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("xss_filter", xss_filter_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="xss_filter" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="xss_filter" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # hsts
    print('<li class="list-group-item">')
    print('<div class="row">')
    hsts_hint = 'Strict-Transport-Security'
    if hsts == 'enabled':
        print_green("hsts", hsts_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="hsts" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="hsts" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("hsts", hsts_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="hsts" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="hsts" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # dos_mitigate
    print('<li class="list-group-item">')
    print('<div class="row">')
    dos_mitigate_hint = "Enable only when under a dos attack"
    if dos_mitigate == 'enabled':
        print_green("dos_mitigate", dos_mitigate_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="dos_mitigate" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="dos_mitigate" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("dos_mitigate", dos_mitigate_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="dos_mitigate" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="dos_mitigate" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # test_cookie
    print('<li class="list-group-item">')
    print('<div class="row">')
    test_cookie_hint = "Disable most bots except good ones like google/yahoo etc with a cookie challenge"
    if os.path.isfile('/etc/nginx/modules.d/testcookie_access.load'):
        if test_cookie == 'enabled':
            print_green("test_cookie", test_cookie_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="test_cookie" value="enabled" checked/> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="test_cookie" value="disabled" /> Disabled</label></div>')
            print('</div>')
        else:
            print_red("test_cookie", test_cookie_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="test_cookie" value="enabled" /> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="test_cookie" value="disabled" checked/> Disabled</label></div>')
            print('</div>')
    else:
        print_red("test_cookie", test_cookie_hint)
        print_disabled()
        print(('<input style="display:none" name="test_cookie" value="'+test_cookie+'">'))
    print('</div>')
    print('</li>')
    # symlink_protection
    print('<li class="list-group-item">')
    print('<div class="row">')
    symlink_protection_hint = "Access to a file is denied if any component of the pathname is a symbolic link, and the link and object that the link points to have different owners"
    if symlink_protection == 'enabled':
        print_green("symlink_protection", symlink_protection_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="symlink_protection" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="symlink_protection" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("symlink_protection", symlink_protection_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="symlink_protection" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="symlink_protection" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # mod_security
    print('<li class="list-group-item">')
    print('<div class="row">')
    mod_security_hint = "mod_security v3 WAF"
    if os.path.isfile('/etc/nginx/modules.d/zz_modsecurity.load'):
        if mod_security == 'enabled':
            print_green('mod_security', mod_security_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="mod_security" value="enabled" checked/> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="mod_security" value="disabled" /> Disabled</label></div>')
            print('</div>')
        else:
            print_red('mod_security', mod_security_hint)
            print('<div class="col-sm-6 col-radio">')
            print('<div class="radio"><label><input type="radio" name="mod_security" value="enabled" /> Enabled</label></div>')
            print('<div class="radio"><label><input type="radio" name="mod_security" value="disabled" checked/> Disabled</label></div>')
            print('</div>')
    else:
        print_red('mod_security', mod_security_hint)
        print_disabled()
        print(('<input style="display:none" name="mod_security" value="'+mod_security+'">'))
    print('</div>')
    print('</li>')
    print('</ul>')

    print('<ul class="list-group">')
    print(('<h6 class="list-group-item-heading">redirections</h6>'))
    # redirect_to_ssl
    print('<li class="list-group-item">')
    print('<div class="row">')
    redirect_to_ssl_hint = "redirect http:// to https:// "
    if redirect_to_ssl == 'enabled':
        print_green("redirect_to_ssl", redirect_to_ssl_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="redirect_to_ssl" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="redirect_to_ssl" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("redirect_to_ssl", redirect_to_ssl_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="redirect_to_ssl" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="redirect_to_ssl" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # redirect_aliases
    print('<li class="list-group-item">')
    print('<div class="row">')
    redirect_aliases_hint = "redirect all alias domains to the main domain"
    if redirect_aliases == 'enabled':
        print_green("redirect_aliases", redirect_aliases_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="redirect_aliases" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="redirect_aliases" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("redirect_aliases", redirect_aliases_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="redirect_aliases" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="redirect_aliases" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # wwwredirect
    print('<li class="list-group-item">')
    www_redirect_hint = "select redirection mode"
    print('<div class="row">')  # marker1
    if wwwredirect == 'none':
        print_red("www redirect", www_redirect_hint)
    else:
        print_green("www redirect", www_redirect_hint)
    print('<div class="col-sm-6 col-radio">')  # marker2
    print('<select name="wwwredirect">')
    if wwwredirect == 'none':
        print(('<option selected value="none">no redirection</option>'))
        print(('<option value="tononwww">redirect www. to non-www</option>'))
        print(('<option value="towww">redirect non-www to www.</option>'))
    elif wwwredirect == 'towww':
        print(('<option value="none">no redirection</option>'))
        print(('<option value="tononwww">redirect www. to non-www</option>'))
        print(('<option selected value="towww">redirect non-www to www.</option>'))
    elif wwwredirect == 'tononwww':
        print(('<option value="none">no redirection</option>'))
        print(('<option selected value="tononwww">redirect www. to non-www</option>'))
        print(('<option value="towww">redirect non-www to www.</option>'))
    print('</select>')
    print('</div>')  # marker2
    print('</div>')  # marker1
    print('</li>')
    # URL Redirect
    print('<li class="list-group-item">')
    print('<div class="row">')
    url_redirect_hint = "select redirection status 301 or 307"
    if redirectstatus == 'none':
        print_red("URL Redirect", url_redirect_hint)
    else:
        print_green("URL Redirect", url_redirect_hint)
    print('<div class="col-sm-6 col-radio">')
    print('<select name="redirectstatus">')
    if redirectstatus == 'none':
        print(('<option selected value="none">no redirection</option>'))
        print(('<option value="301">Permanent Redirect</option>'))
        print(('<option value="307">Temporary Redirect</option>'))
    elif redirectstatus == '301':
        print(('<option value="none">no redirection</option>'))
        print(('<option value="307">Temporary Redirect</option>'))
        print(('<option selected value="301">Permanent Redirect</option>'))
    elif redirectstatus == '307':
        print(('<option value="none">no redirection</option>'))
        print(('<option selected value="307">Temporary Redirect</option>'))
        print(('<option value="301">Permanent Redirect</option>'))
    print('</select>')
    print('</div>')
    print('</div>')
    print('</li>')
    # Append request_uri to redirect
    print('<li class="list-group-item">')
    print('<div class="row">')
    append_requesturi_hint = 'append $$request_uri to the redirect URL'
    if append_requesturi == 'enabled' and redirectstatus != 'none':
        print_green("append $request_uri to redirecturl", append_requesturi_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="append_requesturi" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="append_requesturi" value="disabled" /> Disabled</label></div>')
        print('</div>')
    else:
        print_red("append $request_uri to redirecturl", append_requesturi_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="append_requesturi" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="append_requesturi" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')
    # Redirect URL
    print('<li class="list-group-item">')
    print('<div class="row">')
    redirecturl_hint = "A Valid URL, eg: http://mynewurl.tld"
    if redirecturl == "none" or redirectstatus == 'none':
        print_red("Redirect to URL", redirecturl_hint)
    else:
        print_green("Redirect to URL", redirecturl_hint)
    print('<div class="col-sm-6 col-radio">')
    print('<input class="form-control" placeholder='+redirecturl+' type="text" name="redirecturl">')
    print('</div>')
    print('</div>')
    print('</li>')
    # PHPMAXCHILDREN
    print('<li class="list-group-item">')
    print('<div class="row">')
    phpmaxchildren_hint = "The maximum PHP process that can be spawned"
    print_red("PHP MAXCHILDREN", phpmaxchildren_hint)
    print('<div class="col-sm-6 col-radio">')
    print('<input class="form-control" placeholder='+phpmaxchildren+' type="text" name="phpmaxchildren">')
    print('</div>')
    print('</div>')
    print('</li>')
    # settings_lock
    print('<li class="list-group-item">')
    settings_lock_hint = "Lock application server and security settings"
    print('<div class="row">')
    if settings_lock == 'enabled':
        print_green("settings_lock", settings_lock_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="settings_lock" value="enabled" checked/> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="settings_lock" value="disabled"/> Disabled</label></div>')
        print('</div>')
    else:
        print_red("settings_lock", settings_lock_hint)
        print('<div class="col-sm-6 col-radio">')
        print('<div class="radio"><label><input type="radio" name="settings_lock" value="enabled" /> Enabled</label></div>')
        print('<div class="radio"><label><input type="radio" name="settings_lock" value="disabled" checked/> Disabled</label></div>')
        print('</div>')
    print('</div>')
    print('</li>')

    print('</ul>')
    # end
    # Pass on the package name to the next stage
    print(('<input style="display:none" name="cpanelpkg" value="'+form.getvalue('cpanelpkg')+'">'))
    print('<input class="btn btn-primary" type="submit" value="Submit">')

    print('</form>')
    print('</div>')  # body
    print('</div>')  # collapse
    print('</div>')  # default
    print('</div>')  # accordion
else:
        print('<div class="alert alert-info"><span class="glyphicon glyphicon-alert" aria-hidden="true"></span> Forbidden </div>')

print('<div class="panel-footer"><small>')
print(branding_print_footer())
print('</small></div>')

print('</div>')  # marker3
print('</div>')  # marker2
print('</body>')
print('</html>')
