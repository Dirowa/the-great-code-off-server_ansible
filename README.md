# The Great Code Off: Server

This provides a Zachtronics-like interface for measuring student code and letting students compete against one another.

It provides no authentication currently because it is more likely that our students won't figure out how to "cheat" (we also don't know who is "winning"). But we have a special route for them to announce themselves if they are smart enough to dig into the code.

This is an ansible module with plug and play (together with https://github.com/hexylena/the-great-code-off-client)

##for client with cocalc docker. add the following to the docker file
``` 
RUN pip install git+https://github.com/hexylena/the-great-code-off-client
``` 
## Settings

### groupvars
tgco_hosts_allowed: ["server1","server2"]
### secrets
tgco_secret_key: random generated password 

### defaults
tgco_path: /srv/the-great-code-off
tgco_port: 9091
tgco_debug: False

## License

AGPL-3.0 or later

