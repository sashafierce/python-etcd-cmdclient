import aio_etcd as etcd
import asyncio



client = etcd.Client() # this will create a client against etcd server running on ['http://localhost:2379']

async def f():
             await client.write('/nodes/n1', "wow")
             result = await client.read('/nodes/n1')
             print(result.value) # bar
             await client.write('/nodes/n2', "wow2")
             await client.delete('/nodes/n2')
             await client.write('/nodes/n3', "wow3")
             result = await client.get("/nodes/n3")
             print(result.value)
             machines = await client.machines()
             print(machines)

loop = asyncio.get_event_loop()
loop.run_until_complete(f())  


