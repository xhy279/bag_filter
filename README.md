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



