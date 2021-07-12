import nipyapi as n

n.config.nifi_config.host = 'http://localhost:8080/nifi-api'
n.config.registry_config.host = 'http://localhost:18080/nifi-registry-api'



pipes = n.canvas.list_all_process_groups("388d62f1-0179-1000-ecc6-8da330255db6")
processors = n.canvas.list_all_processors("388d62f1-0179-1000-ecc6-8da330255db6")

cant_procesadores = len(processors)
cant_pipes = len(pipes)
print(f"La cantidad de Procesadores en tu NiFi es: {cant_procesadores}")
print(f"La cantidad de Pipes en tu NiFi es: {cant_pipes}")
