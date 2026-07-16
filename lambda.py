import json
import boto3
import base64
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("LostFoundItems")

s3 = boto3.client("s3")
BUCKET = "lostfoundtask"


def response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    print(json.dumps(event))

    method = event["httpMethod"]
    path = event["resource"]

    # ---------------- REPORT ITEM ----------------

    if method == "POST" and path == "/report":

        body = json.loads(event["body"])

        item_id = str(uuid.uuid4())

        image_url = ""

        if body.get("image"):

            image = base64.b64decode(body["image"])

            filename = item_id + ".jpg"

            s3.put_object(
                Bucket=BUCKET,
                Key=filename,
                Body=image,
                ContentType="image/jpeg"
            )

            image_url = f"https://{BUCKET}.s3.ap-south-1.amazonaws.com/{filename}"

        table.put_item(
            Item={
                "itemId": item_id,
                "name": body.get("name", ""),
                "description": body.get("description", ""),
                "location": body.get("location", ""),
                "date": body.get("date", ""),
                "status": body.get("status", ""),
                "image": image_url
            }
        )

        return response(200, {
            "message": "Item Reported Successfully",
            "itemId": item_id
        })

    # ---------------- VIEW ALL ----------------

    elif method == "GET" and path == "/items":

        params = event.get("queryStringParameters")

        # Search by Item ID
        if params and params.get("itemId"):

            item_id = params["itemId"]

            result = table.get_item(
                Key={
                    "itemId": item_id
                }
            )

            if "Item" in result:
                return response(200, result["Item"])

            return response(404, {
                "message": "Item Not Found"
            })

        # View all items
        result = table.scan()

        return response(200, result["Items"])

    # ---------------- DELETE ----------------

    elif method == "DELETE" and path == "/delete":

        params = event.get("queryStringParameters")

        if not params or "itemId" not in params:
            return response(400, {
                "message": "itemId required"
            })

        table.delete_item(
            Key={
                "itemId": params["itemId"]
            }
        )

        return response(200, {
            "message": "Item Deleted Successfully"
        })

    # ---------------- INVALID ----------------

    return response(404, {
        "message": "Invalid API"
    })
