# AGENTS.md

Guidance for AI coding agents working in this repository.

---

## Project identity

This repository began as the **Multi-Channel Information Field Theory (MCIFT)** / `Quantum-field-hypothesis` toy-model research project.

It is now allowed to grow a second track:

```text
MCIFT Field Engine
```

The engine track repurposes the MCIFT ideas as a **procedural 3D field/voxel/simulation engine**, not as established physics.

Always preserve this distinction:

```text
physics-theory docs = speculative toy-model research
engine code         = software / simulation / rendering prototype
```

Do not present MCIFT as confirmed physics.

---

## Current engine direction

Use **Python** for the first engine prototype.

Python is acceptable for the prototype because the immediate goal is fast iteration on field behavior, channel activation, visualization, and gameplay/simulation rules.

The first engine should be small, inspectable, and testable before performance optimization.

Preferred first stack:

```text
Python 3.11+
Panda3D for the first interactive 3D shell
NumPy for dense field/channel arrays
pytest for tests
ruff for linting
```

Possible later additions:

```text
Numba for CPU acceleration
ModernGL for custom low-level GPU experiments
Pydantic for config/schema validation
Pillow/imageio for debug image output
trimesh or meshio for geometry import/export experiments
```

Do not add heavy dependencies until there is a specific engine need.

---

## Engine concept

The engine should treat the world as a multi-channel field:

```text
Psi[x, y, z, channel]
```

Suggested core channels:

```text
light       render visibility / emission / color activation
mass        solidity / inertia / collision weight
gravity     attraction or field pull
phase       coherence / vortex orientation / interaction alignment
motion      velocity or flow vector
sound       audio emission / acoustic trace
damage      gameplay hazard / destructive activation
ai          targetability / agent-interest field
```

A visible object is not just a mesh. It is a stable channel cluster.

Use these software terms:

```text
FieldGrid       dense or sparse storage for Psi
ChannelSet      named channel indices and semantics
KnotEntity      stable cluster projected from the field
ActivationRule  rule that converts channels into behavior
ExchangeSolver  interaction/update step between nearby clusters
RendererBridge  converts visible channel data into draw calls
PhysicsBridge   converts mass/collision channels into collider proxies
```

---

## Manifest states

Keep the MCIFT manifest-state language, but use it as engine semantics.

```text
visible-manifest:
  light-active + mass-active + coherent
  rendered and physically interactive

dark-manifest:
  light-inactive + mass/gravity-active
  invisible but physically or gravitationally interactive

unmanifest:
  inactive or below threshold
  stored as latent field potential, not rendered and not colliding
```

This is one of the most useful parts of the framework for a game/simulation engine.

---

## Recommended first prototype

Build the smallest possible interactive demo:

```text
1. Create a 3D field grid.
2. Seed a few channel clusters.
3. Run a simple update loop.
4. Render only light-active clusters.
5. Show dark-manifest clusters indirectly through particle distortion or gravity pull.
6. Allow user input to inject light/mass/phase into the field.
7. Log metrics each frame.
```

Target behavior:

```text
visible object     = rendered + collidable
dark object        = invisible + affects particles or gravity
unmanifest object  = latent + no visible/physical projection
```

---

## Folder plan

Add engine code under:

```text
engine/
```

Suggested layout:

```text
engine/
  README.md
  pyproject.toml
  src/mcift_engine/
    __init__.py
    field.py
    channels.py
    entities.py
    activation.py
    exchange.py
    render_panda3d.py
    physics.py
    demo.py
  tests/
    test_field.py
    test_activation.py
    test_exchange.py
  examples/
    minimal_field_demo.py
```

Keep existing theory/model folders intact:

```text
models/
mechanics/
paper/
notes/
tests/
analysis/
```

Do not mix engine code into theory reports unless documenting an explicit software experiment.

---

## Coding standards

Use plain, readable Python.

Required standards for engine code:

```text
Python 3.11+
type hints for public functions/classes
dataclasses for simple data containers
NumPy arrays for field storage
small modules with clear responsibilities
pytest tests for non-rendering logic
ruff linting before committing
```

Avoid:

```text
global mutable state
large untested scripts
hard-coded magic constants without comments
physics claims inside engine code
rendering code mixed into core field math
```

Core field logic must be testable without opening a window.

---

## Performance rules

Prototype first. Optimize second.

Initial limits:

```text
small grid sizes only, e.g. 32^3 or 64^3
single-machine local demo
no networking
no giant asset pipeline
no premature GPU compute system
```

Only optimize when a benchmark shows a real bottleneck.

Optimization path:

```text
1. vectorize NumPy operations
2. reduce allocations
3. use sparse chunks if needed
4. add Numba for hot CPU loops
5. only then explore GPU compute or ModernGL paths
```

---

## Testing requirements

Every engine change should prefer at least one non-rendering test.

Test examples:

```text
FieldGrid initializes with expected shape
channel names map to stable indices
visible-manifest threshold activates correctly
dark-manifest remains invisible but mass/gravity-active
exchange solver conserves or intentionally changes total channel amount
user input injection modifies only intended channels
```

Rendering demos may be smoke-tested manually at first, but core logic should remain automated.

---

## Documentation rules

When adding engine features, document them in engine language first.

Good:

```text
Dark-manifest cluster applies a gravity-like pull to nearby particles while remaining invisible.
```

Avoid:

```text
This proves dark matter works this way.
```

Use explicit status labels:

```text
software prototype
simulation metaphor
gameplay rule
visualization experiment
speculative toy-model idea
```

---

## Safety and scientific honesty

Do not convert speculative MCIFT mechanics into factual physics claims.

When writing theory docs, use language like:

```text
hypothesis
toy model
internal consistency check
simulation metaphor
not established physics
not experimental confirmation
```

When writing engine docs, use language like:

```text
field engine
channel activation
procedural simulation
rendering rule
interaction rule
```

---

## Dependency guidance

Minimum engine prototype requirements:

```text
python>=3.11
numpy
panda3d
pytest
ruff
```

Recommended dev extras:

```text
black or ruff-format
mypy or pyright
pre-commit
```

Optional later requirements:

```text
numba
moderngl
pydantic
pillow
imageio
trimesh
meshio
```

Add new dependencies only with a short note explaining why they are needed.

---

## First useful tasks for agents

Start here:

```text
1. Create engine/pyproject.toml.
2. Create src/mcift_engine/channels.py.
3. Create src/mcift_engine/field.py.
4. Add tests for channel indexing and FieldGrid shape.
5. Add a minimal Panda3D demo that renders light-active clusters as simple spheres/cubes.
6. Add a dark-manifest demo where invisible clusters distort visible particles.
```

Do not start with a full game, full physics engine, or custom GPU renderer.

---

## Commit hygiene

Keep commits focused.

Good commit examples:

```text
Add engine field grid prototype
Add channel activation tests
Add Panda3D minimal field demo
Document dark-manifest engine semantics
```

Avoid mixing unrelated changes, such as theory-model rewrites plus engine renderer code in one commit.
