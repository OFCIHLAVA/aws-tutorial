import boto3
import json

# verify=certification file needed as arg in case communication goes through a proxy
s3_client = boto3.client("s3", verify="combined_cert.crt")
s3_resource = boto3.resource("s3", verify="combined_cert.crt")


def demo_delete_object(bucket: str, key: str, **kwargs) -> None:
    """Delete an object from a S3 bucket

    Args:
        bucket (str): S3 bucket name
        key (str): specific key of the object to delete
        **kwargs: additional args for delete_object method (see docs)

    Note:
    - without the VersionId arg, the file gets deleted(marked as deleted), BUT the individual versions still persists
    on S3(just invisible). Can be downloaded with "download_file" and otherwise manipulated
    - with the VersionId arg, only that specific version gets deleted.

    docs:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_object.html

    """
    s3_client.delete_object(
        Bucket=bucket,
        Key=key,
        **kwargs,
    )


def demo_list_buckets() -> None:
    """List all S3 buckets in the account configured for boto3 client

    docs:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_buckets.html
    """
    response = s3_client.list_buckets()
    print("S3 Buckets:")
    for bucket in response["Buckets"]:
        print(json.dumps(bucket, default=str, indent=4))


def demo_list_objects_v2(bucket: str) -> None:
    """List all objects in a specific S3 bucket

    Args:
        bucket (str): S3 bucket name

    docs:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html
    """
    response = s3_client.list_objects_v2(Bucket=bucket)
    print(f"Objects in S3 Bucket {bucket}:")
    for obj in response.get("Contents", []):
        print(json.dumps(obj, default=str, indent=4))


def demo_download_file(
    bucket: str,
    key: str,
    filename: str,
    **kwargs,
) -> None:
    """Download a file from S3 bucket

    Args:
        bucket (str): S3 bucket name
        key (str): specific key of the object to download (key of the file in S3)
        filename (str): local path to save the downloaded file to

    docs:
        https://boto3.amazonaws.com/v1/documentation/api/latest/_modules/boto3/s3/transfer.html#S3Transfer.download_file
    """
    s3_client.download_file(
        Bucket=bucket,
        Key=key,
        Filename=filename,
        **kwargs,
    )


def demo_put_bucket_versioning(bucket: str, enable: bool) -> None:
    """Enable or disable versioning on a S3 bucket

    Args:
        bucket (str): S3 bucket name
        enable (bool): True to enable versioning, False to disable

    docs:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_versioning.html
    """
    status = "Enabled" if enable else "Suspended"
    s3_client.put_bucket_versioning(
        Bucket=bucket,
        VersioningConfiguration={"Status": status},
    )


def main():
    demo_list_buckets()
    demo_list_objects_v2(
        bucket="ofcihlave-tutorial-test-bucket",
    )
    demo_download_file(
        bucket="ofcihlave-tutorial-test-bucket",
        key="file1.txt",
        filename="file1_downloaded_v2.txt",
    )
    demo_put_bucket_versioning(bucket="ofcihlave-tutorial-test-bucket", enable=True)


# ## Get info about bucket versioning
################################################
# print(
#     json.dumps(
#         s3_client.get_bucket_versioning(Bucket="ofcihlave-tutorial-test-bucket"),
#         default=str,
#         indent=4,
#     )
# )

# ## List all object versions in a bucket
################################################
# print("All objects in S3 Bucket ofcihlave-tutorial-test-bucket:")
# response = s3_client.list_object_versions(Bucket="ofcihlave-tutorial-test-bucket")
# for versioned_file in response["Versions"]:
#     print(json.dumps(versioned_file, default=str, indent=4))

## Download a specific file version
################################################
# response = s3_client.download_file(
#     Bucket="ofcihlave-tutorial-test-bucket",
#     Key="uploaded_file.txt",
#     Filename="invisible_file_donwloaded.txt",
#     ExtraArgs={"VersionId": "QuyiitvHj_FK3.IoSjGgIYq68vMprswU"},
# )

## Upload file to a bucket
################################################
s3_client.upload_file(
    Filename="filetoupload.txt",
    Bucket="ofcihlave-tutorial-test-bucket",
    Key="uploaded_file.txt",
    ExtraArgs={"ContentType": "text/plain"},
)

## Delete a file from a bucket

# Note:
# - without the VersionId arg, the file gets deleted(marked as deleted), BUT the individual versions still persists
# on S3(just invisible). Can be downloaded with "download_file" and otherwise manipulated.
# - with the


if __name__ == "__main__":
    main()
