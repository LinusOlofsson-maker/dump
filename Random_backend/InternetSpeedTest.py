import speedtest
import time as time
from tqdm import tqdm

test = speedtest.Speedtest()
print("Loading server List...")
server_list = test.get_servers()# Get list of servers thats avalible
for j in tqdm(range(len(server_list))):
    time.sleep(0.05)
    #print(f"Found a total of {j} servers", end=' ')

print('\r')
print('Choosing best server....')
best = test.get_best_server() # Grabbing the best server
time.sleep(0.5)
print('\r')
time.sleep(0.5)
print(f"The best server is: {best['host']} located in: {best['country']}", end= ' ')
print('\r')
print("Preforming download test...")
print('\r')
time.sleep(0.5)
for i in tqdm(range(3)):
    download_result = test.download()
    #for j in range(1,4):
    print(' ')
    ping_results = test.results.ping
    print(f"Download speed: {download_result / 1024 / 1024:.2f}  Mbit/s Ping: {ping_results:.2f} ms", end= ' ')
    print(' ')
time.sleep(0.5)
print(' ')
print("Preforming upload test...")
print('\r')
time.sleep(0.5)

for i in tqdm(range(3)):
    upload_result = test.upload()
    #for j in range(1,4):
    print(' ')
    ping_results = test.results.ping
    print(f"Upload speed: {upload_result / 1024 / 1024:.2f}  Mbit/s Ping: {ping_results:.2f} ms", end= ' ')
    print(' ')
time.sleep(0.5)

ping_results = test.results.ping



print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_results:.2f} ms")