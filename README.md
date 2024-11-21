## For filtering debug logs in ROS1 bag

### Install
```shell
pip install .
```

### Usage
```shell
from bag_filter import filter_bags_by_config
  
filter_bags_by_config(bag_path=".") # filter all bags in the current directory with default config in config/config.yaml

filter_bags_by_config(bag_path=".", config_path="path/to/config.yaml") # filter all bags in the current directory with the given config file
```

### Config
```yaml
bag_patterns:
  - "*E371*.bag" # bag contains E371

filters:
  - topic: "/mlog/logs/planning" # topic to watch
    path: "entries" # path to the messages in the bag
    pattern: '\[DBG\]\[\d+\]:\[lateral_decision_info\]\[json_str\]' # pattern to match
    conditions:
      - field: "lcStatus" # field to check
        value: "none"
        operator: "!="
      - field: "lbStatus"
        value: "none"
        operator: "!="
      - field: "lcValid"
        value: true
        operator: "=="
```

### License

Copyright (C) 2024 [Jeremy Xia](https://github.com/xhy279)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

