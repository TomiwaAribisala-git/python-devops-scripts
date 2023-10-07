# A python script that prints an AWS EKS Cluster information such as its cluster endpoint, cluster version and cluster endpoint

import boto3

def get_eks_cluster_info(cluster_name):
    eks_client = boto3.client('eks')

    try:
        response = eks_client.describe_cluster(name=cluster_name)
        cluster_info = response['cluster']
        
        # Extract relevant information
        cluster_arn = cluster_info['arn']
        cluster_version = cluster_info['version']
        cluster_status = cluster_info['status']
        cluster_created_at = cluster_info['createdAt']
        cluster_endpoint = cluster_info['endpoint']
        
        # Print or process the cluster information as needed
        print("Cluster Name:", cluster_name)
        print("ARN:", cluster_arn)
        print("Version:", cluster_version)
        print("Status:", cluster_status)
        print("Created At:", cluster_created_at)
        print("Endpoint:", cluster_endpoint)
        
    except eks_client.exceptions.ClusterNotFoundException:
        print("Cluster not found:", cluster_name)

# Replace 'your-cluster-name' with the actual name of your EKS cluster
get_eks_cluster_info('your-cluster-name')