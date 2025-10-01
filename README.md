# cloud-resume-challenge
🚀 Cloud Resume Challenge built on Microsoft Azure. This project showcases my portfolio website featuring my resume, skills, certifications, and social links. It includes HTML/CSS, Azure Blob Storage (static website hosting), GitHub Actions for CI/CD, and future backend integrations like Azure Functions and Cosmos DB.

## 📌 Project Progress

| Stage | Description | Status | Notes |
|-------|-------------|--------|-------|
| 1 | **Azure Fundamentals Certification (AZ-900)** | ✅ Done | Passed and certified |
| 2 | **HTML Resume Created** | ✅ Done | `index.html` completed |
| 3 | **CSS Styling Applied** | ✅ Done | External `styles.css` used |
| 4 | Website Hosted on Azure Blob Storage | ✅ Done | Static site deployed: [Live Site from preciouswebsite.z6.web.core.windows.net](https://preciouswebsite.z6.web.core.windows.net/) |
| 5 | **HTTPS for Azure Storage URL using Azure CDN** | ✅ Done | Azure CDN profile created |
| 6 | **DNS Domain for Azure CDN endpoint** | ✅ Done | Custom domain added to Azure CDN endpoint |
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

🔗 [Live Website from preciouswebsite.z6.web.core.windows.net](https://preciouswebsite.z6.web.core.windows.net/)

📸 Screenshot:

![Azure Static Website Hosting](./screenshots/stage-4-azure-static-hosting.png)

### ✅ Stage 5: HTTPS for Azure Storage URL using Azure CDN

By default, the Azure Storage static website endpoint only supports **HTTP**, which is not secure.  
To enable **HTTPS** and serve the site on a **custom domain**, I integrated my storage account with **Azure CDN**.

### Steps I Followed

1. **Purchased a Custom Domain**  
   - Bought the domain **preciousresume.site** from **Namecheap**.  
   - Updated the domain’s nameservers to point to **Azure DNS** so I could manage DNS records directly in Azure.  

2. **Created a CDN Profile and Endpoint**  
   - In the Azure Portal, I created a **CDN Profile** under my resource group.  
   - Chose the **Standard Microsoft** tier.  
   - Added a **CDN Endpoint** and set the **origin type** to **Storage Static Website**, pointing it to my resume’s storage account.  

3. **Linked Custom Domain to CDN**  
   - Inside the CDN endpoint, I added my custom domain **www.preciousresume.site**.  
   - Created a **CNAME record** in Azure DNS to map `www.preciousresume.site` → CDN endpoint hostname.  
   - Verified domain ownership successfully.  

4. **Enabled HTTPS**  
   - In the CDN custom domain settings, I turned on **Custom Domain HTTPS**.  
   - Selected the free **Azure-managed certificate** option.  
   - Waited for the certificate to be issued (≈30 minutes).  

5. **Tested the Secure Website**  
   - Accessed my website at **https://www.preciousresume.site**.  
   - Verified the site loads securely with the padlock icon in the browser.  

### Key Benefits
- **Security** – Enforced HTTPS with an Azure-managed SSL certificate.  
- **Professionalism** – The site is hosted on a personal custom domain instead of the default Azure URL.  
- **Performance** – Azure CDN improves speed and availability through global caching.  

### Screenshots
- 📸 Namecheap DNS settings (nameservers pointing to Azure DNS). 
 ![Namecheap DNS settings](step-5-namecheap-dns-settings.png)
- 📸 Azure CDN Profile and Endpoint overview.  
![Overview](step-5-azure-cdn-profile-and-endpoint-overview.png)
- 📸 CDN custom domain settings with HTTPS enabled.  
![CDN custom domain settings with HTTPS enabled](step-5-cdn-custom-domain-settings-with-https-enabled.png)
- 📸 Browser screenshot of the live website with `https://www.preciousresume.site` and the padlock.  
![live website with custom domain](step-5-live-website-with-custom-domain.png)