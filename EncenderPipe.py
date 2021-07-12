import nipyapi as n

n.config.nifi_config.host = 'http://localhost:8080/nifi-api'
n.config.registry_config.host = 'http://localhost:18080/nifi-registry-api'

n.canvas.schedule_process_group("ae80f4a2-0179-1000-2708-1538c87fb249", True)
