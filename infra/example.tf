# example.tf

# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Create an S3 bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-example-bucket-12345"
  acl    = "private"

  tags = {
    Name        = "example-bucket"
    Environment = "dev"
  }
}

# Enable versioning on the bucket
resource "aws_s3_bucket_versioning" "example" {
  bucket = aws_s3_bucket.example.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Output the bucket name
output "bucket_name" {
  value = aws_s3_bucket.example.bucket
}
