import json
import boto3
import uuid
from datetime import datetime

s3 = boto3.client("s3")
polly = boto3.client("polly")
dynamodb = boto3.resource("dynamodb")

BUCKET_NAME = "storytelling-by-pranav"
TABLE_NAME = "storytelling-by-pranav"
VOICE_ID = "Aditi"

table = dynamodb.Table(TABLE_NAME)


def response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event["rawPath"]

    try:

        # ---------------- POST /upload ----------------

        if method == "POST" and path == "/upload":

            body = json.loads(event["body"])

            filename = body["filename"]
            story = body["story"]

            story_id = str(uuid.uuid4())

            txt_key = f"stories/{story_id}_{filename}"

            mp3_key = f"audio/{story_id}_{filename.replace('.txt','.mp3')}"

            # Save txt
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=txt_key,
                Body=story,
                ContentType="text/plain"
            )

            # Polly
            polly_response = polly.synthesize_speech(
                Text=story,
                OutputFormat="mp3",
                VoiceId=VOICE_ID
            )

            audio = polly_response["AudioStream"].read()

            # Save mp3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=mp3_key,
                Body=audio,
                ContentType="audio/mpeg"
            )

            audio_url = s3.generate_presigned_url(
    "get_object",
    Params={
        "Bucket": BUCKET_NAME,
        "Key": mp3_key
    },
    ExpiresIn=3600  # URL valid for 1 hour
)

            table.put_item(
                Item={
                    "storyid": story_id,
                    "story_name": filename,
                    "text_file": txt_key,
                    "audio_file": mp3_key,
                    "audio_url": audio_url,
                    "upload_time": datetime.utcnow().isoformat(),
                    "status": "Completed"
                }
            )

            return response(200, {
                "message": "Success",
                "story_id": story_id,
                "audio_url": audio_url
            })

        # ---------------- GET /stories ----------------

        elif method == "GET" and path == "/stories":

            data = table.scan()

            return response(200, data["Items"])

        # ---------------- GET /story/{id} ----------------

        elif method == "GET" and path.startswith("/story/"):

            story_id = path.split("/")[-1]

            item = table.get_item(Key={"story_id": story_id})

            return response(200, item.get("Item", {}))

        # ---------------- DELETE ----------------

        elif method == "DELETE" and path.startswith("/story/"):

            story_id = path.split("/")[-1]

            item = table.get_item(Key={"story_id": story_id})

            if "Item" not in item:
                return response(404, {"message": "Not Found"})

            data = item["Item"]

            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=data["text_file"]
            )

            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=data["audio_file"]
            )

            table.delete_item(
                Key={"story_id": story_id}
            )

            return response(200, {"message": "Deleted"})

        return response(404, {"message": "Invalid API"})

    except Exception as e:
        print(e)
        return response(500, {"error": str(e)})