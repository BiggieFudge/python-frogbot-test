# 🔴 Showcase: IaC Scanning
# FrogBot will flag: S3 bucket without encryption and public-read ACL
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

resource "aws_s3_bucket" "frogbot_showcase" {
  bucket = "frogbot-py-showcase-bucket"
  # No server_side_encryption_configuration block - FrogBot flags missing encryption
}

resource "aws_s3_bucket_acl" "frogbot_showcase" {
  bucket = aws_s3_bucket.frogbot_showcase.id

  acl = "public-read"  # FrogBot flags public-read as a security misconfiguration
}
