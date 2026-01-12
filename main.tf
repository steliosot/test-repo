# main.tf
resource "aws_db_instance" "app" {
-  instance_class = "db.t3.medium"
+  instance_class = "db.t3.large"
}
