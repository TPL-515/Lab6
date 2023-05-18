from dagster import define_asset_job, ScheduleDefinition
from lab6.assets.dataingest import *
from lab6.assets.modeltrain import *

generate_data_job = define_asset_job(name="generate_data", selection=[create_demo_table, display_table_before, pull_data, ingest_data, display_table_after])
remove_data_job = define_asset_job(name="remove_data", selection=[clear_table])
##########################################################
################# Insert Code Below ######################
##########################################################

generate_data_job_schedule = ScheduleDefinition(
    job=generate_data_job,
    cron_schedule="* * * * *",  # every minute
)

##########################################################
################# Insert Code Below ######################
##########################################################