# Databricks notebook source
# MAGIC %md
# MAGIC ### Access azure data lake using access keys
# MAGIC - Set spark config using access.azure.account.key
# MAGIC - List files from demo container
# MAGIC - Read data from circuits.csv
# MAGIC

# COMMAND ----------

display(
    dbutils.fs.ls(
        "abfss://<container_name>@<storage_account_name>.dfs.core.windows.net"
    )
)


# COMMAND ----------

display(
    spark.read.csv(
        "abfss://<container_name>@<storage_account_name>.dfs.core.windows.net/circuits.csv"
    )
)

# COMMAND ----------


