# 📋 Complete Ticket Handoff: NFIN-22562

## 🎯 What This Ticket Is About (Executive Summary)

**Problem**: Customer support emails sent from Zendesk are **not being delivered** to users with **Yahoo email addresses**. This affects multiple Credit Unions (RelyOnCU, Oregonians CU, and now UBI).

**Impact**: Customers aren't receiving support responses → Poor customer experience → Potential escalation and loss of trust.

**Your Role**: You've been assigned to investigate and fix the email delivery issue.

---

## 📖 The Full Story (Timeline)

### **September 2023: Issue Discovered**
- **RelyOnCU** discovered that emails from Zendesk (`support@relyoncu.zendesk.com`) weren't reaching Yahoo mailboxes
- They suspected it might be other email providers too, but Yahoo was confirmed

### **Zendesk Support Response**
Zendesk support team investigated and found:
- The "From" email address is being modified with a long unique identifier
- **Example**: 
  - Real email: `tyfonetesting@yahoo.com`
  - What Zendesk sees: `tyfonetesting+amv4k3puulbaauwznfppl3jvdxr0qt09@yahoo.com`
- **Zendesk's Conclusion**: They claim an **intermediary mail service** (between the user and Zendesk) is modifying the email address, NOT Zendesk itself
- **Their Recommendation**: Work with IT/email admins to check for intermediary mail processing OR verify SPF records

### **What Happened Next**
- Ticket sat idle for **2+ years** (multiple follow-ups from Ranjini, Ashish, etc.)
- **November 28, 2025 (TODAY)**: 
  - **sreelekshmi.vh** flagged that **UBI** (another CU) has the SAME issue
  - **Prashant Karpe** assigned YOU to perform the checks

---

## 🔧 Technical Breakdown (What's Actually Happening)

### **The Email Delivery Flow**
```
Customer (Yahoo) → Zendesk → RelyOnCU's Customers (Yahoo)
                      ↓
                   BLOCKED by Yahoo
```

### **Why Yahoo Is Blocking**
Yahoo (and other major email providers) use **email authentication** to prevent spam. They check:

1. **SPF (Sender Policy Framework)**
   - A DNS record that says "These servers are allowed to send emails on behalf of my domain"
   - If Zendesk isn't listed → Yahoo thinks it's spam

2. **DKIM (DomainKeys Identified Mail)**
   - A cryptographic signature that proves the email is legitimate
   - If missing → Yahoo doesn't trust it

3. **DMARC (Domain-based Message Authentication)**
   - A policy that tells Yahoo what to do if SPF/DKIM fail
   - If set to "reject" → Email gets blocked

### **The Root Cause (Most Likely)**
RelyOnCU's domain **doesn't have Zendesk authorized** in its SPF record, and/or DKIM isn't configured properly.

---

## 🛠️ What Needs to Be Done (Your Action Items)

### **Phase 1: Investigation (Do This First)**

#### **Task 1: Identify the Domain**
- Find out what domain RelyOnCU uses for emails
- Likely: `relyoncu.com` or `relyoncu.org`
- **How to find**: Check the Zendesk admin panel or ask Chandhar Singh

#### **Task 2: Check SPF Record**
```powershell
nslookup -type=txt relyoncu.com
```
- Look for a line starting with `v=spf1`
- **What you're checking**: Does it contain `include:mail.zendesk.com`?
- **If NO**: This is the problem

#### **Task 3: Check DKIM in Zendesk**
- Log into Zendesk Admin Center
- Go to: **Channels** → **Email** → **Addresses**
- Check if DKIM is enabled for `support@relyoncu.zendesk.com`
- **If NO**: You'll need to add CNAME records to DNS

#### **Task 4: Check DMARC Policy**
```powershell
nslookup -type=txt _dmarc.relyoncu.com
```
- Look for `p=reject` or `p=quarantine`
- **If `p=reject`**: Emails will be blocked if SPF/DKIM fail

### **Phase 2: Fix (After Investigation)**

#### **If SPF is Missing**
- Add `include:mail.zendesk.com` to the SPF record
- **Requires**: DNS access (you'll need IT/DevOps help)

#### **If DKIM is Missing**
- Enable DKIM in Zendesk
- Add the CNAME records Zendesk provides to your DNS
- **Requires**: DNS access

#### **If DMARC is Too Strict**
- Consider changing `p=reject` to `p=quarantine` (temporarily)
- **Requires**: DNS access + approval from security team

---

## 👥 Who's Involved (Stakeholders)

| Name | Role | What They Need |
|------|------|----------------|
| **You (Aditya Raj)** | Assignee | Perform the checks and propose a fix |
| **Prashant Karpe** | Technical Lead | Expects you to report findings and coordinate DNS changes |
| **Chandhar Singh** | Reporter | Originally raised the issue, has context on Zendesk setup |
| **Ranjini H.K** | PM for Oregonians CU | Waiting for resolution (high priority for her) |
| **sreelekshmi.vh** | PM for UBI | Just flagged that UBI has the same issue (urgent) |
| **IT/DevOps Team** | DNS Admins | You'll need them to modify DNS records |

---

## 📊 Business Context (Why This Matters)

### **Affected Credit Unions**
1. **RelyOnCU** (Original reporter)
2. **Oregonians CU** (Escalated by Ranjini)
3. **UBI** (Just reported today)

### **Customer Impact**
- Customers with Yahoo emails can't get support responses
- They might think their tickets are being ignored
- Risk of churn and negative reviews

### **Why It's Urgent**
- Multiple CUs affected
- Issue has been open for **2+ years**
- Recent escalation from UBI means this is now high-visibility

---

## 🧠 Key Concepts Explained (For Your Understanding)

### **What is SPF?**
Think of it like a "guest list" for your domain. It tells email providers: "These servers are allowed to send emails on my behalf."

**Example SPF Record**:
```
v=spf1 include:mail.zendesk.com include:_spf.google.com ~all
```
This says: "Zendesk and Google are allowed to send emails for my domain."

### **What is DKIM?**
It's like a wax seal on a letter. It proves the email wasn't tampered with and came from who it claims to be.

### **What is DMARC?**
It's the "policy" that says what to do if SPF/DKIM checks fail:
- `p=none` → Just monitor (don't block)
- `p=quarantine` → Send to spam
- `p=reject` → Block completely

### **Why Yahoo Specifically?**
Yahoo has **very strict** email authentication policies. If SPF/DKIM aren't perfect, they'll block the email. Gmail is more lenient.

---

## 🎯 Success Criteria (How You Know You're Done)

1. ✅ SPF record includes `mail.zendesk.com`
2. ✅ DKIM is enabled in Zendesk and DNS records are added
3. ✅ Test email sent from Zendesk to a Yahoo address → **Delivered successfully**
4. ✅ All 3 CUs (RelyOnCU, Oregonians, UBI) confirm the issue is resolved
5. ✅ Ticket is closed with a summary of what was fixed

---

## 📝 Suggested Next Steps (Your Game Plan)

### **Today (Next 2 Hours)**
1. Find the domain name (ask Chandhar or check Zendesk)
2. Run the SPF/DKIM/DMARC checks
3. Document findings in a comment on the Jira ticket

### **Tomorrow**
1. If DNS changes are needed, create a request for IT/DevOps
2. Sync with Prashant to review your findings
3. Get approval to proceed with DNS changes

### **This Week**
1. Implement the fix (add SPF/DKIM records)
2. Test with a Yahoo email address
3. Notify the 3 CUs that the issue is resolved
4. Close the ticket

---

## 🚨 Potential Blockers (Watch Out For)

1. **No DNS Access**: You'll need to escalate to IT/DevOps
2. **Multiple Domains**: RelyOnCU might use different domains for different services
3. **Zendesk Admin Access**: You might not have permissions (ask Chandhar)
4. **Security Approval**: Changing DNS records might require security team sign-off

---

## 💬 Draft Message to Post in Jira (After Investigation)

```
Hi team,

I've started investigating NFIN-22562. Based on the Zendesk response and the symptoms, this appears to be an email authentication issue (SPF/DKIM).

I'm performing the following checks:
1. Verifying SPF record for [DOMAIN] includes mail.zendesk.com
2. Checking DKIM configuration in Zendesk Admin
3. Reviewing DMARC policy

I'll update this ticket with findings by EOD.

If anyone has DNS access or Zendesk admin credentials, please let me know.

Thanks,
Aditya
```

---

## 📚 Resources (If You Need to Learn More)

- **SPF Checker**: https://mxtoolbox.com/spf.aspx
- **DKIM Checker**: https://mxtoolbox.com/dkim.aspx
- **Zendesk DKIM Setup**: https://support.zendesk.com/hc/en-us/articles/4408886165530

---

## ✅ Checklist (Before You Start)

- [ ] I understand what SPF/DKIM/DMARC are
- [ ] I know who to contact for DNS access
- [ ] I have Zendesk admin access (or know who does)
- [ ] I've read all the comments in the Jira ticket
- [ ] I'm ready to run the investigation commands

---

**Good luck! You've got this. 🚀**
