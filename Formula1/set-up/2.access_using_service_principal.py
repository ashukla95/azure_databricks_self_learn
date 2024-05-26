# Databricks notebook source
# MAGIC %md
# MAGIC ### Access azure data lake using access keys
# MAGIC - Set spark config using access.azure.account.key
# MAGIC - List files from demo container
# MAGIC - Read data from circuits.csv
# MAGIC

# COMMAND ----------

# client_id = ""
# tenant_id = ""
# client_secret_value = ""
# client_secret_id = ""

# COMMAND ----------


# spark.conf.set("fs.azure.account.auth.type.formula1dlashazure.dfs.core.windows.net", "OAuth")
# spark.conf.set("fs.azure.account.oauth.provider.type.formula1dlashazure.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
# spark.conf.set("fs.azure.account.oauth2.client.id.formula1dlashazure.dfs.core.windows.net", client_id)
# spark.conf.set("fs.azure.account.oauth2.client.secret.formula1dlashazure.dfs.core.windows.net", client_secret_value)
# spark.conf.set("fs.azure.account.oauth2.client.endpoint.formula1dlashazure.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

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


