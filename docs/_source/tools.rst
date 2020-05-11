.. include:: global.rst

=====
Tools
=====

.. image:: ../images/mouse-593297_1920.jpg
   :align: center

We can reduce our mean time to deploy by using tools to prepare and
generate our machine images programatically, and with scripting languages
such as HCL, which Terraform is based on. In this section we examine these
tools in greater depth.

.. index::
   single: Terraform

******
Packer
******

Using Hashicorp Packer is a great way to nail down the contents of a machine
image before we bring up an instance. 

.. index::
   single: Packer

Here is an example of how to set up a JSON file to build a Packer image in 
Google Compute. Save the contents of this file into `packer/gcp-debian-host.json`:

.. code-block:: bash

   {
      "builders": [
         {
            "type": "googlecompute",
            "account_file": "/home/franklin/.config/gcloud/my-gcloud-creds-file.json",
            "project_id": "sec-dev-ops-000378",
            "source_image_family": "debian-10",
            "zone": "us-central1-a",
            "image_description": "SecDevOps Debian Host",
            "image_name": "generic-lab-host",
            "ssh_username": "root",
            "metadata": { "enable-oslogin": "false" }
         }
      ],
      "provisioners": [
         {
            "type": "shell",
            "inline": [
            "sleep 10",
            "mkdir -p /home/franklin/.ssh",
            "chmod 700 /home/franklin/.ssh"
            ]
         }
      ]
   }

Here is an example of how to set up a JSON file to build a Packer image in 
AWS. Save the contents of this file into `packer/aws-debian-host.json`:

.. code-block:: bash

   {
   "variables": {
      "aws_access_key": "",
      "aws_secret_key": ""
   },
   "builders": [
      {
         "type": "amazon-ebs",
         "access_key": "{{user `aws_access_key`}}",
         "secret_key": "{{user `aws_secret_key`}}",
         "region": "us-west-2",
         "source_ami_filter": {
         "filters": {
            "virtualization-type": "hvm",
            "name": "ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*",
            "root-device-type": "ebs"
         },
         "owners": [
            "099720109477"
         ],
         "most_recent": true
         },
         "instance_type": "t2.micro",
         "ssh_username": "ubuntu",
         "ami_name": "generic-lab-host {{timestamp}}",
         "tags": {
         "Name": "Packer-Ansible",
         "Project": "SecDevOps CloudLab",
         "Commit": "unknown"
         }
      }
   ],
   "provisioners": [
      {
         "type": "shell",
         "execute_command": "echo 'packer' | sudo -S sh -c '{{ .Vars }} {{ .Path }}'",
         "inline": [
            "mkdir -p /home/secdevops/.ssh",
            "chmod 700 /home/secdevops/.ssh",
            "cd /home/secdevops && git clone https://github.com/wwce/ctf_scoreboard.git",
            "cp /home/secdevops/cloudlab/packer/authorized_keys /home/secdevops/.ssh",
            "chown -R ubuntu /home/ubuntu",
            "cp /home/ubuntu/ctf_scoreboard/packer/ctfd.service /etc/systemd/system"
      ]}
   ]
   }

*********
Terraform
*********

Terraform is a tool for building, changing, and versioning infrastructure 
safely and efficiently [#]_ . 

.. [#] https://www.terraform.io/intro/index.html

.. index::
   single: Terraform

**********
Validaters
**********

packer
terraform

.. raw:: latex

    \clearpage

************************
Tool Directory Structure
************************

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Updated Project Directory
   :align: center

   digraph folders {
      "cloudlab" [shape=folder];
      "packer" [shape=folder];
      "aws-debian-host.json" [shape=rect];
      "gcp-debian-host.json" [shape=rect];
      "cloudlab" -> "packer";
      "packer" -> "aws-debian-host.json";
      "packer" -> "gcp-debian-host.json";
   }
