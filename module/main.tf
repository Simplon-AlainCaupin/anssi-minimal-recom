resource "azurerm_resource_group" "lain-rg" {
  name     = var.resource_group_name
  location = var.resource_group_location
}

resource "azurerm_virtual_network" "lain-vnet" {
  name                = var.vnet_name
  location            = var.resource_group_location
  resource_group_name = azurerm_resource_group.lain-rg.name
  address_space       = var.vnet_address_space
}

resource "azurerm_subnet" "lain-subnet" {
  name                 = var.subnet_name
  resource_group_name  = azurerm_resource_group.lain-rg.name
  virtual_network_name = azurerm_virtual_network.lain-vnet.name
  address_prefixes     = [var.subnet_address_prefix]
}
