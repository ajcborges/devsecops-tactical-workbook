## Security Scanning a Container (Lab 4c)

The [Trivy container security scanner](https://github.com/aquasecurity/trivy) written by
[Teppei Fukuda](https://github.com/knqyf263) bills itself as
"A Simple and Comprehensive Vulnerability Scanner for Containers and other Artifacts, Suitable for CI" .

Let's try using Trivy to scan our container image created in the previous lab.

1. Follow the [directions to install Trivy](https://aquasecurity.github.io/trivy/v0.18.3/installation/)
1. Now we are ready to execute a scan for known vulnerabilities in our container image.

    trivy image frank378:lab4

You are probably seeing many CVEs listed in a tabular format in the output of the scan. Understanding the risk
you are willing to accept for each of these will take some careful consideration. 

