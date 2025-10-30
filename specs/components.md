# Interactive Component Library

## Component Specifications

Each component includes: name, purpose, props, variants, states, example usage, accessibility notes, and exact `style.md` token references.

---

## Card

### Purpose
Container for grouped content, providing visual separation and depth via borders and shadows.

### Props
- `variant`: "default" | "metrics" | "table" | "error"
- `className`: Optional additional CSS classes
- `borderBottom`: Boolean (adds `border-b` class)
- `children`: React/HTML content

### Variants
- **default**: Standard card with padding `var(--space-1)`
- **metrics**: Padding `var(--space-4)` vertical, `var(--space-2)` horizontal, centered content
- **table**: Padding `var(--space-1)`, minimal padding for table container
- **error**: Padding `var(--space-1)`, text color `var(--text-subtle)`

### States
- **default**: Background `var(--surface-card)`, shadow applied
- **hover**: No hover state (Bosk8 minimal aesthetic)
- **focus**: Visible focus outline (`:focus-visible` rule from style.md)

### Style Tokens (style.md)
- Background: `--surface-card` (#09090B)
- Border: `--border-color` (rgb(39 39 42)), width `--border-w` (1px mobile, 1.5px desktop)
- Border outer: `--border-outer-w` (1px mobile, 2px desktop)
- Shadow: `--shadow-tint` (#0000000d)
- Border-radius: `--r-md` (6px)
- Padding: `--space-1` (1rem), `--space-2` (2rem), `--space-4` (4rem)

### Example Usage
```html
<div class="card border-b">
  <h1 class="tagline">CUSTOMER CHURN DASHBOARD</h1>
  <p class="meta-sm">ROC AUC: 0.842</p>
</div>
```

### Accessibility
- Semantic HTML: Use `<section>`, `<article>`, or `<div>` as appropriate
- ARIA: No required ARIA (container component)
- Focus: Inherits global `:focus-visible` outline

---

## Tagline / Heading

### Purpose
Primary page title, uppercase monospace label following Bosk8 typography rules.

### Props
- `level`: 1 | 2 | 3 (semantic heading level)
- `className`: Optional additional classes
- `children`: Text content

### Variants
- **tagline**: Primary heading (h1), size 1rem, centered
- **label**: Section heading (h2), size 0.875rem (meta-md), left-aligned
- **meta**: Secondary text, size 0.75rem (meta-sm)

### States
- **default**: Color `var(--text-muted)` (#E8E8E8)
- No hover/focus states (text element)

### Style Tokens (style.md)
- Font-family: `--font-ui` (JetBrains Mono stack)
- Text-transform: uppercase
- Letter-spacing: 0.05em
- Color: `--text-muted` (#E8E8E8)
- Font-size: `--fs-base` for tagline, `0.875rem` for meta-md, `0.75rem` for meta-sm
- Text-align: center (tagline), left (label/meta)

### Example Usage
```html
<h1 class="tagline">CUSTOMER CHURN DASHBOARD</h1>
<div class="label">SINGLE-CUSTOMER SCORING</div>
<p class="meta-sm">ROC AUC: 0.842</p>
```

### Accessibility
- Semantic HTML: Use `<h1>`, `<h2>`, `<h3>` as appropriate
- ARIA: No required ARIA for standard headings
- Screen readers: Proper heading hierarchy maintained

---

## Link

### Purpose
Text link for navigation or actions, with hover underline effect.

### Props
- `href`: URL destination (or `#` for anchor)
- `className`: Optional additional classes
- `children`: Link text

### Variants
- **default**: Standard link style

### States
- **default**: Color `var(--text-muted)`, no underline
- **hover**: Color `var(--text-primary)`, underline, offset 4px
- **focus**: Inherits `:focus-visible` outline
- **active**: Same as hover (no distinct active state)

### Style Tokens (style.md)
- Color: `--text-muted` (#E8E8E8) default, `--text-primary` (#FFFFFF) hover
- Text-decoration: none default, underline hover
- Text-underline-offset: 4px
- Transition: all 0.15s

### Example Usage
```html
<a href="#" class="link">EXPORT DATA</a>
```

### Accessibility
- Semantic HTML: Use `<a>` with valid `href`
- ARIA: No required ARIA for standard links
- Keyboard: Fully keyboard accessible (native)
- Focus: Visible focus outline

---

## Button (Derived)

### Purpose
Action trigger button. **Note:** style.md doesn't specify button component; derive from link style with padding and border.

### Props
- `type`: "button" | "submit" | "reset"
- `disabled`: Boolean
- `onClick`: Event handler
- `children`: Button text (uppercase recommended)

### Variants
- **primary**: Default action button
- **disabled**: Grayed out, non-interactive

### States
- **default**: Background transparent, border `var(--border-w) solid var(--border-color)`, padding `var(--space-0_75) var(--space-1)`, text `var(--text-muted)`, uppercase
- **hover**: Color `var(--text-primary)`, border color unchanged
- **focus**: `:focus-visible` outline
- **disabled**: Opacity 0.5, cursor not-allowed, no hover effect
- **active**: Slight opacity reduction (0.9)

### Style Tokens (style.md) — Derived
- Background: Transparent (derived from minimal aesthetic)
- Border: `--border-w` solid `--border-color`
- Padding: `--space-0_75` (0.75rem) vertical, `--space-1` (1rem) horizontal
- Color: `--text-muted` default, `--text-primary` hover
- Font-family: `--font-ui`
- Text-transform: uppercase (Bosk8 convention)
- Letter-spacing: 0.05em
- Transition: all 0.15s
- Border-radius: `--r-sm` (4px) — small radius for buttons

**Derivation Logic:** Buttons inherit link color behavior but add border and padding for visual weight. Small radius added for tactile feel.

### Example Usage
```html
<button type="submit" class="btn-primary">SCORE CUSTOMER</button>
```

### Accessibility
- Semantic HTML: Use `<button>` for actions, `<input type="submit">` for forms
- ARIA: `aria-label` if text unclear, `aria-disabled="true"` for disabled state
- Keyboard: Fully keyboard accessible (native)
- Focus: Visible focus outline

---

## Input (Derived)

### Purpose
Text/number input fields for form data entry.

### Props
- `type`: "text" | "number" | "email" | etc.
- `name`:иначе Input name attribute
- `required`: Boolean
- `disabled`: Boolean
- `placeholder`: Optional placeholder text
- `value`: Controlled value
- `onChange`: Event handler

### Variants
- **text**: Standard text input
- **number**: Numeric input with step controls
- **disabled**: Grayed out, non-editable

### States
- **default**: Background `var(--surface-card)`, border `var(--border-w) solid var(--border-color)`, padding `var(--space-0_75)`, color `var(--text-primary)`, font-family `--font-ui`
- **focus**: Border color unchanged, `:focus-visible` outline (2px solid `--border-color`)
- **disabled**: Opacity 0.5, background dimmed
- **error**: Border color `var(--text-subtle)` (no red, use muted color)

### Style Tokens (style.md) — Derived
- Background: `--surface-card` (#09090B)
- Border: `--border-w` solid `--border-color`
- Padding: `--space-0_75` (0.75rem)
- Color: `--text-primary` (#FFFFFF)
- Font-family: `--font-ui`
- Font-size: Inherits from base (`--fs-base`)
- Border-radius: `--r-sm` (4px)

**Derivation Logic:** Inputs use card surface background for contrast, thin borders for structure, and small radius for consistency.

### Example Usage
```html
<input type="number" name="tenure" class="input" min="0" max="72" required />
```

### Accessibility
- Semantic HTML: Use `<input>` with appropriate `type` and `label`
- ARIA: `aria-label` if no visible label, `aria-invalid="true"` for errors, `aria-describedby` for error messages
- Keyboard: Fully keyboard accessible (native)
- Focus: Visible focus outline
- Labels: Always associate `<label>` with inputs

---

## Select (Derived)

### Purpose
Dropdown selection for categorical choices.

### Props
- `name`: Select name attribute
- `required`: Boolean
- `disabled`: Boolean
- `value`: Controlled value
- `onChange`: Event handler
- `children`: `<option>` elements

### Variants
- **default**: Standard select dropdown
- **disabled**: Grayed out, non-interactive

### States
- **default**: Same as input (background, border, padding, color)
- **focus**: `:focus-visible` outline
- **disabled**: Opacity 0.5
- **hover**: Native browser hover (arrow indicator)

### Style Tokens (style.md) — Derived
- Same as Input component (inherits all input styles)

### Example Usage
```html
<select name="gender" class="input" required>
  <option value="">Select...</option>
  <option value="Male">Male</option>
  <option value="Female">Female</option>
</select>
```

### Accessibility
- Semantic HTML: Use `<select>` with `<option>` elements
- ARIA: `aria-label` if no visible label, `aria-disabled="true"` for disabled
- Keyboard: Fully keyboard accessible (native)
- Focus: Visible focus outline
- Labels: Always associate `<label>` with selects

---

## Table

### Purpose
Data table for displaying tabular information (top 500 customers).

### Props
- `data`: Array of row objects
- `columns`: Array of column definitions
- `sortable`: Boolean
- `className`: Optional additional classes

### Variants
- **default**: Standard data table
- **compact**: Reduced padding for dense data

### States
- **default**: Text color `var(--text-primary)`, background transparent
- **header**: Text `var(--text-muted)`, uppercase, letter-spacing 0.05em
- **row hover**: Background `var(--bg-elev1)` (subtle highlight)
- **sortable header**: Cursor pointer on hover

### Style Tokens (style.md) — Derived
- Background: Transparent (inherits from parent card)
- Border: Bottom border `var(--border-w) solid var(--border-color)` for header
- Color: `--text-primary` (#FFFFFF) for data, `--text-muted` (#E8E8E8) for headers
- Font-family: `--font-ui`
- Font-size: Inherits from base
- Padding: `var(--space-0_75)` for cells (derived from spacing tokens)
- Text-transform: uppercase for headers (Bosk8 convention)

**Derivation Logic:** Tables inherit parent background, use thin borders for structure, and apply uppercase to headers for consistency.

### Example Usage
```html
<table class="table">
  <thead>
    <tr>
      <th>customerID</th>
      <th>churn_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>7590-VHVEG</td>
      <td>0.987</td>
    </tr>
  </tbody>
</table>
```

### Accessibility
- Semantic HTML: Use `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>`
- ARIA: `aria-sort` on sortable headers, `aria-label` on table
- Keyboard: Native table navigation (Tab through cells)
- Focus: Visible focus outline on interactive headers

---

## Badge

### Purpose
Small label indicator for risk levels or status.

### Props
- `variant`: "low" | "medium" | "high"
- `children`: Badge text

### Variants
- **low**: Green accent color (success)
- **medium**: Muted text color
- **high**: Primary text color, bold

### States
- **default**: Text-only badge (no background, no border)
- No hover/focus (decorative element)

### Style Tokens (style.md) — Derived
- **low**: Color `--accent-success` (#22C55E)
- **medium**: Color `--text-muted` (#E8E8E8)
- **high**: Color `--text-primary` (#FFFFFF), font-weight bold
- Font-family: `--font-ui`
- Text-transform: uppercase
- Letter-spacing: 0.05em

**Derivation Logic:** Badges use existing color tokens for semantic meaning. Low risk = success green, medium = muted, high = primary (high contrast).

### Example Usage
```html
<span class="badge badge-high">HIGH RISK</span>
```

### Accessibility
- Semantic HTML: Use `<span>` or `<div>` (decorative)
- ARIA: No required ARIA (visual indicator)
- Screen readers: Ensure text is readable or provide `aria-label` if needed

---

## Error Card

### Purpose
Displays error messages with actionable guidance.

### Props
- `message`: Error message text
- `actionHint`: Optional action hint text
- `className`: Optional additional classes

### Variants
- **default**: Standard error card

### States
- **default**: Background `var(--surface-card)`, text `var(--text-subtle)`, padding `var(--space-1)`

### Style Tokens (style.md)
- Background: `--surface-card` (#09090B)
- Color: `--text-subtle` (#A1A1AA)
- Padding: `--space-1` (1rem)
- Font-family: `--font-ui`
- Font-size: `meta-sm` (0.75rem)

### Example Usage
```html
<div class="card error-card">
  <div class="meta-sm">Top risk CSV not found. Run scoring script first.</div>
</div>
```

### Accessibility
- Semantic HTML: Use `<div>` with `role="alert"` for important errors
- ARIA: `aria-live="polite"` or `aria-live="assertive"` for dynamic errors
- Screen readers: Error messages announced appropriately

---

## Metric Display

### Purpose
Large number display for key metrics (ROC AUC, churn probability).

### Props
- `label`: Metric label text
- `value`: Numeric or string value
- `format`: Optional formatting function
- `className`: Optional additional classes

### Variants
- **default**: Standard metric display
- **large**: Emphasized metric (probability display)

### States
- **default**: Label `var(--text-muted)`, value `var(--text-primary)`
- **unavailable**: Value text `var(--text-subtle)`, italic

### Style Tokens (style.md)
- Label color: `--text-muted` (#E8E8E8)
- Value color: `--text-primary` (#FFFFFF) or `--text-subtle` (#A1A1AA) if unavailable
- Font-family: `--font-ui`
- Font-size: `meta-sm` (0.75rem) for label, larger for value (1.5rem for large variant)

### Example Usage
```html
<div class="metric">
  <span class="meta-sm">ROC AUC</span>
  <span class="metric-value">0.842</span>
</div>
```

### Accessibility
- Semantic HTML: Use `<div>` or `<dl>` structure
- ARIA: `aria-label` for screen reader context if needed
- Screen readers: Ensure value is announced with context

---

## Component Composition Rules

### Reusability
- Components are atomic and composable
- Use composition over configuration where possible
- Maintain single responsibility per component

### Style Adherence
- All components must reference exact style.md tokens
- No new color/spacing tokens without derivation entry
- Border-radius, shadows, and spacing follow style.md strictly

### Accessibility First
- All interactive components keyboard accessible
- ARIA attributes used appropriately
- Focus states always visible
- Semantic HTML preferred

### Streamlit Integration Notes
- Many components are Streamlit native (dataframe, inputs, buttons)
- Custom styling applied via CSS injection
- Streamlit components styled to match Bosk8 aesthetic
- DIvergence from native Streamlit appearance expected (brand consistency prioritized)

