# cloud-resume-challenge
🚀 Cloud Resume Challenge built on Microsoft Azure. This project showcases my portfolio website featuring my resume, skills, certifications, and social links. It includes HTML/CSS, Azure Blob Storage (static website hosting), GitHub Actions for CI/CD, and future backend integrations like Azure Functions and Cosmos DB.

## 📌 Project Progress

| Stage | Description | Status | Notes |
|-------|-------------|--------|-------|
| 1 | **Azure Fundamentals Certification (AZ-900)** | ✅ Done | Passed and certified |
| 2 | **HTML Resume Created** | ✅ Done | `index.html` completed |
| 3 | **CSS Styling Applied** | ✅ Done | External `styles.css` used |
| 4 | Website Hosted on Azure Blob Storage | ✅ Done | Static site deployed |
| 5 | **HTTPS for Azure Storage URL using Azure CDN** | ✅ Done | Azure CDN profile created |
| 6 | **DNS Domain for Azure CDN endpoint** | ✅ Done | Custom domain added to Azure CDN endpoint [Live Site from custom domain] (https://www.preciousresume.site/) |
| 7 | **Frontend JS for Visitor Counter** | 🔜 Pending | Integrate API with resume site |
| 8 | **Azure Cosmos DB / Table Storage** | 🔜 Pending | Store and retrieve visitor count data |
| 9 | **Azure Function Backend API (Visitor Counter)** | 🔜 Pending | Will handle API requests |
|10 | **Python Azure Function (Backend Logic)** | 🔜 Pending | Python code to handle serverless logic |
|11 | **Python Code Testing** | 🔜 Pending | Unit tests to ensure Azure Function logic is reliable and bug-free |
|12 | **Infrastructure as Code (Bicep/Terraform)** | 🔜 Optional | Automate resource provisioning |
|13 | **Source Control & CI/CD** | 🔜 Pending | GitHub repo and workflows to auto-deploy frontend and backend on code changes |
|14 | **CI/CD Pipeline for Backend** | 🔜 Pending | GitHub Actions to run tests and deploy Azure Function and IaC templates automatically |
|15 | **CI/CD Pipeline for Frontend** | 🔜 Pending | Automate frontend deployment to Azure Blob Storage via GitHub Actions, with optional CDN cache purge |
|16 | **Blog Post Summary** | 🔜 Pending | Will write and publish a short blog post reflecting on lessons learned during the Cloud Resume Challenge |

### ✅ Stage 1: Azure Fundamentals Certification (AZ-900)

📸 Screenshot:

![Az-900 Certificate](screenshots/stage-1-az900-certificate.png)

### ✅ Stage 2: HTML Resume Created

📸 Screenshot:

![Html Resume](screenshots/stage-2-index-html.png)

### ✅ Stage 3: CSS Styling Applied

📸 Screenshot:

![CSS Styling](screenshots/stage-3-css-styling.png)

### ✅ Stage 4: Host Resume on Azure Static Website

I deployed my static HTML/CSS site to Azure Blob Storage using the static website hosting feature.

🔗 [Default Azure Storage static website endpoint](https://preciouswebsite.z6.web.core.windows.net/)

📸 Screenshot:

![Azure Static Website Hosting](screenshots/stage-4-azure-static-hosting.png)

### ✅ Stage 5 and ✅ Stage 6: HTTPS for Azure Storage URL using Azure CDN | DNS Domain for Azure CDN endpoint

By default, the Azure Storage static website endpoint only supports HTTP, which is not secure.  
To enable HTTPS and serve the site on a custom domain, I integrated my storage account with Azure CDN. 

### Screenshots
- 📸 Namecheap DNS settings (nameservers pointing to Azure DNS). 
 ![Namecheap DNS settings](screenshots/step-5-namecheap-dns-settings.png)
- 📸 Azure CDN Profile and Endpoint overview.  
![Overview](screenshots/step-5-azure-cdn-profile-and-endpoint-overview.png)
- 📸 CDN custom domain settings with HTTPS enabled.  
![CDN custom domain settings with HTTPS enabled](./screenshots/step-5-cdn-custom-domain-settings-with-https-enabled.png)
- 📸 Browser screenshot of the live website with (https://www.preciousresume.site/) and the padlock.  
![live website with custom domain](screenshots/step-5-live-website-with-custom-domain.png)

### ✅ Stage 7 Frontend JS for Visitor Counter

I made my static website dynamic by fetching the visitor count from Azure Function and displaying it on my resume page.

To integrate my backend API with my resume site, I added a JavaScript fetch call inside index.html that requested the visitor count from my live Azure Function endpoint. I placed the result inside a <span> element to display the count dynamically. Initially, local testing showed "error" because of CORS restrictions, so I updated my Function App’s CORS settings in Azure to allow requests from my static website domain. Finally, I uploaded the updated index.html to the $web container of my storage account. Once live, the site displayed the actual visitor count retrieved from Cosmos DB through the API.

Screenshot of API endpoint in Function App
![alt text](screenshots/step-7-api-endpoint-in-function-app.png)
![alt text](screenshots/step-7-api-endpoint-in-function-app-1.png)
Screenshot of index.html showing fetch() integration
(screenshots/step-7-index-html-showing-fetch()-integration.png)
Screenshot of CORS configuration in Azure Portal
![alt text](screenshots/step-7-cors-settings.png)
Screenshot of final website with live visitor counter
![alt text](screenshots/step-7-website-showing-visitors-count.png)