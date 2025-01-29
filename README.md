# coding_challenge_ec2_metadata

###########How to Run############
1. Prerequisites
    Ensure that Git and Python 3 are installed on your EC2 instance.

2. Clone the GitHub Repository locally to your EC2 Instance
    Use one of the following methods to clone the public repository to your EC2 instance:
    HTTPS URL: https://github.com/msrreddy620/coding_challenge_ec2_metadata.git
    SSH URL:  git@github.com:msrreddy620/coding_challenge_ec2_metadata.git
    GitHub CLI: gh repo clone msrreddy620/coding_challenge_ec2_metadata

3. Navigate to the Project Directory and Run the Script
    After cloning the repository, change into the project directory and execute the script:
    cd coding_challenge_ec2_metadata  
    python metadata_ec2.py

4. Fetch Metadata Keys

    To retrieve specific EC2 metadata as a JSON output, use the following format:
    Example 1: Fetch the AMI ID: python metadata_ec2.py ami-id
    Example 2: Fetch network information: python metadata_ec2.py network
    Example 3: Fetch the MAC address: python metadata_ec2.py mac


