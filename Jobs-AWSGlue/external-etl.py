import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="minsait-data", table_name="minsait", transformation_ctx="S3bucket_node1"
)


# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("id", "string", "id", "string"),
        ("user_id", "long", "user_id", "long"),
        ("mov_type", "string", "mov_type", "string"),
        ("amount", "long", "amount", "long"),
        ("installments", "long", "installments", "long"),
        ("store_id", "long", "store_id", "long"),
        ("store_name", "string", "store_name", "string"),
        ("created_at", "string", "created_at", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
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
        frame=ApplyMapping_node2,
        connection_type="documentdb",
        connection_options=write_documentdb_options
)



job.commit()
