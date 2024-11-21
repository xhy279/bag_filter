import os

from bag_filter import filter_bags_by_config
  
filter_bags_by_config(os.path.join(os.path.dirname(__file__), "../data"))
