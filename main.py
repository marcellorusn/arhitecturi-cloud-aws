
import boto3
from botocore.exceptions import ClientError
from pathlib import Path

# Conectare la S3 prin LocalStack
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

BUCKET = "proiect-student-s3"
FILE = Path("files/exemplu.txt")
DOWNLOADED = Path("files/descarcat.txt")


def create_bucket():
    try:
        s3.create_bucket(Bucket=BUCKET)
        print("Bucket creat cu succes!")
    except ClientError as error:
        if error.response["Error"]["Code"] in (
            "BucketAlreadyOwnedByYou",
            "BucketAlreadyExists"
        ):
            print("Bucket-ul exista deja.")
        else:
            raise


def upload_file():
    s3.upload_file(str(FILE), BUCKET, "exemplu.txt")
    print("Fisier incarcat cu succes!")


def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET)
    print("Fisiere din bucket:")
    for item in response.get("Contents", []):
        print(item["Key"])


def download_file():
    s3.download_file(BUCKET, "exemplu.txt", str(DOWNLOADED))
    print("Fisier descarcat cu succes!")


def delete_file():
    s3.delete_object(Bucket=BUCKET, Key="exemplu.txt")
    print("Fisier sters cu succes!")


if __name__ == "__main__":
    FILE.parent.mkdir(exist_ok=True)
    FILE.write_text(
        "Acesta este un fisier de test pentru proiectul AWS S3.",
        encoding="utf-8"
    )

    create_bucket()
    upload_file()
    list_files()
    download_file()
    delete_file()

    print("Demo finalizat!")
