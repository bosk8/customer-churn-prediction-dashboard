## ADDED Requirements

### Requirement: Card
Cards SHALL use `--surface-card`, outer ring `--border-outer-w` `--border-color`, shadow `--shadow-tint`, and radius `--r-md`.

#### Scenario: Default
- **WHEN** a `.card` is rendered
- **THEN** apply box-shadow `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)`

### Requirement: Button (Mono)
Buttons MUST be minimalist with uppercase labels, `letter-spacing: .05em`, hover state ≤200ms; colors derived from text tokens on `--surface-card`.

#### Scenario: Default/hover/focus/disabled
- **WHEN** default
- **THEN** text `--text-muted`; border `--border-w` `--border-color`
- **WHEN** hover
- **THEN** text `--text-primary`
- **WHEN** focus-visible
- **THEN** outline `2px` `--border-color`
- **WHEN** disabled
- **THEN** text `--text-dim`, pointer-events none

### Requirement: Table
Tables MUST support sticky header, sortable columns, and row hover with subtle background `#18181b` per `style.md` FAQ hover guidance.

#### Scenario: Sticky header
- **WHEN** table scrolls
- **THEN** header remains fixed and uses border `--border-w`

### Requirement: Tooltip
As defined in `style.md` Tooltip Pattern.

#### Scenario: Tokens
- **WHEN** rendering tooltip
- **THEN** use `--surface-card`, `--border-w`, `--border-color`, font `--font-ui`, and sizing `.625rem`

### Requirement: Accordion (FAQ)
As defined in `style.md` FAQ/Accordion Pattern.

#### Scenario: Active answer
- **WHEN** item active
- **THEN** `.faq-a.active { display: block; }`

### Requirement: Typography Components
`Tagline`, `Meta`, `Label`, `Nav` MUST use uppercase, `--font-ui`, `letter-spacing: .05em`.

#### Scenario: Sizes
- **WHEN** `.meta-sm` or `.meta-md` used
- **THEN** apply font-sizes `.75rem` and `.875rem` respectively

## MODIFIED Requirements

## REMOVED Requirements


