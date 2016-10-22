import requests

uri = 'www.baidu.com'

params = None #Dictionary or bytes
data = None #Dictionary, bytes, or file-like object
json_data = None #(optional) json data
headers = None # (optional) Dictionary
cookies_data = None # (optional) Dict or CookieJar object
# file-tuple: ('filename', fileobj), ('filename', fileobj, 'content_type'), ('filename', fileobj, 'content_type', custom_headers)
files_data = None #Dictionary of 'name': file-like-objects(or {'name': file-tuple})
auth_data = None #(optional) Auth tuple
timeout_time = None # float or tuple:(connect timeout, read timeout)
allow_redirects_data = None #(optional) Boolean.
proxies_url = None #Dictionary
verify_data = None #boolean
stream_data = None #boolean
cert_data = None #String or Tuple

kwargs = dict(
        params=params,  # query string for the Request
        data=data,  # the body of the Request.
        json=json_data,  # the body of the Request
        headers=headers,  # HTTP Headers
        cookies=cookies_data,  #
        files=files_data,  #
        auth=auth_data,  # to enable Basic/Digest/Custom HTTP Auth
        timeout=timeout_time,  # wait for the server to send data before giving up
        allow_redirects=allow_redirects_data,  # if POST/PUT/DELETE redirect following is allowed.
        proxies=proxies_url,  # mapping protocol to the URL of the proxy
        verify=verify_data,  # (optional) whether the SSL cert will be verified. A CA_BUNDLE path can also be provided. Defaults to True.
        stream=stream_data,  # if False, the response content will be immediately downloaded.
        cert=cert_data  # if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    )


def taste_request(uri):
    response = requests.request(
        method='Get',
        url=uri,
        **kwargs
    )
    requests.head(uri, **kwargs)
    requests.get(uri, params=None, **kwargs)
    requests.post(uri, data=None, json=None, **kwargs)
    requests.put(uri, data=None,  **kwargs)
    requests.patch(uri, data=None,  **kwargs)
    requests.delete(uri,  **kwargs)


def taste_request_session():
    s = requests.Session()
    s.get('http://httpbin.org/get')
    with requests.Session() as s:
        s.get('http://httpbin.org/get')
    s.auth = None
    s.cert = None
    s.close() #Closes all adapters and as such the session
    s.cookies = None
    s.delete(uri, **kwargs)
    s.get_adapter(uri) #Returns the appropriate connection adapter for the given URL
    s.head(url, **kwargs)
    s.headers = None
    s.hooks = None #Event-handling hooks.
    s.max_redirects = None
    s.merge_environment_settings(url, proxies, stream, verify, cert)
    s.mount(prefix, adapter)
    s.options(url, **kwargs)
    s.params = None
    s.patch(url, data=None, **kwargs)
    s.post(url, data=None, json=None, **kwargs)
    s.prepare_request(request)
    s.proxies = None
    s.put(url, data=None, **kwargs)
    s.rebuild_auth(prepared_request, response)
    s.rebuild_method(prepared_request, response)
    s.rebuild_proxies(prepared_request, proxies)
    s.request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)
    s.resolve_redirects(resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, **adapter_kwargs)
    s.send(request, **kwargs)
    s.stream = None
    s.trust_env = None
    s.verify = None

# lower-level classes
requests.Request()

# Lower-Lower-Level Classes
requests.PreparedRequest()
requests.auth.AuthBase()
requests.auth.HTTPBasicAuth()
requests.auth.HTTPProxyAuth()
requests.auth.HTTPDigestAuth()

requests.utils.get_encodings_from_content(content)
requests.utils.get_encoding_from_headers(headers)
requests.utils.get_unicode_from_response(r)

requests.utils.dict_from_cookiejar(cj)
requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
requests.utils.add_dict_to_cookiejar(cj, cookie_dict)
requests.cookies.RequestsCookieJar(policy=None)

requests.codes



