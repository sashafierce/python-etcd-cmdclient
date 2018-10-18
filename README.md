#  a simple async commandline client to list items from etcd

1. `async_client.py` reads all value corresponding to a key
2. `read_prefixkeys_etcd.py` writes some key value pairs to etcd and reads the keys with provided prefix 

usage
```
$ etcdctl mk /prefix/foo test
$ python read_prefixkeys_etcd.py prefix/
/prefix/foo: test
```
