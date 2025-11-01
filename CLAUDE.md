# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal website/blog built with [Hugo](https://gohugo.io/), a static site generator. The site uses the Congo theme (with some files from Blowfish theme also present in the repository). The website primarily consists of blog posts about acting, travel, and software engineering.

## Repository Structure

- `content/`: Contains all the website content
  - `blog/`: Blog posts organized in folder-based structure with index.md files
  - `about.md`: About page
- `config/`: Hugo configuration files
- `assets/`: Custom CSS and images
- `static/`: Static files like favicons
- `themes/`: Contains the Congo and Blowfish themes

## Common Commands

### Development

To start the Hugo development server with live reload:

```bash
hugo server -D
```

The `-D` flag includes draft content. Remove it to exclude drafts.

### Building

To build the site for production:

```bash
hugo
```

Or use the npm script (which compiles TailwindCSS):

```bash
npm run build
```

## Content Creation

### Creating a New Blog Post

```bash
hugo new content/blog/post-name/index.md
```

Blog posts use a folder-based structure where each post has its own directory containing an index.md file and any related assets.

### Front Matter Structure

Blog posts should include the following front matter:

```yaml
---
title: "Post Title"
date: YYYY-MM-DD
tags: ["tag1", "tag2"]
draft: true  # Set to false when ready to publish
---
```

## Deployment

The site is built for deployment to GitHub Pages (based on the repository name EWol234.github.io).

## Hugo Configuration

The site is configured via several files in the `config/_default/` directory:

- `config.toml`: Main configuration
- `languages.en.toml`: Language settings
- `markup.toml`: Markup rendering settings
- `menus.en.toml`: Navigation menu configuration
- `params.toml`: Theme parameters

## Design Guidelines

This blog follows a **minimalist design philosophy** with carefully considered typography, spacing, and color choices.

**IMPORTANT**: All styling decisions should reference the comprehensive guidelines in `design.md`. This file contains:
- Complete color palette and usage guidelines
- Typography system (Lora serif + Inter sans-serif)
- Spacing scale and layout principles
- Component styling specifications
- Responsive design breakpoints
- Accessibility requirements

### Current Design System

The site uses a custom "minimal" color scheme with:
- **Colors**: Warm, muted taupes (#C8A898) and soft grays
- **Typography**: Lora (serif) for headings, Inter (sans-serif) for body text
- **Layout**: 720px content width, generous whitespace, 8px-based spacing scale
- **Philosophy**: Minimal but warm, typography-first, content-focused

### Customization Files

- `assets/css/custom.css` - Main stylesheet implementing design.md guidelines
- `assets/css/schemes/minimal.css` - Custom Congo theme color scheme
- `config/_default/params.toml` - Theme configuration (uses `colorScheme = "minimal"`)

Before making any styling changes, **always consult design.md** to ensure consistency with the established design system.

## Development Best Practices

- Make sure you follow the proper technique of customizing styles in Hugo by using the top-level `layouts/` directory.
- Reference `design.md` for all styling and design decisions.