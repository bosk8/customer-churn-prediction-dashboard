# Developer Handoff Artifacts

## Design Tokens / CSS Token Map

All CSS variables from style.md, ready for injection into Streamlit app.

```css
:root {
  /* Typography */
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);

  /* Colors - Backgrounds */
  --bg-black: #000;
  --bg-elev1: #0A0A0A;
  --surface-card: #09090B;

  /* Colors - Text */
  --text-primary: #fff;
  --text-muted: #e8e8e8;
  --text-subtle: #a1a1aa;
  --text-dim: #71717a;
  --text-highlight: #f4f4f5;

  /* Colors - Accents */
  --accent-success: #22c55e;

  /* Borders */
  --border-color: rgb(39 39 42);
  --border-w: 1px;
  --border-outer-w: 1px;

  /* Shadows */
  --shadow-tint: #0000000d;

  /* Border Radius */
  --r-sm: 4px;
  --r-md: 6px;

  /* Spacing */
  --space-0_5: 0.5rem;
  --space-0_75: 0.75rem;
  --space-1: 1rem;
  --space-1_5: 1.5rem;
  --space-2: 2rem;
  --space-4: 4rem;
}

@media (min-width: 1024px) {
  :root {
    --border-w: 1.5px;
    --border-outer-w: 2px;
  }
}
```

---

## Component CSS Snippets

### Global Resets & Base
```css
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--fs-base); }
html, body {
  margin: 0;
  width: 100%;
  height: 100%;
  background-color: var(--bg-black);
  font-family: var(--font-ui);
  color: var(--text-primary);
}

main.bosk8 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: var(--space-4) var(--space-1) var(--space-1);
  padding-top: 10rem;
  background-color: var(--bg-elev1);
}

.container {
  width: 100%;
  max-width: min(1100px, 90vw);
  position: relative;
}
```

### Card Component
```css
.card {
  background-color: var(--surface-card);
  box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint);
  border-radius: var(--r-md);
}

.border-b {
  border-bottom: var(--border-w) solid var(--border-color);
}

.metrics-card {
  padding: var(--space-4) var(--space-2);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-0_5);
}

.table-card {
  padding: var(--space-1);
}

.error-card {
  padding: var(--space-1);
  color: var(--text-subtle);
}
```

### Typography
```css
.tagline, .meta, .label, .nav {
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}

.tagline {
  font-size: 1rem;
  text-align: center;
}

.meta-sm {
  font-size: 0.75rem;
}

.meta-md {
  font-size: 0.875rem;
}
```

### Form Elements (Derived)
```css
/* Input / Select */
input[type="text"],
input[type="number"],
select {
  background-color: var(--surface-card);
  border: var(--border-w) solid var(--border-color);
  padding: var(--space-0_75);
  color: var(--text-primary);
  font-family: var(--font-ui);
  font-size: inherit;
  border-radius: var(--r-sm);
}

input:focus-visible,
select:focus-visible {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
}

input:disabled,
select:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Button */
button {
  background: transparent;
  border: var(--border-w) solid var(--border-color);
  padding: var(--space-0_75) var(--space-1);
  color: var(--text-muted);
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-radius: var(--r-sm);
  transition: all 0.15s;
  cursor: pointer;
}

button:hover {
  color: var(--text-primary);
}

button:focus-visible {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### Focus States
```css
:focus-visible {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
}
```

### Links
```css
.link {
  color: var(--text-muted);
  text-decoration: none;
  transition: all 0.15s;
}

.link:hover {
  color: var(--text-primary);
  text-decoration: underline;
  text-underline-offset: 4px;
}
```

---

## HTML Structure Examples

### Header Card
```html
<section class="card metrics-card border-b">
  <h1 class="tagline">CUSTOMER CHURN DASHBOARD</h1>
  <p class="meta-sm">ROC AUC: 0.842</p>
</section>
```

### Table Card
```html
<div class="card table-card border-b">
  <div class="meta-md">TOP 500 AT-RISK CUSTOMERS</div>
  <!-- Streamlit dataframe component here -->
</div>
```

### Error Card
```html
<div class="card error-card">
  <div class="meta-sm">Top risk CSV not found. Run scoring script first.</div>
</div>
```

### Form Result Card
```html
<div class="card" style="padding: var(--space-1); border: var(--border-w) solid var(--border-color); border-radius: var(--r-md);">
  <div style="font-size: 1.5rem; color: var(--text-primary);">65.3%</div>
  <div style="color: var(--text-primary); font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em;">HIGH RISK</div>
  <div style="color: var(--text-muted); margin-top: var(--space-0_5);">Customer is at HIGH risk of churning.</div>
</div>
```

---

## Streamlit Integration Notes

### CSS Injection Pattern
```python
st.markdown(
    """
    <style>
    /* All CSS variables and component styles here */
    </style>
    """,
    unsafe_allow_html=True,
)
```

### Streamlit Component Overrides
- Streamlit's native components (dataframe, inputs, buttons) cannot be fully styled
- CSS injection overrides what's possible
- Priority: Brand consistency > Perfect Streamlit integration
- Acceptable deviations: Sidebar width, some form control styling

### Key Streamlit Components
- `st.dataframe()`: Table display (minimal styling possible)
- `st.number_input()`: Numeric inputs (CSS can override colors/borders)
- `st.selectbox()`: Dropdowns (CSS can override colors/borders)
- `st.button()`: Submit button (CSS can override colors/borders/padding)

---

## Spacing / Redlines

### Component Spacing Guidelines

**Header Card:**
- Padding: 4rem vertical, 2rem horizontal
- Gap between title and subtitle: 0.5rem

**Table Card:**
- Padding: 1rem all sides
- Gap between label and table: 0.5rem (implicit)

**Form Fields:**
- Spacing between adjacent fields: 1rem
- Spacing between logical groups: 1.5rem
- Padding inside inputs: 0.75rem

**Result Card:**
- Padding: 1rem all sides
- Gap between probability and badge: 0.5rem

**Container:**
- Max width: min(1100px, 90vw)
- Padding: 4rem top, 1rem sides/bottom (mobile)
- Padding: 4rem top, 2rem sides/bottom (desktop)

---

## Sample React/HTML Snippets (Reference)

### Complete Card with Content
```html
<main class="bosk8">
  <div class="container">
    <section class="card metrics-card border-b">
      <h1 class="tagline">CUSTOMER CHURN DASHBOARD</h1>
      <p class="meta-sm">ROC AUC: 0.842</p>
    </section>
    
    <section class="card table-card border-b">
      <div class="meta-md">TOP 500 AT-RISK CUSTOMERS</div>
      <!-- Table content -->
    </section>
  </div>
</main>
```

### Form Section
```html
<div class="form-section">
  <div class="label">SINGLE-CUSTOMER SCORING</div>
  
  <label for="tenure">Tenure (months)</label>
  <input type="number" id="tenure" name="tenure" min="0" max="72" required />
  
  <label for="gender">Gender</label>
  <select id="gender" name="gender" required>
    <option value="">Select...</option>
    <option value="Male">Male</option>
    <option value="Female">Female</option>
  </select>
  
  <button type="submit">SCORE CUSTOMER</button>
</div>
```

---

## Acceptance Checklist

### Visual Design
- [ ] All colors match style.md tokens exactly
- [ ] All spacing uses style.md spacing tokens
- [ ] Typography uses JetBrains Mono, uppercase labels, 0.05em letter-spacing
- [ ] Borders use correct widths (1px mobile, 1.5px desktop ≥1024px)
- [ ] Border-radius uses `--r-sm` (4px) for inputs/buttons, `--r-md` (6px) for cards
- [ ] Shadows use `--shadow-tint` and `--border-outer-w` pattern

### Component Implementation
- [ ] Header card displays with correct padding and alignment
- [ ] Table card displays with correct padding and border
- [ ] Error cards display with `--text-subtle` color
- [ ] Form inputs use `--surface-card` background, correct borders/padding
- [ ] Buttons use derived style (transparent bg, border, uppercase text)
- [ ] Risk badges use correct color mapping (green/muted/primary)

### Functionality
- [ ] Dashboard loads and displays top 500 table
- [ ] Model metrics display correctly (ROC AUC)
- [ ] Single-customer form accepts all 19 features
- [ ] Form submission generates churn probability
- [ ] Result displays with correct formatting (percentage, risk badge)
- [ ] Error states display correctly (missing artifacts)

### Accessibility
- [ ] All interactive elements keyboard accessible
- [ ] Focus outlines visible (2px solid `--border-color`, 2px offset)
- [ ] Form labels associated with inputs
- [ ] Error messages use `role="alert"` or `aria-live`
- [ ] Table headers announced correctly
- [ ] Color contrast meets WCAG AA (verified with tools)

### Responsive Behavior
- [ ] Mobile (< 768px): Reduced padding, sidebar hidden
- [ ] Tablet (768px - 1023px): Standard layout, sidebar collapsible
- [ ] Desktop (≥ 1024px): Increased border widths, full layout
- [ ] Text resizes correctly (clamp function working)

### Browser Compatibility
- [ ] Chrome/Edge: All styles render correctly
- [ ] Firefox: All styles render correctly
- [ ] Safari: All styles render correctly
- [ ] CSS variables supported (all modern browsers)

### Performance
- [ ] Dashboard loads in < 3 seconds
- [ ] CSS injection doesn't cause FOUC (Flash of Unstyled Content)
- [ ] Model loading doesn't block UI
- [ ] Table rendering handles 500 rows efficiently

### Documentation
- [ ] All style decisions documented in style-decisions-log.md
- [ ] All tokens mapped in style-compliance-matrix.md
- [ ] Component specs match implementation
- [ ] Accessibility checklist verified

---

## Known Limitations & Workarounds

### Streamlit Styling Limitations
- **Issue**: Streamlit components have default styling that cannot be fully overridden
- **Impact**: Some form controls may not perfectly match Bosk8 aesthetic
- **Workaround**: CSS injection overrides what's possible, accept minor deviations

### Sidebar Width
- **Issue**: Streamlit sidebar has fixed default width (280px)
- **Impact**: Cannot use Bosk8 container max-width for sidebar
- **Workaround**: Accept Streamlit default, focus on main content area compliance

### Table Styling
- **Issue**: Streamlit dataframe component has limited CSS customization
- **Impact**: Table may not perfectly match Bosk8 table spec
- **Workaround**: CSS injection for colors/fonts, accept native table structure

---

## Deployment Checklist

### Pre-Deployment
- [ ] All artifacts exist: `model.joblib`, `top_risk.csv`, `metrics.json`
- [ ] Training script produces ROC AUC ≥ 0.75
- [ ] Scoring script generates correct top 500 CSV
- [ ] Local Streamlit app runs without errors

### Deployment
- [ ] Push to GitHub (public repository)
- [ ] Deploy to Streamlit Community Cloud
- [ ] Set main file path: `app/streamlit_app.py`
- [ ] Verify CSS injection works in deployed environment
- [ ] Verify artifact paths (relative paths may need adjustment for deployment)

### Post-Deployment
- [ ] Test all functionality in production
- [ ] Verify accessibility (keyboard navigation, screen reader compatibility)
- [ ] Test on multiple browsers
- [ ] Verify responsive behavior on mobile/tablet
- [ ] Check console for CSS/JavaScript errors

---

## Support & Questions

### Style Questions
- Refer to `style.md` (canonical reference)
- Refer to `style-decisions-log.md` for derivations
- Refer to `style-compliance-matrix.md` for token mappings

### Implementation Questions
- Refer to `components.md` for component specs
- Refer to `screens.md` for screen layouts
- Refer to `function-to-ui-mapping.md` for backend integration

### Accessibility Questions
- Refer to `accessibility-checklist.md` for WCAG requirements
- Test with automated tools (axe DevTools, WAVE)
- Manual testing with screen readers recommended

