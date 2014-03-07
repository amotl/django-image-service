from hashlib import md5
from pymogile import Client
from django.conf import settings

def get_datastore():
    return  Client(domain='develop', trackers=['127.0.0.1:7001'])

def handle_uploaded_file(f):
    buf = f.read()
    filename = get_key(buf)

    datastore = get_datastore()
    fp = datastore.new_file(filename)
    fp.write(buf)
    fp.close()

    return filename 

def get_filedata(filename):
    datastore = get_datastore()
    return datastore.get_file_data(filename)

def get_key(buf):
     m = md5()
     m.update(buf)
     return '%s.jpg' % m.hexdigest()

if __name__ == "__main__":
    key = 'css.css'
    datastore = Client(domain=settings.MOGILEFS_DOMAIN, trackers=settings.MOGILEFS_TRACKERS)
    fp = datastore.new_file('/var/djangotest/name.txt')
    fp.write(key)
    fp.close()

    print datastore.get_paths(key)
    print datastore.get_paths('/var/djangotest/name.txt')
