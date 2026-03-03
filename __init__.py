"""
MIDIToolkit public API.

This file re-exports the main classes so users can write:
    from MIDIToolkit import MIDIFile, Track, NoteEvent, TempoEvent, ...
"""

from .MIDIToolkit import (
    MIDIFile,
    Track,
    TempoMap,
    MIDIEvent,
    NoteEvent,
    TempoEvent,
    PatchChangeEvent,
    ControlChangeEvent,
    KeySignatureEvent,
    PluginRegistry,
    MIDIPlugin,
    wrap_event,
)

__all__ = [
    "MIDIFile",
    "Track",
    "TempoMap",
    "MIDIEvent",
    "NoteEvent",
    "TempoEvent",
    "PatchChangeEvent",
    "ControlChangeEvent",
    "KeySignatureEvent",
    "PluginRegistry",
    "MIDIPlugin",
    "wrap_event",
]