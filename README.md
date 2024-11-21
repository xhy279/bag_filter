## For filtering planning debug logs in ROS1 bag

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
refer to config/config.yaml for more details.

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

