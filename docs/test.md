```
<PROJECT ROOT>
├── src
|   └── gw
│       ├── common
│       │   └── __init__.py
│       │   └── database.py    # database connection etc.
│       │   └── config.py      # read json config file with db ip etc.
│       ├── reporter
│       │   └── __init__.py
│       │   └── metrics.py     # functions for collecting metrics
│       │   └── main.py        # main function of "metric-reporter"
│       ├── dashboard
│       │    └── dashboard.py  # TBD
│       │    └── main.py       # main function of "metric-dashboard"
│       │    └── __init__.py
│       └── __init__.py
```