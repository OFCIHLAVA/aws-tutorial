import boto3
import json

# verify=certification file needed as arg in case communication goes through a proxy 
s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")


def main():

    # ## Example: List S3 Buckets
    ################################################
    # response = s3_client.list_buckets()
    # print("S3 Buckets:")
    # for bucket in response["Buckets"]:
    #     print(json.dumps(bucket, default=str, indent=4))

    # ## List all objects in a bucket
    ################################################
    # print("All objects in S3 Bucket ofcihlave-tutorial-test-bucket:")
    # response = s3_client.list_objects_v2(Bucket="ofcihlave-tutorial-test-bucket")
    # for obj in response["Contents"]:
    #     print(json.dumps(obj, default=str, indent=4))

    # ## Download a file from a bucket
    ################################################
    # s3_client.download_file(
    #     Bucket="ofcihlave-tutorial-test-bucket",
    #     Key="file1.txt",
    #     Filename="file1_downloaded.txt",
    # )

    # ## Enable bucket versioning
    ################################################
    # s3_client.put_bucket_versioning(
    #     Bucket="ofcihlave-tutorial-test-bucket",
    #     VersioningConfiguration={"Status": "Enabled"},
    # )

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
    #     Key="file1.txt",
    #     Filename="file1_specific_version_donwloaded.txt",
    #     ExtraArgs={"VersionId": "L54rOzQD1nT3OU4kIBK6QvViBOiWsz_1"},
    # )

    ## Upload file to a bucket
    ################################################
    # s3_client.upload_file(
    #     Filename="filetoupload.txt",
    #     Bucket="ofcihlave-tutorial-test-bucket",
    #     Key="uploaded_file.txt",
    #     ExtraArgs={"ContentType": "text/plain"},
    # )


if __name__ == "__main__":
    main()
