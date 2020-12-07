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

To deploy this app using an app service, I would need to:
- Create the app service and associated app service plan
- Deploy the app using the app service

In addition to these workflow considerations, I would have to consider costs, availability and scalability. VMs are a more expensive option than App Service, and would require a greater effort on my part to deliver the same level of availability and scaling (if needed). With App service, ensuring high availability requires no additional work on my part as a developer. App service also enables autoscaling, which would require grouping of multiple VMs and load balancing to route traffic to the different VMs.

For the Article CMS App, I would use app service, because this app is lightweight and does not require multiple vCPUs or high performance compute. Both approaches are available options in my selected region (centralus). However, the app service approach is simpler, and does not include additional costs associated with maintaining VMs, eg., continuously updating them to ensure I do not have any security issues. This allows me to focus on application development.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

I would consider using a VM if certain changes were made to the architecture that required the app to be more scalable. This could be an issue if usage patterns force the hardware limitations of the app service to become an issue. Also, if the developer chose to use a microservices architecture and connect several new services to the app, then I would consider deploying it using a VM in order to have more control over secure communication between services and APIs.