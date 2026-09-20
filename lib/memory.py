"""Logik & Assets für Station 6 · Instrumenten-Memory."""
from __future__ import annotations

import base64
import mimetypes
import random
from dataclasses import dataclass, field
from pathlib import Path

SOUND_DIR = Path(__file__).resolve().parent.parent / "assets" / "sounds" / "memory"
SUPPORTED_SUFFIXES = {".mp3", ".wav", ".ogg", ".m4a", ".aac"}

DIFFICULTIES = {
    "easy":   {"label": "Einfach",  "pairs": 4,  "cols": 4},
    "normal": {"label": "Normal",   "pairs": 8,  "cols": 4},
    "hard":   {"label": "Schwer",   "pairs": 12, "cols": 6},
}

# Anzeigenamen für erwartete Dateinamen. Kleinbuchstaben ohne Endung.
DISPLAY_NAMES = {
    "trompete":   "Trompete",
    "posaune":    "Posaune",
    "horn":       "Waldhorn",
    "tuba":       "Tuba",
    "fluegelhorn": "Flügelhorn",
    "flugelhorn": "Flügelhorn",
    "saxophon":   "Saxophon",
    "klarinette": "Klarinette",
    "querfloete": "Querflöte",
    "querflote":  "Querflöte",
    "oboe":       "Oboe",
    "fagott":     "Fagott",
    "euphonium":  "Euphonium",
    "cornet":     "Cornet",
    "kornett":    "Kornett",
    "bariton":    "Bariton",
    "sousaphon":  "Sousaphon",
    "piccolo":    "Piccolo",
}


@dataclass
class Instrument:
    key: str            # z.B. "trompete"
    display: str        # z.B. "Trompete"
    path: Path
    data_uri: str = ""  # base64-eingebettetes Audio für Autoplay


def _display_for(key: str) -> str:
    return DISPLAY_NAMES.get(key.lower(), key.replace("_", " ").title())


def _to_data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    if mime is None:
        mime = "audio/mpeg"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def load_instruments() -> list[Instrument]:
    """Liest alle Sound-Files aus dem assets-Ordner. Kein Sound → leere Liste."""
    if not SOUND_DIR.exists():
        return []
    instruments: list[Instrument] = []
    for p in sorted(SOUND_DIR.iterdir()):
        if p.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        key = p.stem.lower()
        try:
            uri = _to_data_uri(p)
        except OSError:
            continue
        instruments.append(Instrument(key=key, display=_display_for(key), path=p, data_uri=uri))
    return instruments


@dataclass
class Card:
    idx: int
    instrument_key: str
    revealed: bool = False
    matched: bool = False


@dataclass
class GameState:
    difficulty: str
    cards: list[Card] = field(default_factory=list)
    first_pick: int | None = None
    second_pick: int | None = None
    moves: int = 0
    matched_pairs: int = 0
    play_key: str | None = None  # welchen Sound wir gerade abspielen sollen

    @property
    def total_pairs(self) -> int:
        return len(self.cards) // 2

    @property
    def finished(self) -> bool:
        return self.matched_pairs == self.total_pairs and self.total_pairs > 0


def new_game(difficulty: str, instruments: list[Instrument]) -> GameState:
    cfg = DIFFICULTIES[difficulty]
    pool = instruments[: cfg["pairs"]]
    keys = [inst.key for inst in pool] * 2
    random.shuffle(keys)
    cards = [Card(idx=i, instrument_key=k) for i, k in enumerate(keys)]
    return GameState(difficulty=difficulty, cards=cards)


def reveal_card(state: GameState, idx: int) -> None:
    """Klick-Logik: erste Karte, zweite Karte, Match-Check."""
    card = state.cards[idx]
    if card.matched or card.revealed:
        return

    # Wenn zwei Karten offen und noch nicht ausgewertet → zurücksetzen
    if state.first_pick is not None and state.second_pick is not None:
        c1 = state.cards[state.first_pick]
        c2 = state.cards[state.second_pick]
        if c1.instrument_key != c2.instrument_key:
            c1.revealed = False
            c2.revealed = False
        state.first_pick = None
        state.second_pick = None

    card.revealed = True
    state.play_key = card.instrument_key

    if state.first_pick is None:
        state.first_pick = idx
        return

    state.second_pick = idx
    state.moves += 1

    c1 = state.cards[state.first_pick]
    c2 = state.cards[state.second_pick]
    if c1.instrument_key == c2.instrument_key:
        c1.matched = True
        c2.matched = True
        state.matched_pairs += 1
        state.first_pick = None
        state.second_pick = None
