terraform {
  required_version = ">= 1.0.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

resource "local_file" "sample_config" {
  filename = "${path.module}/config.txt"
  content  = "Environment = Production\nManagedBy = Terraform"
}

output "file_path" {
  value = local_file.sample_config.filename
}
