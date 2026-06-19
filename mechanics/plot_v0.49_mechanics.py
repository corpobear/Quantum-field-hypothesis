#!/usr/bin/env python3
"""
Generate v0.49 MCIFT mechanics diagrams.

Status: speculative toy-model visualization, not established physics.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

STYLE = """
<style>
  .title { font: bold 24px sans-serif; }
  .label { font: 16px sans-serif; }
  .small { font: 13px sans-serif; }
  .box { fill: white; stroke: black; stroke-width: 2; rx: 12; }
  .node { fill: #f8f8f8; stroke: black; stroke-width: 2; }
  .arrow { stroke: black; stroke-width: 2.5; fill: none; marker-end: url(#arrow); }
  .dash { stroke: black; stroke-width: 2; stroke-dasharray: 7 6; fill: none; }
</style>
<defs>
  <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
    <path d="M2,2 L10,6 L2,10 Z" fill="black" />
  </marker>
</defs>
"""

def write(name: str, body: str, w: int = 1100, h: int = 700) -> None:
    (OUT / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n{STYLE}\n{body}\n</svg>\n',
        encoding='utf-8',
    )

def main() -> None:
    write('dense_entanglement_compression.svg', '''
<text x="550" y="45" text-anchor="middle" class="title">Dense entanglement compression</text>
<circle cx="250" cy="260" r="95" class="node"/>
<circle cx="470" cy="260" r="95" class="node"/>
<text x="250" y="255" text-anchor="middle" class="label">sphere A</text>
<text x="250" y="280" text-anchor="middle" class="small">m_A, R_A</text>
<text x="470" y="255" text-anchor="middle" class="label">sphere B</text>
<text x="470" y="280" text-anchor="middle" class="small">m_B, R_B</text>
<path d="M 350 260 L 370 260" class="arrow"/>
<path d="M 585 260 C 660 260, 675 260, 730 260" class="arrow"/>
<circle cx="850" cy="260" r="82" class="node"/>
<circle cx="850" cy="260" r="115" class="dash"/>
<text x="850" y="250" text-anchor="middle" class="label">dense merge</text>
<text x="850" y="276" text-anchor="middle" class="small">R_dense &lt; R_volume</text>
<rect x="260" y="470" width="580" height="130" class="box"/>
<text x="550" y="505" text-anchor="middle" class="label">R_volume = (R_A^3 + R_B^3)^(1/3)</text>
<text x="550" y="535" text-anchor="middle" class="label">R_dense = lambda_R R_volume</text>
<text x="550" y="565" text-anchor="middle" class="label">rho_ratio = (R_volume/R_dense)^3</text>
''')

    write('discarded_vibration_rotation.svg', '''
<text x="550" y="45" text-anchor="middle" class="title">Discarded vibration becomes final rotation</text>
<circle cx="305" cy="310" r="120" class="node"/>
<path d="M 220 225 C 285 165, 385 170, 445 240" class="dash"/>
<path d="M 445 240 L 435 213" class="arrow"/>
<text x="305" y="302" text-anchor="middle" class="label">merged dense core</text>
<text x="305" y="330" text-anchor="middle" class="small">I_dense = (2/5)MR^2</text>
<rect x="620" y="160" width="300" height="110" class="box"/>
<text x="770" y="195" text-anchor="middle" class="label">discarded beat</text>
<text x="770" y="225" text-anchor="middle" class="small">E_discarded = E_beat</text>
<path d="M 620 235 C 520 260, 480 285, 425 310" class="arrow"/>
<rect x="610" y="365" width="330" height="145" class="box"/>
<text x="775" y="405" text-anchor="middle" class="label">angular impulse</text>
<text x="775" y="435" text-anchor="middle" class="small">L = sqrt(2 I E_rotation)</text>
<text x="775" y="465" text-anchor="middle" class="small">omega_final = L/I</text>
<path d="M 610 430 C 525 420, 455 375, 405 340" class="arrow"/>
''')

    write('aero_drill_sink_shape_flow.svg', '''
<text x="550" y="45" text-anchor="middle" class="title">Drill / sink shape-flow stabilization</text>
<ellipse cx="550" cy="330" rx="150" ry="105" class="node"/>
<path d="M 405 330 C 460 245, 640 245, 695 330 C 640 415, 460 415, 405 330 Z" class="dash"/>
<path d="M 385 330 C 300 325, 245 300, 190 255" class="arrow"/>
<path d="M 710 330 C 800 340, 850 370, 910 420" class="arrow"/>
<path d="M 550 225 C 610 240, 635 285, 610 330" class="arrow"/>
<text x="550" y="320" text-anchor="middle" class="label">rotating core</text>
<text x="550" y="348" text-anchor="middle" class="small">drill index + sink intake</text>
<rect x="120" y="450" width="320" height="95" class="box"/>
<text x="280" y="485" text-anchor="middle" class="label">drag bleed</text>
<text x="280" y="515" text-anchor="middle" class="small">core load to shell flow</text>
<rect x="670" y="450" width="320" height="95" class="box"/>
<text x="830" y="485" text-anchor="middle" class="label">coherence lift</text>
<text x="830" y="515" text-anchor="middle" class="small">shape flow raises support</text>
''')

    write('visible_hidden_split_geometry.svg', '''
<text x="550" y="45" text-anchor="middle" class="title">Visible / hidden branch split</text>
<circle cx="550" cy="250" r="115" class="node"/>
<text x="550" y="242" text-anchor="middle" class="label">entangled merge</text>
<text x="550" y="270" text-anchor="middle" class="small">shared dense event</text>
<rect x="130" y="470" width="330" height="120" class="box"/>
<text x="295" y="510" text-anchor="middle" class="label">visible branch</text>
<text x="295" y="540" text-anchor="middle" class="small">face / vortex capture</text>
<text x="295" y="565" text-anchor="middle" class="small">then visible channel split</text>
<rect x="640" y="470" width="340" height="120" class="box"/>
<text x="810" y="510" text-anchor="middle" class="label">hidden branch</text>
<text x="810" y="540" text-anchor="middle" class="small">density shadow + sink intake</text>
<text x="810" y="565" text-anchor="middle" class="small">not added to visible channels</text>
<path d="M 500 350 C 430 415, 355 440, 300 470" class="arrow"/>
<path d="M 605 350 C 680 415, 760 440, 810 470" class="arrow"/>
''')

    write('hidden_core_load_feedback.svg', '''
<text x="550" y="45" text-anchor="middle" class="title">Hidden branch feeds rotating-core load</text>
<circle cx="550" cy="330" r="115" class="node"/>
<circle cx="550" cy="330" r="165" class="dash"/>
<text x="550" y="322" text-anchor="middle" class="label">rotating core</text>
<text x="550" y="350" text-anchor="middle" class="small">core pressure after feedback</text>
<rect x="90" y="150" width="260" height="110" class="box"/>
<text x="220" y="190" text-anchor="middle" class="label">visible load</text>
<text x="220" y="220" text-anchor="middle" class="small">G_visible = E_visible</text>
<rect x="760" y="150" width="270" height="110" class="box"/>
<text x="895" y="190" text-anchor="middle" class="label">hidden load</text>
<text x="895" y="220" text-anchor="middle" class="small">G_hidden = C_sink E_hidden</text>
<rect x="390" y="555" width="320" height="95" class="box"/>
<text x="550" y="592" text-anchor="middle" class="label">rotation load</text>
<text x="550" y="622" text-anchor="middle" class="small">G_rot = xi_rot E_rotation</text>
<path d="M 350 220 C 430 240, 475 270, 505 300" class="arrow"/>
<path d="M 760 220 C 680 240, 630 270, 595 300" class="arrow"/>
<path d="M 550 555 C 550 500, 550 470, 550 445" class="arrow"/>
<text x="550" y="120" text-anchor="middle" class="small">G_load = G_visible + G_hidden + G_rot</text>
''')

if __name__ == '__main__':
    main()
