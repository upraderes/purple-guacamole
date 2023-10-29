# -*- encoding: utf-8 -*-
import json
import ovh
import sys

# define application key, application secret, consumer key based on script arguments
application_key = sys.argv[1] # Application Key
application_secret = sys.argv[2] # Application Secret
consumer_key = sys.argv[3] # Consumer Key


# Instantiate an OVH Client.
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key=application_key,    # Application Key
    application_secret=application_secret, # Application Secret
    consumer_key=consumer_key    # Consumer Key
)

for service in client.get('/cloud/project'):
    print('Service: ')
    print(service)
    service_name = service
    for kube in client.get(rf'/cloud/project/{service_name}/kube'):
        print(kube)
        kube_id = kube
        for pool in client.get(rf'/cloud/project/{service_name}/kube/{kube_id}/nodepool'):
            print(pool)
            pool_id = pool['id']
            result = client.put(rf'/cloud/project/{service_name}/kube/{kube_id}/nodepool/{pool_id}', 
                    autoscale=False, # Enable the auto-scaling on the pool (type: boolean)
                    desiredNodes=0 # New number of nodes wanted in the nodepool (type: long)
                )
            print(rf"Nodepool {pool_id} updated")
