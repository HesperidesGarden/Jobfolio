---
title: Design Decisions
parent: Technical Docs
nav_order: 5
---

[Khanh Linh Pham]
{: .label }

# [Design decisions]

<details open markdown="block">
  <summary>
    Table of contents
  </summary> 
  
  - [Setup Decisions](#setup-decisions)
  - [Portfolio Edit Mode](#portfolio-edit-mode)
</details>

---

## Setup Decisions

### Problem statement

Designing JobFolio was a great idea, but when we looked at what the course scope allowed us to do, we realized it was a bit too much. So, we had to adjust our plans. Instead of trying to build the entire platform from start to finish, we decided to work on the most essential parts. This meant we had to be choosy about what we included.

For example, we simplified the user roles. Instead of having lots of different types of users, we focused on just a few that were really important. This way, we could make sure the main functions of JobFolio were still there without getting too complicated. We also thought about how people would move around inside the platform. We made sure the paths and buttons were clear and straightforward, so users wouldn't get lost or confused. And lastly, we had to think about the content. Originally, we wanted to have a lot of different things on the platform, but we realized that would take too much time. So, we narrowed it down to the most crucial content that would really showcase what JobFolio could do.

### Main decision and regarded options
by [Team]

Our implementation has two roles: *Job Seeker* and *Guest*. We decided against implementing functionalities for hiring managers and organizations, as that would massively increase the work load. By having two main roles, we can focus on JobFolios value proposition of allowing users to create portfolios using simple forms. 

The *Guest* role is only able to see default sites, which all suggest them to 'create an account'. We chose the easiest option, as implementing the *Guest* didn't require more than making a few changes to .html files. Pages such as 'Home', 'Portfolio' and 'Account' are automatically changed and display personalized messages such as *Welcome back, [name]*. Due to us not having a dedicated bar showing the user whether they are logged in or not, those personalized pages help guide the user. This was especially helpful by keeping the page style simple.

By focusing on the *job seeker*, we were also able to narrow down our navigation to just four main pages. The Portfolio editing requires a lot of functionality and routes, so we wanted to focus on that instead of creating more unnecessary introduction pages filled with just text. The content that we did include, however, portray the most important features of JobFolio.

---

## Portfolio Edit Mode

### Problem statement
The challenge with implementing the portfolio edit mode was the complexity that arose from incorporating various functionalities like adding, editing, and deleting items within the portfolio. As the project progressed, the number of HTML, CSS, and Python files began to grow rapidly. This constant addition of files for each new functionality posed a significant issue, especially considering the database interactions and the creation of new methods required for each.

Given the confusing web of files and functionalities that were emerging, managing this growth became increasingly challenging. Integrating these multiple aspects—HTML, CSS, Python code, and database interaction—was proving to be quite intricate and resource-intensive.


### Main decision and regarded options
[by Khanh Linh]

To tackle this situation, I made the decision: simplify the portfolio edit mode by retaining only the delete and add functionalities for **Projects, Skills and Languages** and implementing the edit option only for the **Profile**. While this was undoubtedly a tough choice, it was driven by the necessity to streamline the project's development process and maintain a feasible scope within the limitations of the course.

By opting for this solution, we aimed to reduce the number of forms and forwarding pages, mitigating the mounting complexity of the system. Although this meant sacrificing some of the more conventional and expected edit options, it was a pragmatic move given the circumstances. This decision also aligned with the initial understanding that the platform wouldn't be fully functional due to the project's scope constraints. By keeping the edit option for **Profile**, we showcase that we are capable of implementing it nonetheless.

However, it's important to highlight that the decision to simplify the portfolio edit mode opens up opportunities for future development. While the immediate implementation might not encompass all the desired features, it creates a foundation upon which additional functionalities can be built. This forward-looking approach acknowledges that the project is an evolving entity, and the deliberate simplification was made with the future in mind.

---