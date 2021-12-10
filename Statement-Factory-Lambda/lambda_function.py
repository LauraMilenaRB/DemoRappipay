import json
from base64 import b64encode

import boto3
import jinja2
from pymongo import MongoClient
from weasyprint import HTML

connection_string = 'mongodb://aygo:Prototype2021$@host:27017/admin' \
                    '?authSource=admin&readPreference=primary&appname=MongoDB%20Compass' \
                    '&directConnection=true&ssl=false&retryWrites=false'
client = MongoClient(connection_string)
db = client['statement']
collection_statement = db['statement']
collection_movements = db['movements']


def get_payment_data(statement):
    statement["total_payment"] = sum(i for i in statement["movements"] if i["installments"] == 1)
    statement["payment_minimum"] = sum(i for i in statement["movements"] if i["installments"] > 1)
    statement["payment_minimum_interest"] = statement["payment_minimum"] * 0.0093


def get_statement_info(identification):
    query_info = {"identification": identification}
    statement = collection_statement.find_one(query_info)
    query_movements = {"movements.user_id": statement["user_id"]}
    movements = list(collection_movements.find(query_movements))
    statement["movements"] = movements
    get_payment_data(statement)
    return statement


def render_to_pdf(statement):
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
    template = jinja_env.get_template("content.html")

    html_content = template.render(statement=statement, movements=statement["movements"])
    pdf_content = HTML(string=html_content, base_url='.').write_pdf()

    return pdf_content


def upload_to_s3(info, file):
    bucket_name = 'aygo-prototype'
    file_name = "statements/"+info["contract"]["identification"]+'.pdf'
    s3_client = boto3.resource('s3')

    obj = s3_client.Object(bucket_name, file_name)
    obj.put(Body=file)

    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"


def lambda_handler(event, context):

    lambda_handler_local(event["identification"])
    return {
        'statusCode': 200,
        'body': json.dumps('Statement upload to S3 Successful!')
    }


def lambda_handler_local(identification):

    statement_info = get_statement_info(identification)
    print("lambda_handler:: --statement_info: ", statement_info)

    statement_pdf = render_to_pdf(statement_info)
    print("lambda_handler:: --statement_pdf: ", b64encode(statement_pdf).decode())

    s3_file = upload_to_s3(statement_info, statement_pdf)
    print("lambda_handler:: --s3_file: ", s3_file)

    return {
        'statusCode': 200,
        'body': json.dumps('Statement upload to S3 Successful!')
    }

