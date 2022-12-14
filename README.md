# The Great Code Off: Server

This provides a Zachtronics-like interface for measuring student code and letting students compete against one another.

It provides no authentication currently because it is more likely that our students won't figure out how to "cheat" (we also don't know who is "winning"). But we have a special route for them to announce themselves if they are smart enough to dig into the code.


## Settings

### groupvars

tgco_path: /srv/the-great-code-off
tgco_port: port number (9091)
tgco_debug: False
tgco_hosts_allowed:
    - host: ip4 or DNS
### secrets

tgco_secret_key: random generated password (also inclient)

## License

AGPL-3.0 or later
