# Requires Module -Name DataGateway

# Check if the required module is installed
try {
    Import-Module DataGateway
}
catch {
    Write-Warning "The DataGateway module is not installed. Please install it first using Install-Module -Name DataGateway."
    return
}

# Replace with your desired values
$GatewayName = "MyGatewayCluster"
$GatewayMemberName = "MyGatewayMember"
$GatewayAdminUser = "user@example.com" # Optional, replace with user's email

# 1. Add a new gateway cluster
Write-Host "Adding a new gateway cluster..."
try {
    Add-DataGatewayCluster -Name $GatewayName -OverwriteExistingGateway
}
catch {
    Write-Error "Error adding gateway cluster: $($_.Exception.Message)"
    return
}

# 2. Add a member to the gateway cluster
Write-Host "Adding a gateway member to the cluster..."
try {
    Add-DataGatewayClusterMember -ClusterId $GatewayName -Name $GatewayMemberName -OverwriteExistingGateway
}
catch {
    Write-Error "Error adding gateway member: $($_.Exception.Message)"
    return
}

# 3. (Optional) Add users as gateway administrators
if ($GatewayAdminUser) {
    Write-Host "Adding user as a gateway administrator..."
    try {
        Add-DataGatewayClusterUser -ClusterId $GatewayName -UserEmail $GatewayAdminUser -Permission "Admin"
    }
    catch {
        Write-Error "Error adding gateway admin: $($_.Exception.Message)"
        return
    }
}

Write-Host "Gateway cluster and member added successfully."
