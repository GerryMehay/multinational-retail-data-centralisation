#%%
import yaml
class DatabaseConnector:
  with open('db_creds.yaml') as f:
    read_db_creds = yaml.safe_load(f)
    

# %%
