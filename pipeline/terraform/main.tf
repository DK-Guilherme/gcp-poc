provider "google" {
  project = "disco-sky-450823-i1"   # Replace with your project ID
  region  = "us-south1"       # Replace with your preferred region
}

resource "google_cloud_run_service" "default" {
  name     = "gcp-poc-products"  # Name of your Cloud Run service
  location = "us-south1"           # Cloud Run region
  project  = "disco-sky-450823-i1"       # Replace with your project ID

  template {
    spec {
      containers {
        image = "us-south1-docker.pkg.dev/disco-sky-450823-i1/products/poc-product"  # Replace with your container image
        ports {
          container_port = 8080  # Port where the container listens
        }
      }
    }
  }

  traffic {
    percent = 100
  }
}

resource "google_project_iam_member" "run_invoker" {
  project = "disco-sky-450823-i1"   # Replace with your project ID
  role    = "roles/run.invoker"
  member  = "allUsers"          # This grants access to everyone. You can restrict it to specific users if needed
}

resource "google_cloud_run_domain_mapping" "custom_domain" {
  location = "us-south1"            # Replace with your region
  name     = "gcp-poc-products"            # Replace with your custom domain
  project  = "your-project-id"        # Replace with your project ID
  spec {
    route_name = google_cloud_run_service.default.name
  }
}
