*Azure App Service is the better choice for deploying the CMS. It provides lower operational overhead, built-in autoscaling, high availability, and straightforward CI/CD integration. The platform manages OS patching, runtime updates, certificates, and scaling, reducing maintenance effort and improving reliability. For most CMS workloads—web-based, stateless, and database-backed—App Service offers predictable costs, quick deployment, and strong monitoring/logging tools, making it ideal for long-term sustainability.*

What would change the decision:
A VM-based solution becomes preferable if the CMS requires OS-level customization, unsupported runtimes, custom drivers, specialized security tooling, or strict isolation/compliance not achievable with App Service. Additionally, if the app needs heavy background processing, GPU workloads, or tightly controlled networking, VMs would offer the necessary flexibility and control.*

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

*To avoid forced secret rotation in the future, the app must eliminate long-lived secrets. Use Azure Key Vault, Managed Identity, Azure AD authentication for SQL/Blob, short-lived SAS tokens, and secure CI/CD with GitHub OIDC. No secrets in code or logs. With these design changes, exposure risk disappears.*
