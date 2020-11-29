# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

To deploy this app using a virtual machine (VM), I would need to:
- Create the VM
- Securely copy my app to the VM using SSH
- Install all of the necessary requirements (correct version of python)
- Map the VM ports and adjust settings
- Launch the app on the VM.
This approach would give me the flexibility to select the operating system (OS) I want to use, and control other aspects of the infrastructure without buying any hardware

To deploy this app usin an app service I would need to:
- Create the app service and associated app service plan
- Deploy the app using the app service

For the Article CMS App, I would use app service, because this app is lightweight and does not require multiple vCPUs or high performance compute. 

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

I would consider using a VM if certain changes were made to the architecture that required it to be more scalable. For example, if the developer chose to use a microservices architecture and connect several new services to the app, then I would consider deploying it using a VM.