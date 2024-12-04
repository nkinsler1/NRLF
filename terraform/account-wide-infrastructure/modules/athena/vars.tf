variable "database" {
    description = "What the db will be called"
    default     = "NRL-Reporting"
}

variable "name_prefix" {
  type        = string
  description = "The prefix to apply to all resources in the module."
}