The Grand Archive
=================

The Grand Archive is just a giant repostiory of information. It contains billions of articles on every area the Imperium has ever studied. These articles are interlinked via a very complex network of cross-references, that only [Cognitors](../ocupations/cognitor.md) know how to navigate.

Many minds have been lost trying to navigate the archive, driven mad by endless information loops.

Information Organization
------------------------

The Grand Archive recieves one shipment of information per Imperial year. It is the only time one is allowed to _write_ to the storage. This is performed by the [Archmagos Cognitor](../ocupations/cognitor.md#archmagos-cognitor), during the [Data Entry Rites](../traditions/data_entry_rites.md)

Each document is assigned a unique identifier, calculated as such:

| Date of Entry | Clearance | Id   |
|---------------|-----------|------|
| M40-896       | MINISTER  | 3382 |

The *Clearance* is generated from the following list:

- `POPULUS`: Public information.
- `MINISTER`: Information only available for public officials and administratum employees.
- `MILITIA`: Information available to the Military, including Astra Militarum, Astartes, Sororitas, and of course the Inquisition
- `ORDOS`: Information only available to mebers of the Ordos.

The *Id* is an monotonically increasing number, guaranteed to be unique within the (date, clearance) tuples.

*Note:* This format can cause data corruption. Two documents have the same Id, but different clearances. If one updates the clearance but not the Id, there's trouble.
