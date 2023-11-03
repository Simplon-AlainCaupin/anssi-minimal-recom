variable "resource_group_name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "resource_group_location" {
  description = "Location for the Azure Resource Group."
  type        = string
}

variable "vnet_name" {
  description = "Name of the Azure Virtual Network."
  type        = string
}

variable "vnet_address_space" {
  description = "Address space for the Azure Virtual Network."
  type        = list(string)
}

variable "subnet_name" {
  description = "Name of the Azure Subnet."
  type        = string
}

variable "subnet_address_prefix" {
  description = "Address prefix for the Azure Subnet."
  type        = string
}
