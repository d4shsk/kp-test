import boto3

ACCESS_KEY = "ВАШ_ИДЕНТИФИКАТОР_КЛЮЧА"
SECRET_KEY = "ВАШ_СЕКРЕТНЫЙ_КЛЮЧ"

s3_client = boto3.client(
    service_name="s3",
    endpoint_url="https://storage.yandexcloud.net",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="ru-central1",
)

response = s3_client.list_buckets()
print("Бакеты в Yandex Object Storage:")
for bucket in response.get("Buckets", []):
    print(f"  - {bucket['Name']}")
