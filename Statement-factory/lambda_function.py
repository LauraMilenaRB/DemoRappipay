import json
from base64 import b64encode

import boto3
import jinja2
from pymongo import MongoClient
from weasyprint import HTML

connection_string = 'mongodb://aygo:Prototype2021$@localhost:27017/admin' \
                    '?authSource=admin&readPreference=primary&appname=MongoDB%20Compass' \
                    '&directConnection=true&ssl=false&retryWrites=false'
client = MongoClient(connection_string)
db = client['statement']
collection = db['statement']


def get_statement_info(identification):
    query = {"contract.identification": identification}
    return list(collection.find(query))


def render_to_pdf(statement):
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
    template = jinja_env.get_template("content.html")

    '''
    statement = {
        "contract": {
            "name": "Jhordy Salinas",
            "email": "jhordy.salinas@hotmail.com",
            "identification": "1121946483",
            "card_type": "Clasic",
            "last_digits_digital": "1234",
            "last_digits_physical": "5678",
            "balance": "7100000",
            "used_balance": "1300000",
            "available_balance": "5800000"
        },
        "rewards": {
            "before_balance": "5000",
            "accumulated_balance": "15000",
            "redeem_balance": "8000",
            "balance": "12000"
        },
        "payment": {
            "total": "1300000",
            "minimum": "700000",
            "minimum_interest": "23000"
        },
        "movements": [
            {
                "type": "Compra",
                "amount": "50000",
                "installments": "1",
                "store_name": "Arturo Calle",
                "created_at": "2021-12-05"
            }
        ]
    }
    '''

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


def lambda_handler():#(event, context):
    identification = "1121946483"

    statement_info = get_statement_info(identification)
    print("lambda_handler:: --statement_info: ", statement_info)

    if len(statement_info) == 1:
        statement_pdf = render_to_pdf(statement_info[0])
        print("lambda_handler:: --statement_pdf: ", b64encode(statement_pdf).decode())

        s3_file = upload_to_s3(statement_info[0], statement_pdf)
        print("lambda_handler:: --s3_file: ", s3_file)

        collection.delete_one({"_id": statement_info[0]["_id"]})

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }


lambda_handler()
