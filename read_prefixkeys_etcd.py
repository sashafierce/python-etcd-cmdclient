# usage : python3 async_client.py <prefix-key>  
import aio_etcd as etcd
import asyncio
import sys

prefix = sys.argv[1]

# this will create a client against etcd server running on ['http://localhost:2379']
client = etcd.Client(host='127.0.0.1', port=2379)

async def read_keys():
             # first add some keys
             await client.write('key1', "value")
             await client.write('key2', "value2")
             await client.write('key3', "value3")
             await client.write('/nodes/n1', "akanksha")
             # testing some operations
             await client.delete('key3')
             result = await client.get("/nodes/n1")
             print("reading value:", result.value)
             machines = await client.machines()
             print("machines in cluster:", machines)
             
             # by providing an empty string for first arg, it matches all keys
             r = await client.read('', recursive=True, sorted=True)  
             # search for keys with given prefix 
             flag = False
             for child in r.children:
                 st = str(child.key)
                 if(st.startswith( prefix,1)):
                     flag = True
                     print("%s: %s" % (child.key,child.value))
             if (not flag):
                 print("No key exists with given prefix")
                
loop = asyncio.get_event_loop()
loop.run_until_complete(read_keys())  


