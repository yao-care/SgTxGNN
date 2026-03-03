---
layout: default
title: Blog
nav_order: 7
description: "SgTxGNN news, updates, and research guides"
permalink: /blog/
---

# Blog
{: .fs-9 }

News, updates, and research guides
{: .fs-6 .fw-300 }

---

{% for post in site.posts %}
<div class="blog-post-preview">
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="post-meta">{{ post.date | date: "%B %d, %Y" }} · {{ post.categories | join: ", " }}</p>
  <p>{{ post.description }}</p>
</div>
{% endfor %}

<style>
.blog-post-preview {
  padding: 1.5rem 0;
  border-bottom: 1px solid #eee;
}
.blog-post-preview h2 {
  margin-bottom: 0.5rem;
}
.blog-post-preview h2 a {
  color: #1a5276;
  text-decoration: none;
}
.blog-post-preview h2 a:hover {
  text-decoration: underline;
}
.post-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}
</style>
