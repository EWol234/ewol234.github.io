# Design Guidelines

> Minimalist design guidelines for a personal blog about acting, travel, and software engineering

## Design Philosophy

### Core Principles
1. **Minimal but Warm** - Clean, uncluttered layouts with subtle warmth through carefully chosen colors
2. **Typography-First** - Let beautiful, readable typography carry the design
3. **Generous Whitespace** - Allow content to breathe with ample spacing
4. **Purposeful Color** - Use color sparingly and intentionally
5. **Content-Focused** - Remove distractions; let the writing shine

### Inspiration Notes
Inspired by candaceabroad.com's sophisticated approach but with **reduced visual complexity**:
- Simpler color palette (fewer accent colors)
- Less decorative elements (no circular masks, minimal shadows)
- Cleaner typography hierarchy
- More whitespace, less content density

---

## Color Palette

### Primary Colors
```
Background:     #FEFEFE (almost white, warm undertone)
Primary Text:   #2D2D2D (warm charcoal, not pure black)
Secondary Text: #6B6B6B (medium gray for metadata)
```

### Accent Colors
```
Primary Accent: #C8A898 (soft taupe - muted, warm, versatile)
Link Color:     #A88878 (darker taupe for links)
Link Hover:     #8B6F5F (deepest taupe for hover states)
Border/Divider: #E8E8E8 (very light gray)
```

### Semantic Colors
```
Code Background:  #F7F7F7 (subtle gray)
Code Text:        #505050 (medium charcoal)
Highlight:        #FFF8F5 (warm off-white for subtle highlights)
```

### Usage Guidelines
- **Background**: Pure whites can be harsh; use #FEFEFE for softer feel
- **Text**: Never use pure black (#000); #2D2D2D provides better readability
- **Accents**: Use taupe sparingly - for hover states, subtle highlights, and visual interest
- **Borders**: Keep minimal; when needed, use the lightest gray (#E8E8E8)

---

## Typography

### Font Families

#### Primary: Serif for Headings
```css
font-family: 'Lora', 'Georgia', serif;
```
- **Rationale**: Elegant, readable serif that works for both headings and emphasis
- **Alternative**: 'Merriweather' or 'Crimson Text' if Lora unavailable
- **Usage**: All headings (H1-H6), pull quotes, featured text

#### Secondary: Sans-Serif for Body
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
```
- **Rationale**: Clean, modern, highly readable at all sizes
- **Alternative**: 'Source Sans Pro' or system fonts for performance
- **Usage**: Body text, navigation, metadata, captions

#### Monospace: Code
```css
font-family: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
```
- **Usage**: Code blocks, inline code, technical content

### Type Scale
```
H1: 2.5rem (40px)    - Page titles
H2: 2rem (32px)      - Section headings
H3: 1.5rem (24px)    - Subsection headings
H4: 1.25rem (20px)   - Minor headings
Body: 1.125rem (18px) - Main text
Small: 0.875rem (14px) - Metadata, captions
```

### Typography Settings
```css
/* Body Text */
font-size: 1.125rem;
line-height: 1.8;        /* Generous for readability */
letter-spacing: 0.01em;  /* Subtle */

/* Headings */
line-height: 1.3;
font-weight: 600;        /* Semi-bold, not too heavy */
letter-spacing: -0.02em; /* Tighter for headings */

/* Navigation */
font-size: 0.95rem;
letter-spacing: 0.05em;  /* Slightly spaced for clarity */
text-transform: none;    /* Keep natural case (more minimal than uppercase) */
```

### Hierarchy Guidelines
1. **Clear Contrast**: Maintain significant size difference between levels
2. **Weight Variation**: Use font weight to create hierarchy within same size
3. **Spacing**: Add more margin above headings than below
4. **Consistency**: Use same heading styles throughout the site

---

## Layout & Spacing

### Content Width
```css
Max Content Width: 720px   /* Optimal reading length (60-75 characters) */
Wide Content:      960px   /* For images, galleries, code blocks */
Full Width:        1200px  /* Maximum container width */
```

### Spacing System
Use a consistent spacing scale based on 8px increments:

```
xs:  0.5rem  (8px)   - Tight inline spacing
sm:  1rem    (16px)  - Default element spacing
md:  1.5rem  (24px)  - Section spacing
lg:  2.5rem  (40px)  - Major section breaks
xl:  4rem    (64px)  - Page section dividers
xxl: 6rem    (96px)  - Hero sections, major breaks
```

### Vertical Rhythm
```css
/* Paragraphs */
margin-bottom: 1.5rem;

/* Headings */
H1: margin-top: 3rem, margin-bottom: 1.5rem;
H2: margin-top: 2.5rem, margin-bottom: 1rem;
H3: margin-top: 2rem, margin-bottom: 0.75rem;

/* Lists */
margin-bottom: 1.5rem;
list-style-position: outside;
padding-left: 1.5rem;

/* Images */
margin: 2.5rem 0;
```

### Grid System
- **Blog List**: Single column, full-width cards
- **Image Galleries**: 2-3 column grid with consistent gaps (2rem)
- **Sidebar**: Avoid if possible; use single-column layouts

---

## Navigation & Header

### Header Design
```
Layout: Minimal, fixed-top (optional)
Height: 80px
Background: Transparent → White on scroll
Transition: Smooth (300ms ease)
```

### Header Elements
```css
/* Logo/Site Title */
font-family: 'Lora', serif;  /* Changed from Pacifico for minimalism */
font-size: 1.5rem;
font-weight: 600;
color: #2D2D2D;
letter-spacing: 0.02em;

/* Navigation Links */
font-family: 'Inter', sans-serif;
font-size: 0.95rem;
font-weight: 500;
color: #6B6B6B;
letter-spacing: 0.05em;

/* Hover State */
color: #A88878;
transition: color 200ms ease;
```

### Navigation Structure
- **Primary Nav**: Home, Blog, About (right-aligned or center)
- **No Dropdown Menus**: Keep flat structure
- **Mobile**: Hamburger menu with slide-in drawer (from right)

### Visual Style
- **No borders** around header
- **Subtle shadow** only on scroll: `box-shadow: 0 2px 8px rgba(0,0,0,0.04)`
- **Clean separation** from content with whitespace, not lines

---

## Content Elements

### Blog Post Cards

#### List View
```css
/* Card Container */
background: transparent;
border: none;
border-bottom: 1px solid #E8E8E8;
padding: 2.5rem 0;
transition: none; /* Minimal - no hover effects */

/* Last item */
border-bottom: none;

/* Title */
font-family: 'Lora', serif;
font-size: 1.75rem;
font-weight: 600;
color: #2D2D2D;
margin-bottom: 0.5rem;

/* Metadata (date, tags) */
font-size: 0.875rem;
color: #6B6B6B;
margin-bottom: 0.75rem;

/* Excerpt */
font-size: 1rem;
line-height: 1.7;
color: #505050;
```

#### Featured Image
```css
/* When present */
width: 100%;
max-width: 720px;
margin: 1.5rem 0;
border-radius: 4px; /* Subtle, not too rounded */
aspect-ratio: 16/9; /* Consistent sizing */

/* No shadow, no overlay, no effects */
```

### Article Page

#### Title Section
```css
/* Title */
font-size: 2.5rem;
line-height: 1.2;
margin-bottom: 1rem;
max-width: 720px;
margin-left: auto;
margin-right: auto;

/* Metadata bar */
display: flex;
gap: 1.5rem;
font-size: 0.875rem;
color: #6B6B6B;
margin-bottom: 3rem;
border-bottom: 1px solid #E8E8E8;
padding-bottom: 1.5rem;
```

#### Content Styling
```css
/* Paragraphs */
font-size: 1.125rem;
line-height: 1.8;
margin-bottom: 1.5rem;
color: #2D2D2D;

/* Links */
color: #A88878;
text-decoration: underline;
text-decoration-color: rgba(168, 136, 120, 0.3);
text-underline-offset: 3px;
transition: text-decoration-color 200ms ease;

/* Link Hover */
text-decoration-color: #A88878;

/* Blockquotes */
border-left: 3px solid #C8A898;
padding-left: 1.5rem;
margin: 2rem 0;
font-style: italic;
color: #505050;

/* Lists */
line-height: 1.7;
margin-bottom: 1.5rem;
```

### Images

#### In-Content Images
```css
max-width: 100%;
height: auto;
margin: 2.5rem auto;
display: block;
border-radius: 4px;

/* No shadows, no borders */

/* Captions (if any) */
text-align: center;
font-size: 0.875rem;
color: #6B6B6B;
margin-top: 0.75rem;
font-style: italic;
```

#### Image Galleries
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 2rem;
margin: 3rem 0;

/* Individual images */
aspect-ratio: 4/3;
object-fit: cover;
border-radius: 4px;
```

### Tags

```css
/* Tag Container */
display: inline-flex;
gap: 0.5rem;
flex-wrap: wrap;

/* Individual Tag */
background: #F7F7F7;
color: #505050;
padding: 0.25rem 0.75rem;
border-radius: 3px;
font-size: 0.8rem;
font-weight: 500;
text-decoration: none;
transition: background 200ms ease;

/* Hover */
background: #C8A898;
color: #FFFFFF;
```

### Code Blocks

```css
/* Inline Code */
background: #F7F7F7;
color: #505050;
padding: 0.2em 0.4em;
border-radius: 3px;
font-size: 0.9em;
font-family: 'JetBrains Mono', monospace;

/* Code Blocks */
background: #F7F7F7;
border: 1px solid #E8E8E8;
border-radius: 4px;
padding: 1.5rem;
overflow-x: auto;
font-size: 0.9rem;
line-height: 1.6;
margin: 2rem 0;

/* No syntax highlighting colors - keep minimal */
/* Use subtle grays only */
```

---

## Footer

### Design
```css
background: #FAFAFA;
border-top: 1px solid #E8E8E8;
padding: 3rem 0 2rem;
margin-top: 6rem;
font-size: 0.875rem;
color: #6B6B6B;
text-align: center;
```

### Content
- Copyright notice
- Minimal social links (if any)
- "Scroll to top" link
- **No heavy elements** - keep lightweight

---

## Responsive Design

### Breakpoints
```css
Mobile:  < 640px
Tablet:  640px - 1024px
Desktop: > 1024px
```

### Mobile Adjustments

#### Typography
```css
/* Scale down on mobile */
H1: 2rem (from 2.5rem)
H2: 1.5rem (from 2rem)
Body: 1rem (from 1.125rem)
Line-height: 1.7 (from 1.8)
```

#### Spacing
```css
/* Reduce spacing scale by ~25% */
lg: 2rem (from 2.5rem)
xl: 3rem (from 4rem)
xxl: 4rem (from 6rem)

/* Content padding */
padding: 0 1rem; /* Maintain readable edge spacing */
```

#### Navigation
```css
/* Mobile menu */
position: fixed;
top: 0;
right: 0;
width: 280px;
height: 100vh;
background: #FFFFFF;
transform: translateX(100%);
transition: transform 300ms ease;

/* Active state */
transform: translateX(0);
```

#### Images
```css
/* Full width on mobile */
width: 100%;
margin: 2rem -1rem; /* Break out of padding */

/* Galleries: Single column */
grid-template-columns: 1fr;
gap: 1.5rem;
```

---

## Animation & Interaction

### Philosophy
**Minimal, purposeful animations** - only where they enhance UX

### Allowed Animations
```css
/* Link hovers */
transition: color 200ms ease;

/* Header on scroll */
transition: box-shadow 300ms ease;

/* Mobile menu */
transition: transform 300ms ease;

/* Tag hovers */
transition: background 200ms ease;
```

### Prohibited
- ❌ Fade-in effects on page load
- ❌ Parallax scrolling
- ❌ Carousel/slider animations
- ❌ Decorative animations
- ❌ Hover shadows/scaling on cards

### Micro-interactions
- **Focus states**: Subtle outline in accent color
- **Button press**: Slight opacity change (0.8)
- **Smooth scroll**: When navigating to anchors

---

## Special Considerations

### Performance
1. **Font Loading**: Use `font-display: swap` for custom fonts
2. **Image Optimization**: WebP format, lazy loading
3. **Minimal CSS**: Avoid unused styles, use PurgeCSS
4. **No JavaScript animations**: CSS only

### Accessibility
1. **Color Contrast**: Maintain WCAG AA standard (4.5:1 minimum)
   - #2D2D2D on #FEFEFE = 12.6:1 ✓
   - #6B6B6B on #FEFEFE = 5.74:1 ✓
   - #A88878 on #FEFEFE = 3.8:1 ⚠️ (use for large text only)
2. **Focus Indicators**: Clear, visible focus states
3. **Alt Text**: All images must have descriptive alt text
4. **Semantic HTML**: Proper heading hierarchy, landmarks

### Content Guidelines
1. **Images**: High-quality, compressed, consistent aspect ratios
2. **Excerpts**: 150-200 characters for blog post previews
3. **Headings**: Use H2 for main sections, H3 for subsections
4. **Paragraphs**: Keep 3-5 sentences; break up long blocks

---

## Implementation Priority

### Phase 1: Foundation
1. ✓ Set up color variables
2. ✓ Implement typography system
3. ✓ Create spacing scale
4. ✓ Style basic content elements (headings, paragraphs, links)

### Phase 2: Layout
5. ✓ Build header/navigation
6. ✓ Style blog post cards
7. ✓ Create article page layout
8. ✓ Design footer

### Phase 3: Refinement
9. ✓ Add responsive breakpoints
10. ✓ Implement images and galleries
11. ✓ Style tags, metadata
12. ✓ Code block styling

### Phase 4: Polish
13. ✓ Micro-interactions and transitions
14. ✓ Mobile menu
15. ✓ Accessibility audit
16. ✓ Performance optimization

---

## File Structure for Implementation

```
assets/
├── css/
│   ├── custom.css          ← Main customization file
│   ├── variables.css       ← Color and spacing variables (create)
│   └── typography.css      ← Font definitions (create)
├── fonts/
│   ├── inter/              ← Inter font files
│   ├── lora/               ← Lora font files
│   └── jetbrains-mono/     ← JetBrains Mono (if needed)
└── images/
    └── ...
```

### Custom CSS Organization
```css
/* 1. Variables */
:root { ... }

/* 2. Typography */
@font-face { ... }
body { ... }
h1, h2, h3 { ... }

/* 3. Layout */
.container { ... }
.header { ... }

/* 4. Components */
.blog-card { ... }
.tag { ... }

/* 5. Utilities */
.sr-only { ... }

/* 6. Responsive */
@media (max-width: 640px) { ... }
```

---

## Hugo/Congo Theme Notes

### Customization Approach
1. **Override in `assets/css/custom.css`** - Main method
2. **Create layouts in `layouts/`** - For structural changes
3. **Modify `params.toml`** - For theme configuration
4. **Use Hugo's asset pipeline** - For CSS/JS processing

### Key Files to Modify
- `assets/css/custom.css` - All style overrides
- `config/_default/params.toml` - Theme settings
- `layouts/partials/` - Custom header, footer (if needed)

### Congo Theme Variables to Override
The Congo theme uses CSS variables that can be overridden:
```css
:root {
  --color-neutral: #FEFEFE;
  --color-neutral-700: #2D2D2D;
  --color-primary-600: #C8A898;
  /* etc. */
}
```

---

## Comparison: candaceabroad.com vs. This Design

| Element | Candace Abroad | This Blog (More Minimal) |
|---------|----------------|--------------------------|
| **Colors** | Multiple accent colors (rose, mauve, taupe) | Single accent (taupe) |
| **Typography** | 3 font families (Gelasio, Mulish, Overpass) | 2 font families (Lora, Inter) |
| **Nav Text** | Uppercase with letter-spacing | Natural case |
| **Shadows** | Multiple shadow effects | Minimal/none |
| **Borders** | Rounded shapes, circles | Subtle rectangles only |
| **Image Effects** | Circular masks, overlays | Clean, simple borders |
| **Hover Effects** | Box shadows, transforms | Color changes only |
| **Spacing** | Dense in some areas | Very generous throughout |
| **Base Font Size** | 23px | 18px (more standard) |

---

## Quick Reference: Key Values

```css
/* Colors */
--bg: #FEFEFE;
--text: #2D2D2D;
--accent: #C8A898;
--border: #E8E8E8;

/* Typography */
--font-serif: 'Lora', serif;
--font-sans: 'Inter', sans-serif;
--font-mono: 'JetBrains Mono', monospace;

/* Spacing */
--space-sm: 1rem;
--space-md: 1.5rem;
--space-lg: 2.5rem;
--space-xl: 4rem;

/* Layout */
--content-width: 720px;
--max-width: 1200px;

/* Transitions */
--transition-fast: 200ms ease;
--transition-normal: 300ms ease;
```

---

## Final Notes

This design prioritizes:
- **Readability** over decoration
- **Clarity** over complexity
- **Space** over density
- **Subtlety** over boldness

The goal is a timeless, elegant design that gets out of the way and lets your writing shine. When in doubt, **simplify further**.
