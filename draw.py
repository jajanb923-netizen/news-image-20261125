#!/usr/bin/env python3
"""Draw the news-image-20261125 front page with Pillow (stdlib + Pillow).

Three layout variants (v1/v2/v3) of one newspaper front page summing up
Wednesday 25 November 2026, from reporting published that day. All text
is drawn with Pillow, so no glyph comes out garbled. Run:
    python3 draw.py [v1|v2|v3|all]
Writes candidates/<variant>.png (1024x1024) next to this file.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "candidates"

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (26, 26, 26)
NAVY = (19, 38, 63)
RED = (166, 25, 46)
GOLD = (201, 162, 39)
BLUE = (31, 95, 168)
TEAL = (14, 124, 123)
LIGHT = (255, 255, 255)
BORDER = (198, 190, 172)
GREY = (90, 86, 78)
SEA = (46, 110, 158)
SKY = (214, 232, 244)

DATE_LINE = "WEDNESDAY  •  25 NOVEMBER 2026"

# Stories, each verified from reporting published 25 Nov 2026.
LEAD = {
    "kicker": "WAR AT SEA — KYIV CONFIRMS",
    "headline": "ZELENSKYY CONFIRMS UKRAINE HIT RUSSIAN SHIPS",
    "deck": ("Kyiv says its drones sank the corvette Merkury off "
             "Benghazi, Libya, and hit the cargo ship Sparta II in "
             "the Gulf of Finland. Russia calls the strikes "
             "\u201cterrorism\u201d; Norway urges caution."),
    "credit": "Reuters  •  Bloomberg  •  RFE/RL",
}
HUAWEI = {
    "kicker": "U.S.  •  TECH  •  LAW",
    "headline": "HUAWEI GUILTY IN U.S. TRIAL",
    "deck": ("A Brooklyn jury convicts Huawei on 10 of 12 counts — "
             "Iran sanctions, bank fraud, trade-secret theft."),
}
RIYADH = {
    "kicker": "MIDDLE EAST",
    "headline": "DRONE HITS RIYADH'S TALLEST TOWER",
    "deck": ("Eleven wounded as a drone strikes the PIF Tower, the "
             "Saudi capital's tallest, for the second time in a week."),
}
NATO = {
    "kicker": "EUROPE  •  SECURITY",
    "headline": "NATO SENDS RADAR PLANE TO POLAND",
    "deck": ("AWACS plane to watch Poland's skies after Russian "
             "missiles landed there."),
}
CRICKET = {
    "kicker": "SPORT  •  CRICKET",
    "headline": "15-YEAR-OLD SMASHES 204 OFF 53 BALLS",
    "deck": ("Sooryavanshi hits the fastest List A double hundred — "
             "a world record."),
}
TICKER = ("Nepal quake 5.6 rocks Koshi  •  States sue SpaceX over Grok  •  "
          "Trump honours Giuliani  •  BJP–SAD reunite  •  Gukesh holds Sindarov")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def fit_headline(draw, text, path, start, max_w, max_lines):
    """Largest size (down to 18) whose wrap fits max_lines lines."""
    size = start
    while size > 18:
        fnt = font(path, size)
        lines = wrap(draw, text, fnt, max_w)
        if len(lines) <= max_lines:
            return fnt, lines
        size -= 2
    fnt = font(path, size)
    return fnt, wrap(draw, text, fnt, max_w)


def panel(draw, box, fill=LIGHT, outline=BORDER, width=2):
    draw.rectangle(box, fill=fill, outline=outline, width=width)


def masthead(draw):
    draw.rectangle([0, 0, W, 96], fill=NAVY)
    draw.rectangle([0, 96, W, 100], fill=GOLD)
    f = font(SERIF_B, 62)
    t = "THE WORLD"
    draw.text(((W - draw.textlength(t, font=f)) / 2, 12), t, font=f,
              fill=(255, 255, 255))
    f2 = font(SANS, 15)
    t2 = "ONE DAY  •  ONE PAGE  •  THE WORLD'S NEWS"
    draw.text(((W - draw.textlength(t2, font=f2)) / 2, 74), t2, font=f2,
              fill=(201, 162, 39))


def dateband(draw, y=100, h=40):
    draw.rectangle([0, y, W, y + h], fill=RED)
    f = font(SANS_B, 26)
    draw.text(((W - draw.textlength(DATE_LINE, font=f)) / 2, y + 6),
              DATE_LINE, font=f, fill=(255, 255, 255))


def ticker(draw, y=976, h=30):
    draw.rectangle([0, y, W, y + h], fill=NAVY)
    size = 15
    while size > 11:
        f = font(SANS_B, size)
        if draw.textlength(TICKER, font=f) <= W - 28:
            break
        size -= 1
    draw.text((14, y + 7), TICKER, font=f, fill=(255, 255, 255))


def footer(draw, y=1008):
    f = font(SANS, 12)
    t = "All stories as reported on 25 November 2026  •  Sources: Reuters, Bloomberg, AP, BBC, RFE/RL"
    draw.text(((W - draw.textlength(t, font=f)) / 2, y), t, font=f, fill=GREY)


# ---------------------------------------------------------------- illustrations
def draw_sea(draw, box):
    """Two ships on a grey-blue sea: a sinking corvette (left) and a
    cargo ship with smoke (right); three drone silhouettes above."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=SKY)
    # sun / haze
    draw.ellipse([x1 - 120, y0 + 14, x1 - 52, y0 + 82], fill=(250, 214, 120))
    # sea
    draw.rectangle([x0, y1 - 78, x1, y1], fill=SEA)
    for i, yy in enumerate(range(y1 - 66, y1 - 6, 16)):
        c = (255, 255, 255) if i % 2 == 0 else (170, 205, 228)
        draw.line([x0 + 14, yy, x1 - 14, yy], fill=c, width=3)
    # sinking corvette, listing to port
    hx, hy = x0 + 30, y1 - 130
    draw.polygon([(hx, hy + 34), (hx + 150, hy + 52), (hx + 190, hy + 34),
                  (hx + 176, hy + 62), (hx + 10, hy + 62)],
                 fill=(70, 76, 84))
    draw.rectangle([hx + 52, hy + 8, hx + 96, hy + 36], fill=(52, 58, 66))
    draw.line([hx + 74, hy + 8, hx + 74, hy - 14], fill=(52, 58, 66), width=4)
    # smoke from the corvette
    for cx, cy, r in [(hx + 120, hy - 6, 26), (hx + 146, hy - 26, 32),
                      (hx + 176, hy - 50, 26)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 120, 118))
    # cargo ship Sparta II, upright, smoke from its bow
    cx0, cy0 = x0 + 250, y1 - 118
    draw.polygon([(cx0, cy0 + 30), (cx0 + 150, cy0 + 30), (cx0 + 138, cy0 + 58),
                  (cx0 + 12, cy0 + 58)], fill=(146, 44, 44))
    draw.rectangle([cx0 + 96, cy0 + 2, cx0 + 138, cy0 + 30], fill=(240, 238, 230))
    draw.rectangle([cx0 + 18, cy0 + 8, cx0 + 52, cy0 + 30], fill=(240, 238, 230))
    for sx, sy, r in [(cx0 + 34, cy0 - 8, 20), (cx0 + 56, cy0 - 28, 24),
                      (cx0 + 82, cy0 - 46, 18)]:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(140, 140, 138))
    # drones
    for dx, dy in [(x0 + 60, y0 + 26), (x0 + 190, y0 + 44), (x0 + 250, y0 + 22)]:
        draw.line([dx - 12, dy, dx + 12, dy], fill=(40, 40, 40), width=3)
        draw.ellipse([dx - 5, dy - 4, dx + 5, dy + 4], fill=(40, 40, 40))
    # caption strip: two stacked lines, never overlapping
    draw.rectangle([x0, y1 - 46, x1, y1], fill=NAVY)
    lf = font(SANS_B, 13)
    draw.text((x0 + 12, y1 - 42), "MERKURY — SUNK OFF LIBYA",
              font=lf, fill=(255, 255, 255))
    draw.text((x0 + 12, y1 - 22), "SPARTA II — HIT IN THE BALTIC",
              font=lf, fill=(255, 255, 255))


def draw_tower(draw, box):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle(box, fill=(232, 226, 214))
    # PIF tower: tall, tapering, glassy — all box-relative
    draw.polygon([(x0 + int(w * 0.30), y1),
                  (x0 + int(w * 0.36), y0 + int(h * 0.10)),
                  (x0 + int(w * 0.62), y0 + int(h * 0.10)),
                  (x0 + int(w * 0.68), y1)], fill=(64, 96, 128))
    for i in range(1, 6):
        yy = y0 + int(h * (0.16 + 0.13 * i))
        draw.line([x0 + int(w * 0.33), yy, x0 + int(w * 0.65), yy],
                  fill=(150, 180, 205), width=2)
    # blast mark halfway up + smoke, kept inside the box
    bx, by = x0 + int(w * 0.49), y0 + int(h * 0.52)
    draw.ellipse([bx - 12, by - 10, bx + 12, by + 10], fill=(60, 60, 60))
    for fx, fy, r in [(0.72, 0.30, 12), (0.84, 0.18, 15), (0.92, 0.34, 9)]:
        cx, cy = x0 + int(w * fx), y0 + int(h * fy)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(150, 150, 148))
    # ground + small buildings
    draw.rectangle([x0, y1 - 10, x1, y1], fill=(120, 116, 108))
    draw.rectangle([x0 + int(w * 0.06), y1 - int(h * 0.38),
                    x0 + int(w * 0.20), y1 - 10], fill=(150, 146, 138))
    draw.rectangle([x0 + int(w * 0.78), y1 - int(h * 0.30),
                    x0 + int(w * 0.90), y1 - 10], fill=(150, 146, 138))


def draw_court(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(232, 226, 214))
    # gavel + sound block
    draw.rectangle([x0 + 30, y1 - 34, x0 + 150, y1 - 20], fill=(120, 82, 40))
    draw.rectangle([x0 + 82, y1 - 58, x0 + 96, y1 - 34], fill=(90, 60, 28))
    draw.rectangle([x0 + 44, y1 - 92, x0 + 134, y1 - 58], fill=(146, 100, 48))
    draw.line([x0 + 44, y1 - 92, x0 + 134, y1 - 58], fill=(90, 60, 28), width=3)
    # scales of justice, small
    draw.line([x0 + 150, y0 + 26, x0 + 150, y0 + 78], fill=(90, 60, 28), width=4)
    draw.line([x0 + 122, y0 + 34, x0 + 178, y0 + 34], fill=(90, 60, 28), width=4)
    draw.polygon([(x0 + 122, y0 + 34), (x0 + 110, y0 + 62), (x0 + 134, y0 + 62)],
                 fill=(201, 162, 39))
    draw.polygon([(x0 + 178, y0 + 34), (x0 + 166, y0 + 62), (x0 + 190, y0 + 62)],
                 fill=(201, 162, 39))


def draw_awacs(draw, box):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    draw.rectangle(box, fill=SKY)
    # clouds
    for fx, fy in [(0.20, 0.22), (0.70, 0.38), (0.85, 0.16)]:
        cx, cy = x0 + int(w * fx), y0 + int(h * fy)
        draw.ellipse([cx - 16, cy - 6, cx + 16, cy + 6], fill=(255, 255, 255))
    # AWACS as a dark silhouette: fuselage + radar dome + tail + wings
    fy0 = y0 + int(h * 0.48)
    dark = (38, 52, 68)
    draw.ellipse([x0 + int(w * 0.10), fy0, x0 + int(w * 0.92), fy0 + int(h * 0.20)],
                 fill=dark)
    draw.ellipse([x0 + int(w * 0.38), fy0 - int(h * 0.16),
                  x0 + int(w * 0.62), fy0 + int(h * 0.06)], fill=dark)
    draw.polygon([(x0 + int(w * 0.86), fy0 + int(h * 0.04)),
                  (x0 + int(w * 0.96), fy0 - int(h * 0.18)),
                  (x0 + int(w * 0.96), fy0 + int(h * 0.04))], fill=dark)
    draw.polygon([(x0 + int(w * 0.14), fy0 + int(h * 0.10)),
                  (x0 + int(w * 0.44), fy0 + int(h * 0.30)),
                  (x0 + int(w * 0.14), fy0 + int(h * 0.30))], fill=dark)
    draw.polygon([(x0 + int(w * 0.52), fy0 + int(h * 0.10)),
                  (x0 + int(w * 0.76), fy0 + int(h * 0.32)),
                  (x0 + int(w * 0.52), fy0 + int(h * 0.32))], fill=dark)


def draw_cricket(draw, box):
    x0, y0, x1, y1 = box
    h = y1 - y0
    draw.rectangle(box, fill=(222, 238, 214))
    # pitch
    py0, py1 = y0 + int(h * 0.45), y1 - 4
    draw.rectangle([x0 + 8, py0, x1 - 8, py1], fill=(214, 190, 140))
    draw.line([x0 + 8, py0, x1 - 8, py0], fill=(255, 255, 255), width=2)
    # stumps
    for sx in (x0 + 22, x0 + 29, x0 + 36):
        draw.line([sx, py1 - 16, sx, py1 - 2], fill=(240, 200, 60), width=3)
    # bat, swung high
    draw.line([x0 + 52, py1 - 4, x0 + 96, y0 + 8], fill=(120, 82, 40), width=7)
    draw.rectangle([x0 + 88, y0 + 2, x0 + 110, y0 + 22], fill=(190, 150, 90))
    # ball flying
    draw.ellipse([x0 + 100, y0 + 26, x0 + 116, y0 + 42], fill=(166, 25, 46))
    # big "204" score, bottom-left of the art box
    sf = font(SANS_B, 30)
    draw.text((x0 + 8, py1 - 36), "204", font=sf, fill=RED)


# ------------------------------------------------------------------- layouts
def story_block(draw, box, story, head_start, head_lines, body_size=16,
                art=None, art_h=0, max_deck=2):
    """Headline + deck inside a panel; optional art strip on top.
    The deck is capped at max_deck lines so text can never spill past
    the panel border."""
    x0, y0, x1, y1 = box
    y = y0 + 12
    if art is not None:
        art(draw, (x0 + 12, y, x1 - 12, y + art_h))
        y += art_h + 10
    kf = font(SANS_B, 14)
    draw.text((x0 + 14, y), story["kicker"], font=kf, fill=RED)
    y += 22
    hf, lines = fit_headline(draw, story["headline"], SANS_B, head_start,
                             (x1 - x0) - 28, head_lines)
    y = draw_lines(draw, lines, x0 + 14, y, hf, INK)
    bf = font(SANS, body_size)
    blines = wrap(draw, story["deck"], bf, (x1 - x0) - 28)[:max_deck]
    draw_lines(draw, blines, x0 + 14, y + 6, bf, (60, 58, 52))


def story_block_side(draw, box, story, art, head_start=26):
    """Short panel: art square on the left, text column on the right.
    Used for the bottom row, where a top art strip would not fit."""
    x0, y0, x1, y1 = box
    art(draw, (x0 + 12, y0 + 12, x0 + 156, y1 - 12))
    tx = x0 + 170
    kf = font(SANS_B, 14)
    draw.text((tx, y0 + 14), story["kicker"], font=kf, fill=RED)
    hf, lines = fit_headline(draw, story["headline"], SANS_B, head_start,
                             (x1 - tx) - 14, 2)
    y = draw_lines(draw, lines, tx, y0 + 38, hf, INK)
    bf = font(SANS, 16)
    blines = wrap(draw, story["deck"], bf, (x1 - tx) - 14)[:2]
    draw_lines(draw, blines, tx, y + 6, bf, (60, 58, 52))


def variant1():
    """Hero lead + two rows of two panels + ticker. The proven shape:
    biggest story gets the biggest picture and the most words."""
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    dateband(d)
    # lead panel
    panel(d, [28, 152, 996, 512])
    d.rectangle([28, 152, 996, 192], fill=NAVY)
    kf = font(SANS_B, 15)
    d.text((44, 162), LEAD["kicker"], font=kf, fill=GOLD)
    hf, lines = fit_headline(d, LEAD["headline"], SANS_B, 46, 520, 3)
    y = draw_lines(d, lines, 44, 204, hf, INK)
    bf = font(SANS, 19)
    blines = wrap(d, LEAD["deck"], bf, 520)
    y = draw_lines(d, blines, 44, y + 8, bf, (60, 58, 52))
    cf = font(SANS, 14)
    d.text((44, 486), LEAD["credit"], font=cf, fill=GREY)
    draw_sea(d, (592, 200, 980, 500))
    # row 2: Huawei + Riyadh
    panel(d, [28, 528, 504, 772])
    story_block(d, (28, 528, 504, 772), HUAWEI, 28, 2, art=draw_court, art_h=72)
    panel(d, [520, 528, 996, 772])
    story_block(d, (520, 528, 996, 772), RIYADH, 28, 2, art=draw_tower, art_h=72)
    # row 3: NATO + cricket, side-art panels
    panel(d, [28, 788, 504, 960])
    story_block_side(d, (28, 788, 504, 960), NATO, draw_awacs)
    panel(d, [520, 788, 996, 960])
    story_block_side(d, (520, 788, 996, 960), CRICKET, draw_cricket)
    ticker(d)
    footer(d)
    return img


def variant2():
    """Tall lead column left, three stacked panels right, ticker."""
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    dateband(d)
    # lead column
    panel(d, [28, 152, 600, 960])
    d.rectangle([28, 152, 600, 192], fill=NAVY)
    kf = font(SANS_B, 15)
    d.text((44, 162), LEAD["kicker"], font=kf, fill=GOLD)
    hf, lines = fit_headline(d, LEAD["headline"], SANS_B, 44, 540, 4)
    y = draw_lines(d, lines, 44, 204, hf, INK)
    bf = font(SANS, 19)
    blines = wrap(d, LEAD["deck"], bf, 540)
    y = draw_lines(d, blines, 44, y + 8, bf, (60, 58, 52))
    draw_sea(d, (44, y + 16, 584, 900))
    cf = font(SANS, 14)
    d.text((44, 922), LEAD["credit"], font=cf, fill=GREY)
    # right stack
    panel(d, [616, 152, 996, 420])
    story_block(d, (616, 152, 996, 420), HUAWEI, 28, 2, art=draw_court, art_h=96)
    panel(d, [616, 436, 996, 700])
    story_block(d, (616, 436, 996, 700), RIYADH, 28, 2, art=draw_tower, art_h=96)
    panel(d, [616, 716, 996, 960])
    story_block(d, (616, 716, 996, 960), CRICKET, 26, 2, art=draw_cricket,
                art_h=64)
    # NATO moves to the ticker line area: a thin strip under the lead
    ticker(d)
    footer(d)
    return img


def variant3():
    """Six equal panels in a 2x3 grid + date strip. Flat, no hierarchy."""
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    dateband(d)
    stories = [LEAD, HUAWEI, RIYADH, NATO, CRICKET]
    arts = [draw_sea, draw_court, draw_tower, draw_awacs, draw_cricket]
    boxes = [(28, 152, 504, 420), (520, 152, 996, 420),
             (28, 436, 504, 700), (520, 436, 996, 700),
             (28, 716, 996, 960)]
    for box, story, art in zip(boxes, stories, arts):
        panel(d, list(box))
        ah = 110 if box[2] - box[0] < 500 else 130
        story_block(d, box, story, 26, 2, art=art, art_h=ah)
    ticker(d)
    footer(d)
    return img


VARIANTS = {"v1": variant1, "v2": variant2, "v3": variant3}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    names = sys.argv[1:] or ["all"]
    if names == ["all"]:
        names = list(VARIANTS)
    for name in names:
        img = VARIANTS[name]()
        path = OUT / f"{name}.png"
        img.save(path, optimize=True)
        print(f"{name}: {path} {path.stat().st_size} bytes "
              f"{img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
