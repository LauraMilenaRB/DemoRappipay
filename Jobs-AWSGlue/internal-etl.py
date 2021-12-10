import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node DC Contract
DCContract_node1638637984362 = glueContext.create_dynamic_frame.from_catalog(
    database="contract-data",
    table_name="contract_info",
    additional_options = {
        "database": "contract","collection": "info"
    },
    transformation_ctx="DCContract_node1638637984362",
)

# Script generated for node DC Rewards
DCRewards_node1638638010228 = glueContext.create_dynamic_frame.from_catalog(
    database="rewards-data",
    table_name="rewards_balance",
    additional_options = {
        "database": "rewards","collection": "balance"
    },
    transformation_ctx="DCRewards_node1638638010228",
)

# Script generated for node SQL
SqlQuery0 = """
select c.name as name,
       c.email as email,
       c.identification as identification,
       c.card_type as card_type,
       c.last_digits_digital as last_digits_digital,
       c.last_digits_physical as last_digits_physical,
       c.balance as contract_balance,
       c.used_balance as contract_used_balance,
       c.available_balance as contract_available_balance,
       r.before_balance as rewards_before_balance,
       r.accumulated_balance as rewards_accumulated_balance,
       r.redeem_balance as rewards_redeem_balance,
       r.balance as rewards_balance,
       r.user_id as user_id
from contract c join rewards r on c.user_id = r.user_id

"""
SQL_node1638638029465 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={
        "contract": DCContract_node1638637984362,
        "rewards": DCRewards_node1638638010228,
    },
    transformation_ctx="SQL_node1638638029465",
)

write_documentdb_options = {
    "uri": "mongodb://docdb-2021-11-28-22-06-27.cl9erysdj8fz.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false",
    "database": "statement",
    "collection": "statement",
    "username": "aygo",
    "password": "Prototype2021$",
    "ssl": "false",
    "ssl.domain_match": "false",
    "partitioner": "MongoSamplePartitioner",
    "partitionerOptions.partitionSizeMB": "10",
    "partitionerOptions.partitionKey": "_id"
}

DocumentDB_node1637811446542 = glueContext.write_dynamic_frame.from_options(
        frame=SQL_node1638638029465,
        connection_type="documentdb",
        connection_options=write_documentdb_options
)

job.commit()
