## ADDED Requirements

### Requirement: Bosk8 Token Adoption
The UI system SHALL use only tokens defined in `style.md` and the provided CSS variables mapping.

#### Scenario: Global base and container
- **WHEN** the app renders `main.bosk8`
- **THEN** it SHALL apply `--bg-elev1`, `--fs-base`, and `--font-ui`, with container width `min(1100px, 90vw)`

#### Scenario: Cards and borders
- **WHEN** a card surface is shown
- **THEN** it SHALL use `--surface-card` with outer ring `--border-outer-w` and color `--border-color`

### Requirement: Typography and Labels
The UI system MUST render UI labels in uppercase with `letter-spacing: 0.05em` using `--font-ui`.

#### Scenario: Meta text
- **WHEN** meta text is displayed
- **THEN** it SHALL use `.meta-sm` or `.meta-md` sizes and `--text-muted`

### Requirement: Interactive States
All focusable elements MUST define hover and focus-visible states per `style.md`.

#### Scenario: Link hover
- **WHEN** a `.link` is hovered
- **THEN** color transitions from `--text-muted` to `--text-primary` with underline offset 4px

#### Scenario: Keyboard focus
- **WHEN** an element receives keyboard focus
- **THEN** it SHALL show `outline: 2px solid var(--border-color)` on `--surface-card`

### Requirement: Tooltip Behavior
Tooltips MUST display on hover for ≥768px and on tap/click for <768px per `style.md`.

#### Scenario: Desktop hover
- **WHEN** pointer hovers `.tooltip-trigger`
- **THEN** `.tooltip` becomes visible with opacity transition

#### Scenario: Mobile tap
- **WHEN** `.tooltip-trigger` has class `active`
- **THEN** `.tooltip` becomes visible

### Requirement: Motion
Transitions MUST be ≤200ms and avoid large parallax.

#### Scenario: Button hover motion
- **WHEN** a primary action is hovered
- **THEN** transition durations SHALL be ≤200ms and subtle

## MODIFIED Requirements

## REMOVED Requirements


