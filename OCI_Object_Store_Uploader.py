import oci

# Load config from ~/.oci/config
config = oci.config.from_file()

# Clients
object_storage = oci.object_storage.ObjectStorageClient(config)

# Get namespace
namespace = object_storage.get_namespace().data

bucket_name = "my-bucket"
compartment_id = config["tenancy"] 

# Create Bucket (if not exists)
try:
    create_bucket_details = oci.object_storage.models.CreateBucketDetails(
        name=bucket_name,
        compartment_id=compartment_id,
        public_access_type="NoPublicAccess"
    )

    object_storage.create_bucket(
        namespace_name=namespace,
        create_bucket_details=create_bucket_details
    )

    print(f"Bucket '{bucket_name}' created successfully.")

except oci.exceptions.ServiceError as e:
    if e.status == 409:
        print("Bucket already exists, skipping creation.")
    else:
        raise

# Upload File
file_name = "file.txt"

with open(file_name, "rb") as f:
    object_storage.put_object(
        namespace_name=namespace,
        bucket_name=bucket_name,
        object_name=file_name,
        put_object_body=f
    )

print("File uploaded successfully.")